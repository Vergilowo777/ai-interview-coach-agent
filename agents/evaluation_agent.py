from config import client, MODEL_NAME


def evaluate_answer(question: str, answer: str) -> str:
    """
    Evaluate the user's answer and return scoring feedback.
    """
    prompt = f"""
You are an interview evaluator.

Please evaluate the following interview answer based on these 4 dimensions:
1. Clarity
2. Relevance
3. Technical Depth
4. Product Thinking

Question:
{question}

Answer:
{answer}

Requirements:
- Give each dimension a score out of 10
- Briefly explain each score
- At the end, provide an overall summary
- Keep the response clear and structured
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a professional interview evaluator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()