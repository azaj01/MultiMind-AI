"""Report generator — converts JSON results into a Markdown benchmark report."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _pct(value: float) -> str:
    return f"{value:.1%}"


def _sec(value: float) -> str:
    return f"{value:.1f}s"


def generate_report(results_dir: Path, output_path: Path | None = None) -> str:
    """Generate a Markdown report from benchmark results.

    Reads summary.json if available, otherwise scans for per-run JSON files.
    Returns the report as a string and optionally writes to *output_path*.
    """
    summary_path = results_dir / "summary.json"
    summary: dict[str, Any] = {}
    runs: dict[str, Any] = {}

    if summary_path.exists():
        summary = json.loads(summary_path.read_text())
        runs = summary.get("runs", {})
    else:
        # Fallback: scan for all {suite}__{model}__{mode}.json files
        import re
        from benchmarks.run_benchmarks import _load_suite
        from benchmarks.scorer import compute_suite_metrics

        for f in results_dir.glob("*.json"):
            if f.name == "summary.json":
                continue

            # Expected name format: suite__model__mode.json
            # Fallback for simpler names: name.json -> used as suite_name
            match = re.match(r"(.+?)__(.+?)__(.+?)\.json", f.name)
            if match:
                suite_name, model, mode = match.groups()
            else:
                suite_name = f.stem
                model = "unknown"
                mode = "unknown"

            run_key = f"{suite_name}__{model}__{mode}"
            
            try:
                result_dicts = json.loads(f.read_text())
                # Try to load suite info to get score type
                try:
                    _, score_type = _load_suite(suite_name)
                except ValueError:
                    score_type = "unknown"
                
                runs[run_key] = compute_suite_metrics(result_dicts, score_type)
            except Exception:
                continue

        summary = {
            "timestamp": "N/A (Inferred from files)",
            "total_time_seconds": 0,
            "models": list(set(k.split("__")[1] for k in runs.keys())),
            "council_models": [],
            "runs": runs
        }

    if not runs:
        return "# Error\n\nNo result files found in results directory."

    lines: list[str] = []
    lines.append("# MultiMind AI — Benchmark Report\n")
    lines.append(f"**Generated:** {summary.get('timestamp', 'N/A')}\n")
    lines.append(f"**Total runtime:** {_sec(summary.get('total_time_seconds', 0))}\n")
    lines.append(f"**Models:** {', '.join(summary.get('models', []))}\n")
    lines.append(f"**Council advisors:** {', '.join(summary.get('council_models', []))}\n")
    lines.append("---\n")

    # ── Group runs by suite ──────────────────────────────────────────
    suites: dict[str, list[tuple[str, dict]]] = {}
    for run_key, metrics in runs.items():
        parts = run_key.split("__")
        suite_name = parts[0]
        suites.setdefault(suite_name, []).append((run_key, metrics))

    for suite_name, suite_runs in suites.items():
        lines.append(f"## {suite_name}\n")

        # Build accuracy table
        if any(r[1].get("accuracy") is not None for r in suite_runs):
            lines.append("### Accuracy\n")
            lines.append("| Model | Mode | Accuracy | Correct | Total | Median Time |")
            lines.append("|-------|------|----------|---------|-------|-------------|")

            for run_key, metrics in sorted(suite_runs, key=lambda x: x[0]):
                parts = run_key.split("__")
                model = parts[1] if len(parts) > 1 else "?"
                mode = parts[2] if len(parts) > 2 else "?"
                acc = metrics.get("accuracy", 0)
                correct = metrics.get("correct", 0)
                total = metrics.get("total_questions", 0)
                median = metrics.get("median_time_seconds", 0)

                lines.append(
                    f"| {model} | {mode} | {_pct(acc)} | {correct} | {total} | {_sec(median)} |"
                )

            lines.append("")

        # Reasoning effort comparison (off vs medium vs hard)
        _add_reasoning_effort_analysis(lines, suite_runs)

        # Self-correction analysis (hard mode)
        _add_self_correction_analysis(lines, suite_runs)

        # Token overhead analysis
        _add_overhead_analysis(lines, suite_runs)

        lines.append("---\n")

    # ── Cross-suite summary ──────────────────────────────────────────
    lines.append("## Cross-Suite Summary\n")
    _add_cross_suite_summary(lines, suites)

    report = "\n".join(lines)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report)

    return report


def _add_reasoning_effort_analysis(
    lines: list[str], suite_runs: list[tuple[str, dict]]
) -> None:
    """Add Δ accuracy analysis between off/medium/hard modes."""
    # Group by model
    by_model: dict[str, dict[str, float]] = {}
    for run_key, metrics in suite_runs:
        parts = run_key.split("__")
        if len(parts) < 3:
            continue
        model = parts[1]
        mode = parts[2]
        if mode in ("off", "medium", "hard"):
            by_model.setdefault(model, {})[mode] = metrics.get("accuracy", 0)

    if not by_model:
        return

    has_deltas = any(len(modes) > 1 for modes in by_model.values())
    if not has_deltas:
        return

    lines.append("### Reasoning Effort Delta\n")
    lines.append("| Model | off | medium | hard | Δ(medium-off) | Δ(hard-off) |")
    lines.append("|-------|-----|--------|------|---------------|-------------|")

    for model, modes in sorted(by_model.items()):
        off = modes.get("off", 0)
        med = modes.get("medium", 0)
        hard = modes.get("hard", 0)
        delta_m = med - off
        delta_h = hard - off

        sign_m = "+" if delta_m >= 0 else ""
        sign_h = "+" if delta_h >= 0 else ""

        lines.append(
            f"| {model} | {_pct(off)} | {_pct(med)} | {_pct(hard)} "
            f"| {sign_m}{_pct(delta_m)} | {sign_h}{_pct(delta_h)} |"
        )

    lines.append("")


def _add_self_correction_analysis(
    lines: list[str], suite_runs: list[tuple[str, dict]]
) -> None:
    """Show self-correction rate for hard mode runs."""
    hard_runs = [
        (k, m)
        for k, m in suite_runs
        if "__hard" in k and m.get("self_correction_rate") is not None
    ]
    if not hard_runs:
        return

    lines.append("### Self-Correction (Hard Mode)\n")
    lines.append("| Model | Self-Correction Rate |")
    lines.append("|-------|---------------------|")

    for run_key, metrics in sorted(hard_runs):
        model = run_key.split("__")[1] if "__" in run_key else "?"
        rate = metrics.get("self_correction_rate", 0)
        lines.append(f"| {model} | {_pct(rate)} |")

    lines.append("")


def _add_overhead_analysis(
    lines: list[str], suite_runs: list[tuple[str, dict]]
) -> None:
    """Show time and token overhead relative to off mode."""
    by_model: dict[str, dict[str, dict]] = {}
    for run_key, metrics in suite_runs:
        parts = run_key.split("__")
        if len(parts) < 3:
            continue
        model, mode = parts[1], parts[2]
        by_model.setdefault(model, {})[mode] = metrics

    has_comparison = any(
        "off" in modes and len(modes) > 1 for modes in by_model.values()
    )
    if not has_comparison:
        return

    lines.append("### Overhead vs Off Mode\n")
    lines.append("| Model | Mode | Time Ratio | Char Ratio |")
    lines.append("|-------|------|------------|------------|")

    for model, modes in sorted(by_model.items()):
        off_time = modes.get("off", {}).get("median_time_seconds", 1)
        off_chars = modes.get("off", {}).get("total_output_chars", 1)

        for mode_name in ("medium", "hard", "council", "org"):
            if mode_name not in modes:
                continue
            m = modes[mode_name]
            t_ratio = m.get("median_time_seconds", 0) / max(off_time, 0.01)
            c_ratio = m.get("total_output_chars", 0) / max(off_chars, 1)
            lines.append(
                f"| {model} | {mode_name} | {t_ratio:.1f}× | {c_ratio:.1f}× |"
            )

    lines.append("")


def _add_cross_suite_summary(
    lines: list[str], suites: dict[str, list[tuple[str, dict]]]
) -> None:
    """Add a high-level summary across all suites."""
    lines.append("| Suite | Best Model | Best Mode | Best Accuracy |")
    lines.append("|-------|------------|-----------|---------------|")

    for suite_name, suite_runs in sorted(suites.items()):
        best_run = None
        best_acc = -1.0
        for run_key, metrics in suite_runs:
            acc = metrics.get("accuracy", 0)
            if acc > best_acc:
                best_acc = acc
                best_run = run_key

        if best_run:
            parts = best_run.split("__")
            model = parts[1] if len(parts) > 1 else "?"
            mode = parts[2] if len(parts) > 2 else "?"
            lines.append(
                f"| {suite_name} | {model} | {mode} | {_pct(best_acc)} |"
            )

    lines.append("")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate benchmark report")
    parser.add_argument(
        "--results",
        default="benchmarks/results",
        help="Results directory (default: benchmarks/results)",
    )
    parser.add_argument(
        "--output",
        default="benchmarks/results/report.md",
        help="Output report path (default: benchmarks/results/report.md)",
    )
    args = parser.parse_args()

    report = generate_report(
        results_dir=Path(args.results),
        output_path=Path(args.output),
    )
    print(report)
    print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
