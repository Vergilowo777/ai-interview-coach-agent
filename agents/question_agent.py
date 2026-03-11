from config import client, MODEL_NAME
from utils.text_parser import clean_question_lines


def generate_questions(job_description: str) -> list[str]:
    """
    Generate 5 interview questions based on a job description.
    """
    prompt = f"""
You are an interview coach.

Based on the following job description, generate exactly 5 interview questions.
The questions should be relevant to the role and suitable for a mock interview.

Job Description:
{job_description}

Requirements:
- Return exactly 5 questions
- Each question should be on a new line
- Do not include explanations
- Do not include headings
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a professional interview coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    questions_text = response.choices[0].message.content.strip()
    questions = clean_question_lines(questions_text)

    return questions[:5]