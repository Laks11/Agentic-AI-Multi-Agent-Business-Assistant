def generate_report(question, agent, insight, action):
    return f"""
### Business Analysis Report

**User Question:**  
{question}

**Selected Agent:**  
{agent}

### Insight
{insight}

### Recommended Action
{action}

### Conclusion
The Agentic AI workflow routed the question to the appropriate specialist,
analyzed the business dataset, generated an insight, and converted the
insight into an actionable recommendation.
"""
