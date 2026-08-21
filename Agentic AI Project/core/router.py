def route_question(question: str) -> str:
    """Route the user question to the most suitable specialist agent."""
    q = question.lower()

    ml_keywords = [
        "predict", "prediction", "forecast", "future",
        "next month", "next year", "estimate"
    ]

    support_keywords = [
        "column", "columns", "dataset", "records", "rows",
        "available", "what data", "ship mode"
    ]

    if any(word in q for word in ml_keywords):
        return "ML Agent"

    if any(word in q for word in support_keywords):
        return "Support Agent"

    return "Data Agent"
