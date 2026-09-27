from app.services.groq_service import generate_response

response = generate_response(
    "Explain Agentic AI in one sentence."
)

print(response)
