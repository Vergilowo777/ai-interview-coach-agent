from config import client, MODEL_NAME


def generate_followup_question(question: str, answer: str) -> str:
    """
    Generate one follow-up interview question based on the user's answer.
    """
    prompt = f"""
You are an interview coach.

The user answered the following interview question.

Original Question:
{question}

User Answer:
{answer}

Your task:
Generate exactly one follow-up interview question that digs deeper into the user's answer.

Requirements:
- Ask only one follow-up question
- Make it relevant to the user's answer
- Make it sound like a realistic interview follow-up
- Do not include explanations
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a professional interviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()