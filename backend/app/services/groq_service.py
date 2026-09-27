from fastapi import HTTPException
from openai import AsyncOpenAI

from app.core.config import settings
from app.core.logger import logger
from app.prompt.templates import RESEARCH_SYSTEM_PROMPT


class GroqService:

    def __init__(self):
        if not settings.GROQ_API_KEY:
            raise HTTPException(
                status_code=503,
                detail="GROQ_API_KEY is not configured. Add it to backend/.env before running research.",
            )

        self.client = AsyncOpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )

    async def generate_response(
        self,
        prompt: str,
        context: str = "",
    ):

        logger.info("Sending request to Groq API")

        try:
            messages = [
                {
                    "role": "system",
                    "content": RESEARCH_SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"""
Research Context:
{context}

User Question:
{prompt}
""",
                },
            ]

            response = await self.client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
            )

            logger.info(
                "Response received successfully from Groq API"
            )

            return response.choices[0].message.content

        except Exception as e:
            logger.exception(f"Groq API Error: {e}")
            raise