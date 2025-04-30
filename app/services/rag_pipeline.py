import os
import httpx
from app.services.vector_store import query_similar_documents

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")
GROQ_URL = 'https://api.groq.com/openai/v1/chat/completions'

def generate_answer(question):
    contexts = query_similar_documents(question)
    context_block = '\n\n'.join(contexts)

    prompt = f"""Use the context below to answer the question

    context:
    {context_block}

Question: {question}
Answer:"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = httpx.post(GROQ_URL, json=payload, headers=headers,timeout=15)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
