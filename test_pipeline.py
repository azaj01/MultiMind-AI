import asyncio
from multimind.llm_client import LocalLLMClient
from multimind.pipeline import run_pipeline

class MockLLMClient(LocalLLMClient):
    async def stream_chat(self, *args, **kwargs):
        yield "Mock response"

async def main():
    client = MockLLMClient()
    model_map = {"plan": "model", "execute": "model", "critique": "model"}
    async for event in run_pipeline(
        client=client,
        provider_kind="openai",
        base_url="http://localhost",
        model_map=model_map,
        ollama_think=False,
        user_message="Test message",
        mode="hard",
        max_iterations=2
    ):
        print(f"Event: {event.get('type')}, step: {event.get('step')}")

asyncio.run(main())
