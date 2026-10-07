# ProofLens AI

Proof-Carrying Data Analyst for HackNex 2026 PS08.

## MVP
- CSV upload
- Dataset preview
- Missing/duplicate checks
- Supported analytical questions
- Executable Python proof
- Verification status
- Refusal for unsupported questions

## Run

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Linux/macOS:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Demo questions
- What is the total revenue?
- What is the average revenue?
- Which region had the highest revenue?
- Which product generated the most revenue?
- What is the average unit price?
- How many transactions are there?
- What was our profit? (should refuse)
