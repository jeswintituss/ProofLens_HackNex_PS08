# ProofLens AI

## Proof-Carrying Data Analyst — HackNex 2026 PS08

ProofLens AI is an AI-assisted data analysis system designed to make numerical answers **verifiable and evidence-backed**.

Instead of simply returning a number, ProofLens follows a verification pipeline:

**User Question → Data Understanding → Data Quality Checks → Analysis Code → Code Execution → Verification → Answer + Executable Proof**

If the available data does not support an answer reliably, the system **refuses to guess** and explains why.

---

## 1. What the Project Does

Traditional AI data analysis systems can produce useful answers, but users may not know how the number was calculated or whether the underlying data actually supports the answer.

ProofLens addresses this by making every supported numerical answer **proof-carrying**.

For a user question such as:

> What is the total revenue?

ProofLens:

1. Reads the uploaded dataset.
2. Analyzes the user's natural-language question.
3. Identifies the relevant column(s).
4. Checks basic data quality.
5. Generates executable Python analysis code.
6. Executes the code against the uploaded dataset.
7. Captures the computed result.
8. Displays the answer together with the code used to reproduce it.
9. Shows whether execution was successful.

For questions that cannot be supported by the available data, ProofLens does not invent an answer.

For example:

> What was our profit?

If the dataset contains revenue and sales information but no verified profit information, ProofLens returns a refusal instead of estimating or hallucinating a profit value.

### Core idea

> **Don't just trust the AI. Verify the answer.**

Every numerical answer should have an executable path back to the data.

---

## 2. Key Features

### Proof-Carrying Answers

Numerical answers are accompanied by executable Python code showing how the result was calculated.

### Data Quality Checks

The system checks the uploaded dataset for basic issues including:

* Number of rows
* Number of columns
* Missing cells
* Duplicate rows

### Evidence-Aware Refusal

When the available data does not contain enough information to answer a question reliably, the system refuses instead of guessing.

### Natural-Language Questions

Users can ask questions in normal language rather than writing Python or SQL.

Examples:

```text
What is the total revenue?
```

```text
Which region had the highest revenue?
```

```text
What is the average unit price?
```

### Reproducible Computation

The final numerical result comes from executing generated analysis code against the actual dataset.

---

# 3. System Architecture

```text
                    ┌──────────────────┐
                    │    User Question │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Question Analyzer│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Data Understanding│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Data Quality Check│
                    │ Missing / Duplicate│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Code Generator  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Python Execution │
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    ▼                   ▼
             ┌──────────────┐   ┌──────────────┐
             │ Verification │   │    Refusal   │
             └──────┬───────┘   └──────────────┘
                    │
                    ▼
             ┌──────────────┐
             │ Answer + Code│
             │ + Evidence   │
             └──────────────┘
```

The important design principle is that the AI does not directly become the source of truth for numerical calculations.

The generated program performs the actual calculation.

---

# 4. Technologies, Libraries and Models

## Programming Language

### Python

Python is used for:

* Data processing
* Analysis
* Code execution
* Validation
* Application logic

## Libraries

### Streamlit

Used to build the interactive web interface.

### pandas

Used for:

* Reading CSV files
* Inspecting datasets
* Performing calculations
* Grouping and aggregation
* Detecting missing values and duplicates

### NumPy

Used as a numerical computing dependency.

### pytest

Used for automated testing of the project.

---

## AI / Model Layer

The current hackathon MVP uses a **rule-based analytical code generator** so that the core proof-carrying workflow is deterministic and easy to demonstrate.

The architecture is intentionally designed so that an LLM can later be placed in the question-understanding and code-generation layer.

The important separation is:

```text
AI / Question Understanding
          ↓
Analysis Code
          ↓
Deterministic Python Execution
          ↓
Verified Numerical Result
```

This prevents the language model itself from being treated as the final numerical calculator.

### Current MVP

The current implementation supports common analytical questions through a deterministic code-generation layer, including:

* Total revenue
* Average revenue
* Average unit price
* Number of transactions
* Highest-revenue region
* Highest-revenue product
* Explicit refusal for unsupported profit questions
* Explicit refusal when required information is unavailable

---

# 5. Project Structure

```text
ProofLens/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sales.csv
│
├── agent/
│   ├── __init__.py
│   └── code_generator.py
│
├── validation/
│   ├── __init__.py
│   └── data_quality.py
│
├── execution/
│   ├── __init__.py
│   └── runner.py
│
└── tests/
    └── test_basic.py
```

### Important files

| File                         | Purpose                                         |
| ---------------------------- | ----------------------------------------------- |
| `app.py`                     | Main Streamlit application                      |
| `agent/code_generator.py`    | Converts supported questions into analysis code |
| `validation/data_quality.py` | Performs dataset quality checks                 |
| `execution/runner.py`        | Executes generated analysis code                |
| `data/sales.csv`             | Demonstration dataset                           |
| `tests/test_basic.py`        | Basic automated tests                           |
| `requirements.txt`           | Python dependencies                             |

---

# 6. Installation

## Requirements

Recommended:

* Python 3.10+
* pip
* Git

Clone the repository:

```bash
git clone <YOUR_PUBLIC_GITHUB_REPOSITORY_URL>
cd ProofLens
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

The required libraries are listed in `requirements.txt`.

---

# 7. Configuration

The current MVP does not require API keys or external model credentials.

The application works with the included demonstration CSV dataset.

The default demonstration dataset is:

```text
data/sales.csv
```

Users can also upload their own compatible CSV file through the Streamlit interface.

---

# 8. Running the System

Start the application with:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, normally similar to:

```text
http://localhost:8501
```

Open that URL in a browser.

---

# 9. How to Use the System

## Step 1 — Upload a Dataset

Use the CSV uploader in the sidebar.

The application will load the dataset and display:

* Number of rows
* Number of columns
* Missing cells
* Duplicate rows
* Data preview

---

## Step 2 — Ask a Question

Enter a natural-language analytical question.

For example:

```text
What is the total revenue?
```

Then click **Analyze**.

---

## Step 3 — Inspect the Generated Proof

ProofLens displays the generated Python code used for the calculation.

For example, the generated analysis performs an aggregation over the relevant revenue field.

The important point is that the displayed answer is backed by code that can be executed against the dataset.

---

## Step 4 — Verify the Result

The generated code is executed against the uploaded DataFrame.

The interface reports whether execution succeeded.

A successful result means that the displayed numerical result was obtained through execution rather than being merely generated as text.

---

# 10. Reproducing the Demonstrated Results

The repository contains a sample dataset:

```text
data/sales.csv
```

After starting the application:

```bash
streamlit run app.py
```

use the following questions.

## Test 1 — Total Revenue

Question:

```text
What is the total revenue?
```

Expected result:

```text
615000
```

The result is calculated from the `Revenue` column in `data/sales.csv`.

---

## Test 2 — Average Revenue

Question:

```text
What is the average revenue?
```

The application calculates the arithmetic mean of the `Revenue` column.

---

## Test 3 — Highest-Revenue Region

Question:

```text
Which region had the highest revenue?
```

The application groups the sales data by region, calculates revenue for each region, and returns the region with the highest value.

---

## Test 4 — Highest-Revenue Product

Question:

```text
Which product generated the most revenue?
```

The application groups the data by product and identifies the product with the highest total revenue.

---

## Test 5 — Average Unit Price

Question:

```text
What is the average unit price?
```

The application calculates the mean of the `Unit Price` field.

---

## Test 6 — Transaction Count

Question:

```text
How many transactions are there?
```

The application returns the number of transactions represented by the dataset.

---

## Test 7 — Evidence-Aware Refusal

Question:

```text
What was our profit?
```

Expected behavior:

```text
REFUSED
```

The system should not invent a profit value when the dataset does not contain verified profit information.

This demonstrates one of ProofLens's core principles:

> **When the evidence is insufficient, the system refuses instead of guessing.**

---

# 11. Running Automated Tests

With the virtual environment activated:

```bash
pytest
```

The tests verify core functionality of the analytical pipeline.

---

# 12. Example Workflow

A typical ProofLens interaction looks like this:

```text
User:
"What is the total revenue?"

        ↓

ProofLens identifies:
Revenue → numerical field

        ↓

Data quality checks

        ↓

Analysis code generated

        ↓

Python code executed

        ↓

Execution successful

        ↓

Result:
615000

        ↓

User receives:
• Numerical answer
• Generated executable code
• Execution status
• Dataset evidence
```

For unsupported questions:

```text
User:
"What was our profit?"

        ↓

Required verified profit information unavailable

        ↓

ProofLens refuses

        ↓

No fabricated numerical answer
```

---

# 13. Why This Is Different

The key idea is not simply using AI to analyze data.

ProofLens combines:

1. Natural-language analytical interaction
2. Data-quality awareness
3. Executable generated analysis
4. Deterministic computation
5. Evidence-backed answers
6. Evidence-aware refusal

The LLM/AI layer can interpret what the user wants, but the numerical calculation is performed by executable code against the actual dataset.

This creates a clear separation:

```text
AI → Understand and propose
Python → Calculate
Verification → Check and expose the proof
```

---

# 14. Limitations of the Current MVP

The current hackathon MVP intentionally focuses on a small, demonstrable set of analytical operations.

Current limitations include:

* Primarily CSV input
* Limited supported natural-language question patterns
* Basic data-quality checks
* Rule-based code generation in the current prototype
* Local code execution rather than a production-grade isolated execution service
* No full semantic understanding of every possible dataset schema

These limitations can be addressed in future versions.

---

# 15. Future Improvements

Possible extensions include:

* LLM-based natural-language question decomposition
* Automatic schema understanding
* SQL generation
* Support for multiple tables
* Unit consistency checking
* Date ambiguity detection
* Contradictory-data detection
* More advanced missing-data reasoning
* Stronger execution sandboxing
* Automatic test-case generation
* Evidence graphs linking answers to source rows
* Confidence/evidence scoring
* Support for Excel and database sources

---

# 16. Reproducibility Principle

ProofLens is designed around a simple principle:

> **If a numerical answer cannot be reproduced from the available evidence, the system should not confidently present it as fact.**

The repository therefore contains the application source code, validation logic, execution logic, demonstration dataset, tests, and instructions required to reproduce the demonstrated workflow.

---

# 17. Hackathon Demo

For the HackNex PS08 demonstration, the recommended sequence is:

### Demo 1 — Normal Question

```text
What is the total revenue?
```

Show:

**Answer → Generated Code → Successful Execution**

### Demo 2 — Analytical Question

```text
Which region had the highest revenue?
```

Show that the system can translate a natural-language question into an executable analysis.

### Demo 3 — Data Quality

Show the dataset statistics:

* Rows
* Columns
* Missing values
* Duplicate rows

### Demo 4 — Refusal

Ask:

```text
What was our profit?
```

Show that ProofLens refuses to fabricate a result because the required evidence is unavailable.

This final demonstration highlights the project's main differentiator:

> **ProofLens doesn't just try to answer. It checks whether the data can actually support the answer.**
