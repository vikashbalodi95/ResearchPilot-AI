from app.tools.retrieval_tool import RetrievalTool
from app.tools.document_tool import DocumentTool
from app.tools.tool_selector import ToolSelector
from app.services.groq_service import GroqService


class ResearchAgent:

    def __init__(self):
        self.retrieval_tool = RetrievalTool()
        self.document_tool = DocumentTool()
        self.tool_selector = ToolSelector()
        self.groq_service = GroqService()

    async def analyze_question(self, question: str):
        """
        Step 1:
        Understand what the user is asking.
        """

        analysis_prompt = f"""
Analyze the following research question.

Identify the main information the user is asking for.

Question:
{question}
"""

        return await self.groq_service.generate_response(
            prompt=analysis_prompt
        )

    async def retrieve_information(
        self,
        question: str,
        top_k: int = 3
    ):
        """
        Retrieve relevant document chunks using RetrievalTool.
        """

        documents = self.retrieval_tool.retrieve(
            query=question,
            top_k=top_k
        )

        return "\n\n".join(documents)

    async def get_document_information(
        self,
        file_path: str
    ):
        """
        Get document information using DocumentTool.
        """

        return self.document_tool.get_document_info(
            file_path=file_path
        )

    async def analyze_information(
        self,
        question: str,
        context: str
    ):
        """
        Analyze the retrieved information.
        """

        analysis_prompt = f"""
Analyze the following research information
and extract the findings relevant to the question.

Question:
{question}

Research Context:
{context}
"""

        return await self.groq_service.generate_response(
            prompt=analysis_prompt
        )

    async def generate_final_answer(
        self,
        question: str,
        findings: str
    ):
        """
        Generate the final answer.
        """

        final_prompt = f"""
Answer the user's research question using the
analyzed findings below.

Question:
{question}

Analyzed Findings:
{findings}
"""

        return await self.groq_service.generate_response(
            prompt=final_prompt
        )

    async def research(
        self,
        question: str,
        file_path: str = None
    ):
        """
        Execute the research workflow with tool selection.
        """

        # Step 1: Analyze question
        analysis = await self.analyze_question(question)

        # Step 2: Select tool
        selected_tool = self.tool_selector.select_tool(question)

        # Step 3: Execute selected tool
        if selected_tool == "document":

            if not file_path:
                return "A document file path is required for this request."

            document_info = await self.get_document_information(
                file_path
            )

            return document_info

        # Retrieval tool
        context = await self.retrieve_information(
            question
        )

        # Step 4: Analyze retrieved information
        findings = await self.analyze_information(
            question,
            context
        )

        # Step 5: Generate final answer
        answer = await self.generate_final_answer(
            question,
            findings
        )

        return answer