# PolicyPilot AI - Retrieval Evaluation

## Purpose
This file records retrieval-quality checks for the Sprint 2 semantic search layer and early Sprint 3 Q&A behavior.

## In-scope queries

### 1. How many vacation days do employees get?
- Expected topic: Vacation allowance
- Top 1 relevant: Partial
- Top 3 relevant: Yes
- Notes: The correct answer appears in Result 2. Carryover ranked above annual allowance.

### 2. What are the password requirements?
- Expected topic: Password policy
- Top 1 relevant: Yes
- Top 3 relevant: Yes
- Notes: Exact policy section retrieved first.

### 3. How do I submit an expense reimbursement?
- Expected topic: Expense submission process
- Top 1 relevant: Yes
- Top 3 relevant: Yes
- Notes: Exact submission-process section retrieved first.

### 4. What should I do if I suspect harassment?
- Expected topic: Harassment reporting
- Top 1 relevant: Yes
- Top 3 relevant: Yes
- Notes: Strong retrieval quality. Relevant reporting and conduct sections returned.

## Out-of-scope queries

### 5. What is the company stock price?
- Expected behavior: Refuse to answer because this is outside the policy corpus
- Actual behavior: Returned generic policy-document header chunks
- Notes: Guardrail not implemented yet.

### 6. Who is the CEO’s assistant?
- Expected behavior: Refuse to answer because this is outside the policy corpus
- Actual behavior: Returned weak/irrelevant policy chunks
- Notes: Guardrail not implemented yet.

## Summary
Retrieval quality is strong for most in-scope policy questions. The main remaining issues are ranking quality for some queries and the lack of out-of-scope refusal behavior.

## Sprint 3 Refinement Pass

### Improvements made
- Added stronger out-of-scope refusal logic.
- Added simple ranking heuristics for better answer selection.
- Improved handling of questions asking for secrets, live information, or unsupported personal/company details.

### Retest observations
- Vacation question now prioritizes annual allowance over carryover.
- Stock price and CEO assistant questions are refused.
- Wi-Fi password questions are refused instead of returning loosely related IT policy chunks.

### Remaining improvement areas
- Replace heuristic scoring with more robust confidence/relevance logic.
- Improve answer phrasing so the response is more natural and concise.
- Move the Q&A workflow into a Streamlit interface.

## Streamlit MVP Check

### Result
The first Streamlit interface was created successfully.

### Confirmed behavior
- In-scope policy questions returned grounded answers.
- Supporting sources were displayed with filename, section title, and chunk ID.
- Out-of-scope questions were refused with a fallback message.

### Next UI improvements
- make the answer shorter and more polished
- improve page styling
- add a sidebar with sample questions
- add a reset button
