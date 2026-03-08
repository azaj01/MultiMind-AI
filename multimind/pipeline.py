from __future__ import annotations

from collections.abc import AsyncIterator

from multimind.config import PIPELINE_STEPS
from multimind.llm_client import LocalLLMClient
from multimind.markdown_render import render_markdown_to_html


STEP_LABELS = {
    "plan": "Planning",
    "execute": "Executing",
    "critique": "Critiquing",
}

def _system_prompt_for_plan() -> str:
    return (
        "You are the expert analytical planning stage in a multi-step reasoning pipeline.\n"
        "Your task: carefully analyze the user request and map out a step-by-step strategy to solve it.\n"
        "Instructions:\n"
        "1. Break down the problem logically.\n"
        "2. Identify any edge cases, constraints, or complexities.\n"
        "3. Provide a clear, actionable roadmap using bullet points.\n"
        "4. DO NOT provide the final answer or write the actual solution. Focus entirely on HOW to solve it."
    )


def _system_prompt_for_execute(mode: str) -> str:
    if mode == "hard":
        return (
            "You are the expert execution stage in a reasoning pipeline.\n"
            "Your task: follow the provided plan strictly to formulate the most comprehensive and accurate draft answer possible.\n"
            "Instructions:\n"
            "1. Think step-by-step, reasoning thoroughly based on the provided plan.\n"
            "2. Ensure all constraints and requirements from the user request are fully met.\n"
            "3. Be highly detailed, explicit, and rigorous in your execution.\n"
            "4. Leave no ambiguity or gaps in your draft solution."
        )

    return (
        "You are the expert execution stage in a reasoning pipeline. "
        "Use the provided plan to smoothly produce a final, highly polished, and directly useful user-facing answer. "
        "Think step-by-step to ensure accuracy, but keep the final output clean and thorough."
    )


def _system_prompt_for_critique() -> str:
    return (
        "You are the expert critique and revision stage in a reasoning pipeline.\n"
        "Your task: rigorously review the draft answer against the original user request and the plan.\n"
        "Instructions:\n"
        "1. Actively look for factual mistakes, weak logic, omissions, or failure to follow constraints.\n"
        "2. Synthesize your corrections into a significantly improved, superior final response.\n"
        "3. Output ONLY the improved final answer. Do not include any meta-commentary, explanations of what you changed, or introductory/concluding filler."
    )



def _build_messages_for_plan(user_message: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": _system_prompt_for_plan()},
        {"role": "user", "content": user_message},
    ]


def _build_messages_for_execute(user_message: str, plan: str, mode: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": _system_prompt_for_execute(mode)},
        {
            "role": "user",
            "content": (
                f"User request:\n{user_message}\n\n"
                f"Plan:\n{plan or 'No plan was generated.'}\n\n"
                "Write the best possible answer."
            ),
        },
    ]


def _build_messages_for_critique(user_message: str, plan: str, draft: str) -> list[dict[str, str]]:
    return [
        {"role": "system", "content": _system_prompt_for_critique()},
        {
            "role": "user",
            "content": (
                f"User request:\n{user_message}\n\n"
                f"Plan:\n{plan or 'No plan was generated.'}\n\n"
                f"Draft answer:\n{draft or 'No draft answer was generated.'}\n\n"
                "Provide the corrected final answer."
            ),
        },
    ]


def _pipeline_for_mode(mode: str) -> tuple[str, ...]:
    if mode == "off":
        return ("execute",)
    if mode == "medium":
        return ("plan", "execute")
    return PIPELINE_STEPS


async def run_pipeline(
    *,
    client: LocalLLMClient,
    provider_kind: str,
    base_url: str,
    model_map: dict[str, str],
    user_message: str,
    mode: str,
) -> AsyncIterator[dict]:
    steps = _pipeline_for_mode(mode)
    outputs: dict[str, str] = {}

    yield {"type": "run-start", "mode": mode, "steps": list(steps)}

    for step in steps:
        model = model_map.get(step) or model_map.get("execute") or ""
        if not model:
            raise ValueError(f"No model configured for step '{step}'.")

        yield {
            "type": "step-start",
            "step": step,
            "label": STEP_LABELS[step],
            "model": model,
            "thought": step != "execute" or mode == "hard",
        }

        if step == "execute" and mode != "hard":
            yield {"type": "answer-start", "step": step, "label": STEP_LABELS[step], "model": model}
        if step == "critique":
            yield {"type": "answer-start", "step": step, "label": STEP_LABELS[step], "model": model}

        if step == "plan":
            messages = _build_messages_for_plan(user_message)
        elif step == "execute":
            messages = _build_messages_for_execute(user_message, outputs.get("plan", ""), mode)
        else:
            messages = _build_messages_for_critique(
                user_message,
                outputs.get("plan", ""),
                outputs.get("execute", ""),
            )

        buffer: list[str] = []
        partial_content = ""
        async for token in client.stream_chat(
            provider_kind=provider_kind,
            base_url=base_url,
            model=model,
            messages=messages,
        ):
            buffer.append(token)
            partial_content += token
            yield {
                "type": "step-delta",
                "step": step,
                "delta": token,
                "content": partial_content,
                "html": render_markdown_to_html(partial_content),
            }

            if (step == "execute" and mode != "hard") or step == "critique":
                yield {
                    "type": "answer-delta",
                    "step": step,
                    "delta": token,
                    "content": partial_content,
                    "html": render_markdown_to_html(partial_content),
                }

        outputs[step] = "".join(buffer).strip()
        yield {
            "type": "step-complete",
            "step": step,
            "content": outputs[step],
            "html": render_markdown_to_html(outputs[step]),
        }

        if (step == "execute" and mode != "hard") or step == "critique":
            yield {
                "type": "answer-complete",
                "step": step,
                "content": outputs[step],
                "html": render_markdown_to_html(outputs[step]),
            }

    if mode == "off":
        outputs["final"] = outputs.get("execute", "")
    elif mode == "medium":
        outputs["final"] = outputs.get("execute", "")
    else:
        outputs["final"] = outputs.get("critique", "")

    yield {"type": "run-complete", "outputs": outputs}