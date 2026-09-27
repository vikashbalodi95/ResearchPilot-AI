from app.tools.tool_selector import ToolSelector


selector = ToolSelector()


questions = [
    "What is machine learning?",
    "How many words are in this document?",
    "What is the character count of this file?",
]


for question in questions:

    selected_tool = selector.select_tool(question)

    print(f"Question: {question}")
    print(f"Selected Tool: {selected_tool}")
    print()