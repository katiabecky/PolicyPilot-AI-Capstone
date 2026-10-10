# PolicyPilot AI — Demo / Presentation Outline

## 1. Presentation Goal
The goal of this presentation is to demonstrate the design, functionality, testing, and practical value of PolicyPilot AI as a working capstone software artifact.

## 2. Presentation Length
Target length: 15 to 20 minutes

## 3. Recording Requirements
- Be visible on camera during the presentation
- Show a government-issued ID at the beginning so name and photo are visible
- Demonstrate the working software through screen sharing
- Export the final recording as a single video file

## 4. Recommended Presentation Structure

### 0:00 - 1:00 | Identity Verification
- Greet the reviewer
- Briefly introduce yourself
- Show your government-issued ID clearly to the camera
- State the project title: PolicyPilot AI

### 1:00 - 3:00 | Project Introduction
Explain:
- what PolicyPilot AI is
- what problem it solves
- why this problem matters
- the scope of the MVP

Suggested talking points:
- Employees often need fast answers to policy questions
- Policy information is spread across multiple documents
- PolicyPilot AI helps retrieve grounded answers from policy documents
- The MVP focuses on policy-related questions and refusal of unsupported questions

### 3:00 - 6:00 | System Design Overview
Explain the main components:
- policy document corpus
- chunked data
- Chroma vector store
- retrieval pipeline
- ranking heuristics
- refusal logic
- Streamlit user interface

Suggested talking points:
- Documents were prepared and chunked for retrieval
- ChromaDB stores the chunk vectors persistently
- The system retrieves relevant chunks for a user query
- The app returns grounded answers when support is strong
- The app refuses unsupported questions when support is weak

### 6:00 - 11:00 | Live Application Demo
Demonstrate at least 4 successful in-scope questions:
1. How many vacation days do employees get?
2. What are the password requirements?
3. How do I submit an expense reimbursement?
4. What should I do if I suspect harassment?

For each example:
- enter the question
- show the answer
- scroll to the sources
- expand at least one source excerpt
- explain how the source supports the answer

### 11:00 - 13:00 | Out-of-Scope / Refusal Demo
Demonstrate unsupported questions such as:
- What is the company stock price?
- Who is the CEO’s assistant?
- What is the office Wi-Fi password today?

Explain:
- these are outside the supported policy corpus
- the system refuses when there is not enough support
- this improves trustworthiness and reduces unsupported answers

### 13:00 - 15:00 | Testing Summary
Summarize how the system was tested:
- setup validation
- retrieval testing
- CLI testing
- Streamlit UI testing

Suggested talking points:
- test_vector_setup.py verified the vector database setup
- retrieve_chunks.py tested retrieval quality
- answer_question.py tested answer generation and refusal behavior
- Streamlit testing confirmed the end-to-end user workflow

### 15:00 - 17:00 | Challenges and Improvements
Discuss:
- retrieval ranking issues in early versions
- adding refusal logic for unsupported questions
- keeping the scope realistic for an MVP

Suggested future improvements:
- broader policy corpus
- improved ranking and confidence scoring
- stronger UI/UX
- deployment hardening
- formal automated tests

### 17:00 - 18:00 | Closing
Close with:
- what the project demonstrates
- what you learned
- why PolicyPilot AI is a valid capstone deliverable

Suggested closing idea:
PolicyPilot AI demonstrates a functional retrieval-based policy assistant that provides grounded answers, visible source traceability, and refusal safeguards for unsupported questions.

## 5. Demo Preparation Checklist
Before recording, make sure:
- the Streamlit app is already running
- your test questions are ready in a text file
- unnecessary browser tabs are closed
- zoom level makes text easy to read
- your webcam is working
- your microphone is clear
- the app is tested one final time before recording

## 6. Suggested Demo Assets
Useful materials to have ready:
- GitHub repository
- Streamlit app
- screenshots folder
- design and testing document
- reflection notes
- agile board link
- deployed app link, if available

## 7. Final Submission Reminder
The final presentation should align with the written documentation and show that the software is functional, tested, and understandable to a reviewer.
