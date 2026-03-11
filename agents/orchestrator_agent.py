from agents.question_agent import generate_questions
from agents.evaluation_agent import evaluate_answer
from agents.feedback_agent import generate_feedback
from agents.followup_agent import generate_followup_question


class InterviewOrchestratorAgent:
    """
    Orchestrates the interview workflow by coordinating:
    - Question generation
    - Answer evaluation
    - Feedback generation
    - Follow-up question generation
    """

    def generate_interview_questions(self, job_description: str) -> list[str]:
        return generate_questions(job_description)

    def evaluate_user_answer(self, question: str, answer: str) -> str:
        return evaluate_answer(question, answer)

    def generate_improvement_feedback(self, question: str, answer: str) -> str:
        return generate_feedback(question, answer)

    def generate_followup(self, question: str, answer: str) -> str:
        return generate_followup_question(question, answer)

    def run_full_evaluation(self, question: str, answer: str) -> dict:
        """
        Run evaluation + feedback + follow-up together and return a structured result.
        """
        evaluation = self.evaluate_user_answer(question, answer)
        feedback = self.generate_improvement_feedback(question, answer)
        followup = self.generate_followup(question, answer)

        return {
            "evaluation": evaluation,
            "feedback": feedback,
            "followup": followup
        }