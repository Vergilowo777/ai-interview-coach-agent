from config import client, MODEL_NAME


def generate_feedback(question: str, answer: str) -> str:
    """
    Generate actionable feedback for improving the user's answer.
    """
    prompt = f"""
You are an interview coach.

The user answered the following interview question.

Question:
{question}

Answer:
{answer}

Please provide feedback to help the user improve.

Requirements:
- Point out 2 to 3 weaknesses
- Suggest 2 to 3 specific improvements
- If possible, recommend a better answer structure
- Be constructive and easy to understand
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful interview coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6
    )

    return response.choices[0].message.content.strip()