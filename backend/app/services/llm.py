from dotenv import load_dotenv
load_dotenv()


def generate_answer(query, chunks):
    context = "\n\n".join([c["text"] for c in chunks])

    prompt = f"""
You are a document QA assistant.
Answer ONLY using the provided context.
If answer is not in context, say: Not found in documents.

Context:
{context}

Question:
{query}

Answer:
"""
    return prompt
