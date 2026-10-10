# PolicyPilot AI — Design and Testing Document

## 1. Project Overview
PolicyPilot AI is a retrieval-augmented policy assistant designed to answer company policy questions using a curated set of internal policy documents. The goal of the project is to help users quickly find reliable, policy-backed answers without manually searching across multiple files.

The system is intended for policy-related questions such as vacation allowances, expense reimbursement, workplace conduct, remote work, and IT security requirements. It is not designed to answer unrelated, real-time, or confidential questions outside the current policy corpus.

## 2. Problem Statement
Company policy information is often distributed across multiple documents, making it time-consuming for users to locate accurate answers. Users may overlook relevant sections or misinterpret policy details when searching manually.

PolicyPilot AI addresses this problem by retrieving the most relevant policy excerpts from indexed documents and presenting a grounded answer with visible supporting sources.

## 3. Scope of the MVP
The MVP focuses on:
- answering policy questions from a fixed internal document set
- retrieving relevant chunks from a local Chroma vector store
- returning grounded answers with source references
- refusing unsupported or out-of-scope questions when evidence is weak

The MVP does not include:
- real-time company data lookup
- authentication or user roles
- policy document upload by end users
- advanced UI styling
- production-grade monitoring or analytics

## 4. System Architecture
PolicyPilot AI follows a simple retrieval-augmented architecture with the following components:

1. **Policy document corpus**
   - Internal policy documents are prepared and stored locally.

2. **Chunked policy data**
   - Documents are split into chunks and saved in structured form for retrieval.

3. **Vector store**
   - Chunks are indexed in a persistent Chroma database stored locally.

4. **Retrieval layer**
   - User queries are matched against the vector store to retrieve the most relevant chunks.

5. **Ranking and guardrail layer**
   - Retrieved chunks are evaluated using heuristic scoring rules.
   - Weak or unsupported matches are rejected.

6. **User interface**
   - A Streamlit web app allows the user to enter a question, view the answer, and inspect supporting sources.

## 5. Design and Architecture Decisions
### 5.1 Python
Python was selected because it supports rapid prototyping, has strong tooling for document processing and vector retrieval, and integrates well with Streamlit and ChromaDB.

### 5.2 Streamlit
Streamlit was chosen for the frontend because it allows quick development of a simple interactive web application without requiring a full frontend framework. This was appropriate for an MVP and capstone scope.

### 5.3 ChromaDB
ChromaDB was selected as the vector database because it is lightweight, easy to run locally, and suitable for experimentation with retrieval-based systems. A persistent local store was sufficient for this project stage.

### 5.4 Local-first architecture
The project was built to run locally in order to reduce deployment complexity during development, simplify testing, and keep infrastructure costs low.

### 5.5 Retrieval-first answer design
The system was designed to provide grounded answers only when the retrieved evidence is strong enough. This decision was made to reduce hallucination risk and make answer traceability visible to the user.

## 6. Software and Architectural Patterns Used
### 6.1 Retrieval-Augmented Generation style workflow
The project uses a retrieval-augmented workflow in which relevant document chunks are retrieved before presenting an answer. Even though the MVP answer generation is controlled and lightweight, the core interaction pattern is RAG-style because the answer is grounded in retrieved source text.

### 6.2 Separation of concerns
The project structure separates:
- app interface logic
- retrieval/testing scripts
- data files
- documentation

This makes the project easier to maintain and explain.

### 6.3 Defensive filtering / guardrails
The system uses refusal logic for out-of-scope questions. This is a defensive design pattern intended to improve trustworthiness by avoiding unsupported answers.

## 7. Data Preparation
The policy corpus was prepared from internal policy documents and transformed into chunked data for retrieval.

The retrieval setup includes:
- structured chunk metadata
- filename tracking
- section title tracking
- chunk ID tracking

This metadata improves transparency by allowing the app to display exactly which source sections support the answer. The chunked dataset used in testing contained 69 chunks.

## 8. Retrieval and Answer Flow
The user interaction flow is as follows:

1. The user enters a policy-related question.
2. The system queries the Chroma vector store.
3. The top matching chunks are retrieved.
4. Ranking heuristics prioritize stronger, more relevant matches.
5. If enough support exists, the system returns a grounded answer.
6. If support is weak or the question is out of scope, the system refuses to answer and prompts the user to ask about supported policy topics.
7. The system displays source filenames, section titles, chunk IDs, and expandable source excerpts.

## 9. Deployment Options and Cost Considerations
### 9.1 Local deployment
The simplest deployment option is local execution on a personal machine using Streamlit. This has effectively no hosting cost and is suitable for development and testing.

### 9.2 Cloud deployment
For a web-based capstone submission, cloud deployment is preferable because it provides a shareable link for reviewers. Suitable low-cost or free-tier options include platforms such as Streamlit Community Cloud, Render, or Railway.

### 9.3 Recommended option
For this capstone, a low-cost cloud deployment is recommended if required for submission, because it makes the application easy to access for grading while keeping infrastructure overhead low.

## 10. Testing Strategy
Testing was performed in stages to validate the system incrementally.

### 10.1 Setup validation
The `test_vector_setup.py` script was used to verify:
- chunk data loads correctly from JSON
- ChromaDB imports successfully
- the persistent database is reachable
- the expected collection exists
- the collection contains the expected records

### 10.2 Retrieval validation
The `retrieve_chunks.py` script was used to test whether relevant chunks were returned for representative policy questions.

### 10.3 CLI answer validation
The `answer_question.py` script was used to test:
- direct answer generation
- supporting source output
- refusal behavior for unsupported questions

### 10.4 Streamlit UI validation
The Streamlit app was tested to confirm:
- the interface loads correctly
- policy questions return grounded answers
- source metadata is shown
- source excerpts can be expanded
- unsupported questions are refused appropriately

## 11. Testing Performed and Results
### 11.1 Successful in-scope tests
The following representative questions returned correct policy-backed answers:
- How many vacation days do employees get?
- What are the password requirements?
- How do I submit an expense reimbursement?
- What should I do if I suspect harassment?

### 11.2 Out-of-scope refusal tests
The following questions were correctly refused:
- What is the company stock price?
- Who is the CEO’s assistant?
- What is the office Wi-Fi password today?
- Can you tell me today’s Wi-Fi password?

### 11.3 Retrieval quality observations
Early testing showed that some queries could retrieve related but not ideal chunks first. For example, a vacation-days question initially prioritized a carryover chunk above the annual allowance chunk. This was improved through heuristic refinement.

### 11.4 Guardrail observations
Early versions of the CLI sometimes returned weak matches for unsupported questions. This was improved by adding out-of-scope detection and refusal logic.

## 12. Automated and Script-Based Tests Used
The project includes script-based testing through:
- `scripts/test_vector_setup.py`
- `scripts/retrieve_chunks.py`
- `scripts/answer_question.py`

These tests were used because they are lightweight, practical for an MVP, and effective for validating the retrieval pipeline before and after UI integration.

## 13. Limitations
Current limitations include:
- limited document corpus
- no live company data access
- no user authentication
- no document upload workflow
- simple heuristic ranking rather than advanced semantic re-ranking
- MVP-level interface styling

## 14. Future Improvements
Potential next improvements include:
- stronger ranking and confidence scoring
- richer source citation formatting
- broader policy corpus coverage
- admin workflow for updating documents
- improved UI/UX design
- formal automated test suite
- cloud deployment hardening

## 15. Conclusion
PolicyPilot AI demonstrates a functional policy-question answering MVP built around retrieval, source transparency, and refusal safeguards. The project shows how a lightweight RAG-style system can provide grounded answers from internal documents while reducing the risk of unsupported responses.
