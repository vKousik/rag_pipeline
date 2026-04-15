from crew.crew_setup import run_crew

SYSTEM_PROMPT = """
Strict RAG:
- Only use retrieved content
- No hallucination
- If not found → "I don't know based on the provided documents."
"""

def get_answer(query: str):
    return run_crew(query)