from __future__ import annotations

import json
from collections.abc import AsyncIterator

import httpx

from multimind.config import REQUEST_TIMEOUT_SECONDS
from multimind.discovery import normalize_base_url


class LocalLLMClient:
    def __init__(self) -> None:
        self._client = httpx.AsyncClient(timeout=REQUEST_TIMEOUT_SECONDS)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def stream_chat(
        self,
        *,
        provider_kind: str,
        base_url: str,
        model: str,
        messages: list[dict[str, str]],
        temperature: float = 0.2,
    ) -> AsyncIterator[str]:
        if provider_kind == "ollama":
            async for token in self._stream_ollama(
                base_url=base_url,
                model=model,
                messages=messages,
                temperature=temperature,
            ):
                yield token
            return

        async for token in self._stream_openai(
            base_url=base_url,
            model=model,
            messages=messages,
            temperature=temperature,
        ):
            yield token

    async def _stream_ollama(
        self,
        *,
        base_url: str,
        model: str,
        messages: list[dict[str, str]],
        temperature: float,
    ) -> AsyncIterator[str]:
        payload = {
            "model": model,
            "messages": messages,
            "stream": True,
            "options": {"temperature": temperature},
        }

        async with self._client.stream(
            "POST",
            f"{normalize_base_url(base_url)}/api/chat",
            json=payload,
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if not line:
                    continue

                payload = json.loads(line)
                message = payload.get("message") or {}
                content = message.get("content")
                if content:
                    yield content
                if payload.get("done"):
                    break

    async def _stream_openai(
        self,
        *,
        base_url: str,
        model: str,
        messages: list[dict[str, str]],
        temperature: float,
    ) -> AsyncIterator[str]:
        payload = {
            "model": model,
            "messages": messages,
            "stream": True,
            "temperature": temperature,
        }

        async with self._client.stream(
            "POST",
            f"{normalize_base_url(base_url)}/v1/chat/completions",
            json=payload,
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if not line or not line.startswith("data:"):
                    continue

                data = line.removeprefix("data:").strip()
                if data == "[DONE]":
                    break

                payload = json.loads(data)
                choices = payload.get("choices") or []
                if not choices:
                    continue

                delta = choices[0].get("delta") or {}
                content = delta.get("content")
                if content:
                    yield content