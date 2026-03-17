def analyze_prompt(prompt):
    feedback = []

    if len(prompt.strip()) < 20:
        feedback.append("Prompt is too short. Add more context.")

    action_words = ["write", "generate", "explain", "summarize", "create", "list", "compare"]
    if not any(word in prompt.lower() for word in action_words):
        feedback.append("Prompt may be missing a clear action word like write, explain, summarize, or generate.")

    if "for" not in prompt.lower() and "about" not in prompt.lower():
        feedback.append("Prompt may be missing context. Try mentioning what the task is about or who it is for.")

    if "example" not in prompt.lower():
        feedback.append("Consider asking for an example to improve the response quality.")

    if not feedback:
        feedback.append("Good prompt. It looks reasonably clear.")

    return feedback