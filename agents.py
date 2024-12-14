from langchain.chains.llm import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

import os

from knowledge_base import create_embeddings
from prompts import (
    WORLD_BUILDER_TEMPLATE,
    CHARACTER_TEMPLATE,
    PLOTTER_TEMPLATE,
    WRITER_TEMPLATE,
)

from utils import create_chat_openai_instance


class Agent:
    def __init__(self, name: str, knowledge_base_directory: str, task: str):
        self.name = name
        self.db = create_embeddings(knowledge_base_directory)
        self.task = task
        self.llm = create_chat_openai_instance(tuneai_api_key=os.environ["TUNE_API_KEY"])
        # self.llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo-16k")

    def query_knowledge_base(self, query: str, top_k: int = 5):
        """
        Queries the agent's knowledge base using RAG.

        Args:
            query (str): The query string.
            top_k (int): The number of top results to retrieve.

        Returns:
            list: A list of relevant documents (or text chunks) from the knowledge base.
        """
        docs_and_scores = self.db.similarity_search_with_score(query, k=top_k)

        results = []
        for doc, score in docs_and_scores:
            results.append({"score": score, "content": doc.page_content})
        return results

    def generate_response(self, user_input: str, context: str) -> str:
        """
        Generates a response to the user input using the agent's knowledge base.

        Args:
            user_input (str): The user's input.
            context (str): Additional context from other agents or interactions.

        Returns:
            str: The agent's response.
        """

        # creating a knowledge base query using user_input and context
        rag_query = f"Relevant information for task '{self.task}': {context}\nUser input: {user_input}"

        relevant_docs = self.query_knowledge_base(rag_query)

        # combine retrieved information with user input and context for the llm prompt
        augmented_input = f"Task: {self.task}\nContext from other agents: {context}\n"
        if relevant_docs:
            augmented_input += "Relevant knowledge:\n"
            for doc in relevant_docs:
                augmented_input += f"- {doc['content']}\n"
        augmented_input += f"\nUser input: {user_input}\n"

        if self.name == "Worldbuilder":
            template = WORLD_BUILDER_TEMPLATE
        elif self.name == "Plotter":
            template = PLOTTER_TEMPLATE
        elif self.name == "Character":
            template = CHARACTER_TEMPLATE
        elif self.name == "Chapter Writer":
            template = WRITER_TEMPLATE

        # generating response
        human_message_prompt = HumanMessagePromptTemplate.from_template(template)
        chat_prompt = ChatPromptTemplate.from_messages([human_message_prompt])
        chain = LLMChain(llm=self.llm, prompt=chat_prompt)
        response = chain.run(
            {"agent_name": self.name, "augmented_input": augmented_input}
        )

        return response

class WorldbuilderAgent(Agent):
    def __init__(self):
        super().__init__("Worldbuilder", "data/", "world building")

class PlotterAgent(Agent):
    def __init__(self):
        super().__init__("Plotter", "data/", "plot development")

class CharacterAgent(Agent):
    def __init__(self):
        super().__init__("Character", "data/", "character creation and development")

class ChapterWriterAgent(Agent):
    def __init__(self):
        super().__init__("Chapter Writer", "data/", "writing novel chapters")
