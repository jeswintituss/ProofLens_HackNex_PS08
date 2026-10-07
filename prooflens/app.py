import streamlit as st
import pandas as pd
from agent.code_generator import generate_code
from execution.runner import execute_code
from validation.data_quality import inspect_dataframe

st.set_page_config(page_title="ProofLens AI", page_icon="🔍", layout="wide")
st.title("🔍 ProofLens AI")
st.caption("Proof-Carrying Data Analyst — every numerical answer comes with executable evidence.")

if "df" not in st.session_state:
    st.session_state.df = None

with st.sidebar:
    st.header("📁 Data")
    uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded:
        try:
            st.session_state.df = pd.read_csv(uploaded)
            st.success(f"Loaded: {uploaded.name}")
        except Exception as e:
            st.error(f"Could not read CSV: {e}")
    st.divider()
    st.caption("HackNex 2026 • PS08")

df = st.session_state.df

if df is None:
    st.info("Upload a CSV file from the sidebar to begin.")
    st.markdown("""
### What this prototype does
1. Inspects the dataset.
2. Checks common data-quality problems.
3. Converts supported questions into executable Python.
4. Runs the calculation.
5. Shows the answer and proof.
6. Refuses unsupported questions instead of inventing an answer.
""")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Rows", len(df))
c2.metric("Columns", len(df.columns))
c3.metric("Missing cells", int(df.isna().sum().sum()))
c4.metric("Duplicate rows", int(df.duplicated().sum()))

with st.expander("Preview data"):
    st.dataframe(df.head(30), use_container_width=True)

with st.expander("Data quality report", expanded=True):
    for item in inspect_dataframe(df):
        if item["severity"] == "warning":
            st.warning(item["message"])
        else:
            st.info(item["message"])

st.divider()
st.subheader("Ask your data")
question = st.text_input("Question", placeholder="Example: What is the total revenue?")

if st.button("🔍 Analyze & Verify", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Enter a question first.")
    else:
        code, explanation = generate_code(question, df)
        if code is None:
            st.error("⚠ CANNOT DETERMINE")
            st.write(explanation)
        else:
            st.subheader("💻 Executable Proof")
            st.code(code, language="python")
            result = execute_code(code, df)
            if result["success"]:
                st.success("✓ VERIFIED — code executed successfully")
                st.subheader("Answer")
                st.markdown(f"**{result['output'].strip()}**")
                st.subheader("Execution Evidence")
                st.code(result["output"].strip() or "(no printed output)")
                st.caption(explanation)
            else:
                st.error("❌ VERIFICATION FAILED")
                st.write(result["error"])

st.divider()
st.caption("If the system cannot support an answer reliably, it refuses rather than hallucinating.")
