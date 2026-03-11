import streamlit as st

from agents.orchestrator_agent import InterviewOrchestratorAgent


st.set_page_config(
    page_title="AI Interview Coach Agent",
    page_icon="🤖",
    layout="wide"
)

orchestrator = InterviewOrchestratorAgent()

st.title("🤖 AI Interview Coach Agent")
st.write("Paste a job description, generate interview questions, answer one question, and receive AI evaluation, feedback, and a follow-up question.")

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = []

if "selected_question" not in st.session_state:
    st.session_state.selected_question = ""

if "evaluation_result" not in st.session_state:
    st.session_state.evaluation_result = ""

if "feedback_result" not in st.session_state:
    st.session_state.feedback_result = ""

if "followup_result" not in st.session_state:
    st.session_state.followup_result = ""

# Step 1: Input Job Description
st.subheader("1. Paste Job Description")
job_description = st.text_area(
    "Job Description",
    height=180,
    placeholder="Paste the job description here..."
)

# Step 2: Generate Questions
if st.button("Generate Interview Questions"):
    if not job_description.strip():
        st.warning("Please enter a job description first.")
    else:
        with st.spinner("Generating interview questions..."):
            questions = orchestrator.generate_interview_questions(job_description)
            st.session_state.questions = questions
            st.session_state.selected_question = ""
            st.session_state.evaluation_result = ""
            st.session_state.feedback_result = ""
            st.session_state.followup_result = ""

# Step 3: Show Questions
if st.session_state.questions:
    st.subheader("2. Generated Questions")

    question_options = {
        f"Question {i + 1}: {q}": q
        for i, q in enumerate(st.session_state.questions)
    }

    selected_label = st.radio(
        "Choose one question to answer:",
        list(question_options.keys())
    )

    st.session_state.selected_question = question_options[selected_label]

# Step 4: Input Answer
answer = ""
if st.session_state.selected_question:
    st.subheader("3. Your Answer")
    st.write(f"**Selected Question:** {st.session_state.selected_question}")

    answer = st.text_area(
        "Type your answer here:",
        height=180,
        placeholder="Enter your interview answer..."
    )

# Step 5: Evaluate Answer
if st.session_state.selected_question and st.button("Evaluate My Answer"):
    if not answer.strip():
        st.warning("Please type your answer first.")
    else:
        with st.spinner("Evaluating your answer..."):
            result = orchestrator.run_full_evaluation(
                st.session_state.selected_question,
                answer
            )

            st.session_state.evaluation_result = result["evaluation"]
            st.session_state.feedback_result = result["feedback"]
            st.session_state.followup_result = result["followup"]

# Step 6: Display Results
if st.session_state.evaluation_result:
    st.subheader("4. Evaluation Result")
    st.write(st.session_state.evaluation_result)

if st.session_state.feedback_result:
    st.subheader("5. Improvement Feedback")
    st.write(st.session_state.feedback_result)

if st.session_state.followup_result:
    st.subheader("6. Follow-up Question")
    st.write(st.session_state.followup_result)