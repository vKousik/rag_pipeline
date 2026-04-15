from crewai import Agent
from tools.vectordb_tools import search_vector_db

def get_researcher(llm):
    return Agent(
        role="Researcher",
        goal="Retrieve only relevant facts from the vector database.",
        backstory=(
            "Use the vector DB tool ONCE only. "
            "Return the tool's output exactly as-is. "
            "Only say 'I don't know' if the tool returns NO_RELEVANT_CONTEXT."
        ),
        verbose=True,
        allow_delegation=False,
        tools=[search_vector_db],
        llm=llm
    )