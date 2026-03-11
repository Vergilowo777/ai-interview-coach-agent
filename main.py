from agents.question_agent import generate_questions
from agents.evaluation_agent import evaluate_answer
from agents.feedback_agent import generate_feedback


def main() -> None:
    print("=== AI Interview Coach Agent (Modular Version) ===\n")

    job_description = input("Please paste the job description:\n").strip()
    if not job_description:
        print("Job description cannot be empty.")
        return

    print("\nGenerating interview questions...\n")
    questions = generate_questions(job_description)

    if not questions:
        print("No questions were generated.")
        return

    print("Generated Questions:")
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")

    print("\nPlease choose one question number to answer.")
    selected = input("Enter question number (1-5): ").strip()

    if not selected.isdigit():
        print("Invalid input. Please enter a number.")
        return

    selected_index = int(selected) - 1
    if selected_index < 0 or selected_index >= len(questions):
        print("Question number out of range.")
        return

    selected_question = questions[selected_index]

    print(f"\nSelected Question:\n{selected_question}\n")
    answer = input("Please type your answer:\n").strip()

    if not answer:
        print("Answer cannot be empty.")
        return

    print("\nEvaluating your answer...\n")
    evaluation = evaluate_answer(selected_question, answer)

    print("=== Evaluation Result ===")
    print(evaluation)

    print("\nGenerating improvement feedback...\n")
    feedback = generate_feedback(selected_question, answer)

    print("=== Improvement Feedback ===")
    print(feedback)


if __name__ == "__main__":
    main()