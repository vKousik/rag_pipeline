from crewai import Agent

def get_writer(llm):
    return Agent(
        role="Writer",
        goal="Paraphrase and format the researcher's output only.",
        backstory="Rephrase and structure given facts. No additions, no expansions, no examples beyond what was retrieved.",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )