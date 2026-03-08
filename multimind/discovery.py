from __future__ import annotations

from dataclasses import asdict, dataclass

import httpx

from multimind.config import DISCOVERY_CANDIDATES, DISCOVERY_TIMEOUT_SECONDS, ProviderCandidate


@dataclass
class ProviderInfo:
    name: str
    kind: str
    base_url: str
    available: bool
    models: list[str]
    error: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


async def discover_providers() -> list[ProviderInfo]:
    providers: list[ProviderInfo] = []
    async with httpx.AsyncClient(timeout=DISCOVERY_TIMEOUT_SECONDS) as client:
        for candidate in DISCOVERY_CANDIDATES:
            providers.append(await probe_provider(client, candidate))
    return providers


async def probe_provider(client: httpx.AsyncClient, candidate: ProviderCandidate) -> ProviderInfo:
    base_url = normalize_base_url(candidate.base_url)

    try:
        if candidate.kind == "ollama":
            response = await client.get(f"{base_url}/api/tags")
            response.raise_for_status()
            payload = response.json()
            models = [item.get("model") or item.get("name") for item in payload.get("models", [])]
        else:
            response = await client.get(f"{base_url}/v1/models")
            response.raise_for_status()
            payload = response.json()
            models = [item.get("id") for item in payload.get("data", [])]

        clean_models = [model for model in models if model]
        return ProviderInfo(
            name=candidate.name,
            kind=candidate.kind,
            base_url=base_url,
            available=True,
            models=clean_models,
        )
    except Exception as exc:
        return ProviderInfo(
            name=candidate.name,
            kind=candidate.kind,
            base_url=base_url,
            available=False,
            models=[],
            error=str(exc),
        )


def select_default_provider(providers: list[ProviderInfo]) -> ProviderInfo | None:
    for provider in providers:
        if provider.available and provider.models:
            return provider
    for provider in providers:
        if provider.available:
            return provider
    return None