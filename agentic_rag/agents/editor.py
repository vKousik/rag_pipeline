from crewai import Agent

def get_editor(llm):
    return Agent(
        role="Editor",
        goal="Remove anything not grounded in the research.",
        backstory="You strip any content not directly supported by the researcher's output. No additions, no inference.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )