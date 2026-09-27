class ToolSelector:

    def select_tool(self, question: str):

        question_lower = question.lower()

        document_keywords = [
            "word count",
            "character count",
            "document info",
            "file info",
            "how many words",
            "how many characters",
        ]

        for keyword in document_keywords:
            if keyword in question_lower:
                return "document"

        return "retrieval"