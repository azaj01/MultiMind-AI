"""Scoring functions for benchmark evaluation.

Provides exact-match, code execution, rubric-based, and delegation
accuracy scorers.
"""

from __future__ import annotations

import re
import subprocess
import tempfile
import textwrap
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Numeric exact match (GSM8K-style)
# ---------------------------------------------------------------------------

def extract_numeric_answer(text: str) -> str | None:
    """Extract the final numeric answer from model output.

    Looks for patterns like '#### 42', 'the answer is 42', or falls back
    to the last standalone number in the text.
    """
    # Pattern 1: GSM8K-style delimiter
    m = re.search(r"####\s*([\-\d,\.]+)", text)
    if m:
        return m.group(1).replace(",", "").strip()

    # Pattern 2: "the answer is X"
    m = re.search(
        r"(?:the\s+)?answer\s+is[:\s]*([\-\d,\.]+)", text, re.IGNORECASE
    )
    if m:
        return m.group(1).replace(",", "").strip()

    # Pattern 3: boxed answer (LaTeX)
    m = re.search(r"\\boxed\{([\-\d,\.]+)\}", text)
    if m:
        return m.group(1).replace(",", "").strip()

    # Fallback: last number in text
    numbers = re.findall(r"(?<!\w)([\-]?\d[\d,]*\.?\d*)(?!\w)", text)
    if numbers:
        return numbers[-1].replace(",", "").strip()

    return None


def score_exact_numeric(expected: str, actual: str) -> float:
    """Score 1.0 if final numeric answer matches, 0.0 otherwise."""
    extracted = extract_numeric_answer(actual)
    if extracted is None:
        return 0.0

    try:
        expected_val = float(expected.replace(",", "").strip())
        actual_val = float(extracted)
        # Allow tiny floating-point tolerance
        return 1.0 if abs(expected_val - actual_val) < 1e-6 else 0.0
    except (ValueError, TypeError):
        return 1.0 if expected.strip() == extracted.strip() else 0.0


# ---------------------------------------------------------------------------
# Code execution (pass@1)
# ---------------------------------------------------------------------------

def score_code_pass(
    model_output: str,
    test_code: str,
    timeout_seconds: int = 15,
) -> dict[str, Any]:
    """Execute model-generated code + test assertions, return pass/fail.

    Returns dict with keys: passed (bool), error (str | None).
    """
    # Extract code block from model output
    code = _extract_code_block(model_output)
    if not code:
        return {"passed": False, "error": "No code block found in output"}

    full_script = code + "\n\n" + test_code

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False
    ) as f:
        f.write(full_script)
        f.flush()
        tmp_path = Path(f.name)

    try:
        result = subprocess.run(
            ["python3", str(tmp_path)],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
        if result.returncode == 0:
            return {"passed": True, "error": None}
        return {"passed": False, "error": result.stderr[:500]}
    except subprocess.TimeoutExpired:
        return {"passed": False, "error": "Execution timed out"}
    except Exception as exc:
        return {"passed": False, "error": str(exc)[:500]}
    finally:
        tmp_path.unlink(missing_ok=True)


def _extract_code_block(text: str) -> str | None:
    """Extract the first Python code block from markdown output."""
    # Try fenced code block
    m = re.search(
        r"```(?:python)?\s*\n(.*?)```", text, re.DOTALL
    )
    if m:
        return m.group(1).strip()

    # Try indented code (4 spaces) — only if substantial
    lines = text.split("\n")
    code_lines = []
    for line in lines:
        if line.startswith("    ") or line.startswith("\t"):
            code_lines.append(line)
        elif code_lines and line.strip() == "":
            code_lines.append("")  # preserve blank lines in code
        elif code_lines:
            break

    if len(code_lines) >= 3:
        return textwrap.dedent("\n".join(code_lines)).strip()

    # If the output looks like pure code (starts with def/class/import)
    stripped = text.strip()
    if stripped and re.match(r"^(def |class |import |from )", stripped):
        return stripped

    return None


# ---------------------------------------------------------------------------
# Delegation accuracy (org mode)
# ---------------------------------------------------------------------------

def score_delegation(
    expected_departments: list[str],
    actual_output: str,
) -> dict[str, Any]:
    """Score how well the CEO delegated to the correct departments.

    Returns dict with: accuracy (float), matched (list), missed (list), extra (list).
    """
    # Try to parse the CEO's JSON output to find department names
    actual_depts: set[str] = set()

    # Look for department names in the output
    import json

    try:
        parsed = json.loads(actual_output)
        if isinstance(parsed, list):
            for item in parsed:
                if isinstance(item, dict) and "department" in item:
                    actual_depts.add(item["department"])
    except (json.JSONDecodeError, TypeError):
        pass

    # Fallback: search for department names as strings
    if not actual_depts:
        from multimind.org_roles import VALID_DEPARTMENTS

        for dept in VALID_DEPARTMENTS:
            if dept.lower() in actual_output.lower():
                actual_depts.add(dept)

    expected_set = set(expected_departments)
    matched = expected_set & actual_depts
    missed = expected_set - actual_depts
    extra = actual_depts - expected_set

    accuracy = len(matched) / len(expected_set) if expected_set else 0.0

    return {
        "accuracy": accuracy,
        "matched": sorted(matched),
        "missed": sorted(missed),
        "extra": sorted(extra),
    }


# ---------------------------------------------------------------------------
# Rubric scoring (human-review output)
# ---------------------------------------------------------------------------

def generate_rubric_template(
    question: str,
    model_output: str,
    checklist: list[str],
) -> str:
    """Generate a markdown rubric template for human review.

    Returns a markdown string with checkboxes for each rubric criterion.
    """
    lines = [
        "## Rubric Evaluation",
        "",
        f"**Prompt:** {question[:200]}{'...' if len(question) > 200 else ''}",
        "",
        "### Scores (1-5)",
        "",
        "| Criterion | Score | Notes |",
        "|-----------|-------|-------|",
        "| Correctness | /5 | |",
        "| Completeness | /5 | |",
        "| Coherence | /5 | |",
        "| Depth | /5 | |",
        "",
        "### Checklist",
        "",
    ]
    for item in checklist:
        lines.append(f"- [ ] {item}")

    lines.extend([
        "",
        "### Model Output (first 500 chars)",
        "",
        f"```\n{model_output[:500]}\n```",
    ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Aggregate scoring
# ---------------------------------------------------------------------------

def compute_suite_metrics(
    results: list[dict[str, Any]],
    score_fn: str = "exact_numeric",
) -> dict[str, Any]:
    """Compute aggregate metrics for a suite of results.

    Returns: accuracy, mean_time, median_time, total_chars, self_correction_rate.
    """
    if not results:
        return {}

    scores = []
    times = []
    chars = []
    corrections = 0
    correction_improvements = 0
    total_hard = 0

    for r in results:
        expected = r.get("expected_answer", "")
        actual = r.get("final_answer", "")

        if score_fn == "exact_numeric":
            s = score_exact_numeric(expected, actual)
        else:
            s = 0.0  # placeholder for other scoring

        scores.append(s)
        times.append(r.get("wall_time_seconds", 0.0))
        chars.append(r.get("total_output_chars", 0))

        meta = r.get("metadata", {})
        if meta.get("self_corrected") is not None:
            total_hard += 1
            if meta["self_corrected"]:
                corrections += 1

    accuracy = sum(scores) / len(scores) if scores else 0.0
    sorted_times = sorted(times)
    median_time = sorted_times[len(sorted_times) // 2] if sorted_times else 0.0

    return {
        "accuracy": round(accuracy, 4),
        "total_questions": len(results),
        "correct": int(sum(scores)),
        "mean_time_seconds": round(sum(times) / len(times), 2) if times else 0,
        "median_time_seconds": round(median_time, 2),
        "total_output_chars": sum(chars),
        "self_correction_rate": (
            round(corrections / total_hard, 4) if total_hard > 0 else None
        ),
    }
