from crewai import Crew, Task, LLM
import os
import time

from agents.researcher import get_researcher
from agents.writer import get_writer
from agents.editor import get_editor

from dotenv import load_dotenv
load_dotenv()


def run_crew(query: str):
    print(f"[INFO] New Query Received: {query}")

    print("[INFO] Initializing Groq LLM...")
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.1
    )

    print("[INFO] Initializing agents...")
    researcher = get_researcher(llm)
    writer = get_writer(llm)
    editor = get_editor(llm)

    print("[INFO] Creating tasks...")

    research_task = Task(
        description=(
            f"Query: {query}\n"
            "Retrieve relevant chunks from the vector database only. "
            "No prior knowledge. If nothing relevant found, return: "
            "'I don't know based on the provided documents.'"
        ),
        expected_output="Raw relevant facts from vector DB only.",
        agent=researcher,
    )

    writing_task = Task(
        description=(
            "Paraphrase the researcher's output into a concise, structured answer. "
            "Do not add, infer, or invent any information."
        ),
        expected_output="Concise answer strictly based on retrieved facts.",
        agent=writer,
        context=[research_task]
    )

    editing_task = Task(
        description=(
            "Remove anything not found in the research. "
            "Edit using the context of research andwriting task and don't add them both"
            "Remove duplicates strictly"
            "If no valid grounded content exists, output only: "
            "'I don't know based on the provided documents.'"
        ),
        expected_output="Final verified answer grounded strictly in research.",
        agent=editor,
        context=[research_task, writing_task]
    )

    print("[INFO] Assembling crew...")
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        verbose=True
    )

    print("[INFO] Starting crew execution...\n")

    try:
        exec_start = time.time()
        result = crew.kickoff()
        exec_end = time.time()
        print(f"[INFO] Crew execution completed in {exec_end - exec_start:.2f}s")

    except Exception as e:
        print(f"[ERROR] Crew execution failed: {e}")
        return "Execution failed."

    return result.raw