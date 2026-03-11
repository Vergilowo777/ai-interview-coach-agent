def clean_question_lines(text: str) -> list[str]:
    """
    Convert raw LLM output into a cleaned list of questions.
    """
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    cleaned_questions = []

    for line in lines:
        # Remove common numbering formats like:
        # 1. xxx
        # 2) xxx
        # - xxx
        if line[0].isdigit():
            if ". " in line:
                line = line.split(". ", 1)[1].strip()
            elif ")" in line:
                line = line.split(")", 1)[1].strip()
        elif line.startswith("- "):
            line = line[2:].strip()

        cleaned_questions.append(line)

    return cleaned_questions