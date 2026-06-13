import requests


def generate_summary(text, language):

    prompt = f"""
Respond ONLY in {language}.

Create a short summary in 5 bullet points.

DOCUMENT:
{text[:3000]}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def ask_question(document_text, question, language):

    prompt = f"""
Respond ONLY in {language}.

Use the document below to answer the question.

DOCUMENT:
{document_text[:3000]}

QUESTION:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]