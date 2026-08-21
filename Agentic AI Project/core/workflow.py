from agents.support_agent import SupportAgent
from agents.data_agent import DataAgent
from agents.ml_agent import MLAgent
from core.router import route_question
from core.report_generator import generate_report


def run_workflow(question, df):
    agent_name = route_question(question)

    if agent_name == "Support Agent":
        result = SupportAgent(df).run(question)
    elif agent_name == "ML Agent":
        result = MLAgent(df).run(question)
    else:
        result = DataAgent(df).run(question)

    report = generate_report(
        question=question,
        agent=agent_name,
        insight=result["insight"],
        action=result["action"]
    )

    result["agent"] = agent_name
    result["report"] = report
    return result