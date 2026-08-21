import streamlit as st
from core.router import route_question
from core.workflow import run_workflow
from utils.data_loader import load_data

st.set_page_config(
    page_title="Agentic AI Business Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Agentic AI – Multi-Agent Business Assistant")
st.caption("User Question → Router → Agent → Insight → Action → Report")

try:
    df = load_data()
except Exception as e:
    st.error(f"Dataset loading failed: {e}")
    st.stop()

with st.sidebar:
    st.header("📁 Dataset")
    st.success("Superstore.xlsx loaded")
    st.metric("Records", f"{len(df):,}")
    st.metric("Columns", len(df.columns))

    st.divider()
    st.header("🤖 Available Agents")
    st.write("• Support Agent")
    st.write("• Data Agent")
    st.write("• ML Agent")

    st.divider()
    st.header("📌 Workflow")
    st.write("1. User Question")
    st.write("2. Agent Router")
    st.write("3. Specialist Agent")
    st.write("4. Insight")
    st.write("5. Action")
    st.write("6. Report")

question = st.text_input(
    "Ask a business question",
    placeholder="Example: Which region has the highest profit?"
)

if st.button("🚀 Run Agent", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    result = run_workflow(question, df)

    st.subheader("🤖 Agent Decision")
    st.info(f"Selected Agent: **{result['agent']}**")

    st.subheader("💡 Insight")
    st.write(result["insight"])

    st.subheader("⚡ Recommended Action")
    st.write(result["action"])

    if result.get("table") is not None:
        st.subheader("📊 Supporting Data")
        st.dataframe(result["table"], use_container_width=True)

    if result.get("chart") is not None:
        st.subheader("📈 Visualization")
        st.line_chart(result["chart"])

    st.subheader("📝 Business Report")
    st.markdown(result["report"])

st.divider()
st.subheader("💬 Try These Questions")

examples = [
    "Which region has the highest sales?",
    "Which category has the highest profit?",
    "Which segment is most profitable?",
    "What is the total sales and total profit?",
    "How many orders are in the dataset?",
    "What columns are available?",
    "Predict next month's sales"
]

cols = st.columns(2)
for i, example in enumerate(examples):
    cols[i % 2].write(f"• {example}")
