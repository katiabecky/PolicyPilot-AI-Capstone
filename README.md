# PolicyPilot AI Capstone

PolicyPilot AI is a solo MSSE capstone project that builds a retrieval-augmented policy assistant for internal company documents.

## Project Overview
PolicyPilot AI allows users to ask policy-related questions in natural language and receive grounded answers based on an approved internal policy corpus. The system returns supporting source metadata and excerpts, and refuses unsupported or out-of-scope questions when the available documents do not provide enough evidence.

## Problem Statement
Employees often need quick answers to policy questions, but long policy documents are difficult to search manually. A lightweight retrieval-augmented assistant can improve access to policy knowledge while keeping responses grounded in the actual source material.

## Solution Summary
PolicyPilot AI:
- ingests internal company policy documents
- breaks them into structured chunks with metadata
- stores them in a Chroma vector database
- retrieves relevant chunks for a user question
- displays grounded answers with source support
- refuses unsupported questions when evidence is insufficient

## MVP Features
The current MVP supports:
- policy question answering through a Streamlit interface
- retrieval of relevant policy chunks from a curated corpus
- display of source metadata
- expandable source excerpts for traceability
- refusal behavior for unsupported or out-of-scope questions

### Examples of validated in-scope questions
- How many vacation days do employees get?
- What are the password requirements?
- How do I submit an expense reimbursement?
- What should I do if I suspect harassment?

### Examples of validated unsupported questions
- What is the company stock price?
- Who is the CEO’s assistant?
- What is the office Wi-Fi password today?
- Can you tell me today’s Wi-Fi password?

## Project Structure
- `app/` — Streamlit application layer
- `data/` — policy documents and processed chunk data
- `scripts/` — ingestion, vector-store, retrieval, and Q&A scripts
- `tests/` — validation and test files
- `docs/` — capstone documentation and demo materials
- `.github/workflows/` — CI workflow files
- `chroma_db/` — local persistent Chroma vector store (local only; not intended for repository tracking)

## Tech Stack
- Python
- Streamlit
- ChromaDB
- Markdown policy corpus
- local retrieval pipeline / vector search

## Current Status
Completed:
- repository structure created
- policy corpus prepared
- cleaned chunk dataset generated
- Chroma vector database created
- retrieval pipeline implemented
- retrieval testing completed
- unsupported-question refusal logic added
- Streamlit MVP built and validated
- capstone draft documentation created
- agile task board prepared

Remaining final submission work:
- deploy the Streamlit app
- add the public deployment link
- record final presentation
- run final submission QA

## How to Run Locally

### 1. Activate the virtual environment
On Windows:
```bash
venv\Scripts\activate
