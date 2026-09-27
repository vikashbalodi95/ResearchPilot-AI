import asyncio

from app.agents.research_agent import ResearchAgent


async def main():

    agent = ResearchAgent()

    result = await agent.research(
        "What is machine learning?"
    )

    print("\nFinal Answer:\n")
    print(result)


asyncio.run(main())