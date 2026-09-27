from openai import OpenAI
from app.core.config import settings


client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

models = client.models.list()

print("\nAvailable Groq Models:\n")

for model in models.data:
    print(model.id)