[README.md](https://github.com/user-attachments/files/31289594/README.md)
# 🤖 Agentic AI – Multi-Agent Business Assistant
## Intern POC

### Project Objective

Build an Agentic AI business assistant that accepts a natural-language
business question, selects the appropriate specialist agent, analyzes a
real business dataset, generates an insight, recommends an action and
produces a business report.

### Required Flow

```text
User Question
      ↓
Agent Router
      ↓
Support / Data / ML Agent
      ↓
Insight
      ↓
Action
      ↓
Report
```

### Agents

#### Support Agent
Handles dataset-information questions:
- Available columns
- Number of records
- Regions
- Categories
- Ship modes

#### Data Agent
Performs business analysis:
- Total sales
- Total profit
- Total orders
- Region performance
- Category performance
- Segment performance
- Product performance
- State/City performance

#### ML Agent
Performs a simple monthly sales forecast using Linear Regression.

### Dataset

`data/Superstore.xlsx`

Sheet:
`Superstore_Data`

### Project Structure

```text
Agentic_AI_Intern_POC/
│
├── app.py
├── requirements.txt
├── run.bat
├── .env.example
├── README.md
│
├── agents/
│   ├── support_agent.py
│   ├── data_agent.py
│   └── ml_agent.py
│
├── core/
│   ├── router.py
│   ├── workflow.py
│   └── report_generator.py
│
├── utils/
│   ├── data_loader.py
│   └── metrics.py
│
├── config/
│   └── settings.py
│
├── data/
│   └── Superstore.xlsx
│
└── reports/
```

### Installation

Open the project folder in VS Code.

Create/activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install packages:

```powershell
pip install -r requirements.txt
```

Run:

```powershell
streamlit run app.py
```

### Sample Questions

```text
Which region has the highest sales?
Which category has the highest profit?
Which segment is most profitable?
What is the total sales and total profit?
How many orders are in the dataset?
What columns are available?
Predict next month's sales
```

### POC Demonstration

For the internship demonstration, show this sequence:

1. Open the Streamlit application.
2. Ask a normal business question.
3. Show the Router selecting the Data Agent.
4. Show the dataset calculation.
5. Display the Insight.
6. Display the Recommended Action.
7. Display the final Report.
8. Ask a forecasting question and show the ML Agent.

### Important

This is an internship POC, so the architecture is separated into
agents, routing, workflow, data loading, metrics and report generation.
The ML forecast is intentionally simple and should be described as a
demonstration model rather than a production forecasting system.
