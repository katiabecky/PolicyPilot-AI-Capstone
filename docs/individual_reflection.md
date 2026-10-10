# PolicyPilot AI — Individual Reflection

## 1. Introduction
This capstone project gave me the opportunity to apply software engineering concepts in a practical way by designing and building a working software artifact. For my project, I developed **PolicyPilot AI**, a retrieval-augmented policy assistant that helps users ask questions about company policies and receive grounded answers based on internal policy documents.

I chose this project because it combines several topics that I wanted to understand better, including information retrieval, document-based question answering, lightweight AI application design, and user-focused software delivery. I also liked that it could solve a realistic business problem: employees often need quick answers to policy questions, but the information is spread across multiple documents and can be time-consuming to find manually.

## 2. Original Goal
My original goal was to build a simple but functional system that could:
- search a small internal policy corpus,
- retrieve the most relevant policy content,
- present a useful answer in a simple interface, and
- avoid answering questions that were not supported by the available documents.

I wanted the final result to be practical, easy to demonstrate, and clearly aligned with the capstone requirement of producing a working software artifact supported by design and testing documentation.

## 3. What I Built
The final MVP of PolicyPilot AI includes:
- a local corpus of policy documents,
- chunked policy data prepared for retrieval,
- a persistent Chroma vector database,
- Python scripts for setup, retrieval testing, and question answering,
- a Streamlit web app interface,
- source-backed answers with visible metadata, and
- refusal handling for unsupported or out-of-scope questions.

The application can successfully answer questions related to company policies such as vacation, expenses, workplace conduct, and IT security. It can also refuse unsupported questions such as real-time company data requests or confidential information not contained in the current policy set.

## 4. What I Learned
One of the biggest lessons from this project was that building even a small AI-powered system requires much more than simply retrieving text. I learned that relevance, ranking quality, guardrails, and transparency all matter if the result is meant to be useful and trustworthy.

I also learned the importance of metadata in retrieval systems. By storing the filename, section title, and chunk ID for each policy chunk, I was able to make the app more explainable and easier to validate during testing.

Another important lesson was the value of iterative testing. Early retrieval results were not always ideal, and some unsupported questions initially produced weak or misleading answers. Refining the logic step by step helped improve both the usefulness and the credibility of the system.

## 5. Challenges I Encountered
One challenge was making sure the app returned the *right* chunk first rather than just a related chunk. For example, an early version answered a vacation-days question using the carryover rule instead of the annual vacation allowance section. This showed me that retrieval quality is not only about whether relevant content appears, but also about ranking the most relevant content properly.

Another challenge was handling out-of-scope questions. Some questions sounded related to the company context but were not actually supported by the available policy documents. Without guardrails, the system could return weak matches that did not truly answer the question. This made it necessary to introduce refusal logic and strengthen the filtering approach.

A third challenge was balancing scope. There were many possible improvements I could have added, such as more advanced UI design, broader policy coverage, and more sophisticated answer generation. However, for the capstone, I needed to stay focused on building a solid MVP rather than trying to over-expand the project.

## 6. How I Addressed Those Challenges
To improve retrieval quality, I refined the scoring logic so that stronger matches were prioritized over weaker or generic chunks. This helped the system prefer more appropriate results for common policy questions.

To improve trustworthiness, I added refusal handling for unsupported questions. The system now refuses questions such as requests for stock price information, executive personal details, or live Wi-Fi passwords when there is not enough support in the policy corpus.

To keep the project manageable, I focused on the core use case: answering policy questions with grounded evidence. This decision helped me complete a working system rather than an overly ambitious but unfinished project.

## 7. Strengths of the Final MVP
I believe the final MVP has several strengths:
- it solves a realistic and understandable problem,
- it demonstrates a full retrieval workflow,
- it provides visible source traceability,
- it includes refusal safeguards for unsupported questions,
- and it is simple enough to explain and demonstrate clearly.

The project also reflects a practical software engineering mindset by combining implementation, testing, iteration, and documentation rather than focusing only on coding.

## 8. Limitations
At the same time, the project has clear limitations. The current system depends on a limited policy corpus and does not support real-time data, authentication, or document uploads. The answer generation logic is also intentionally simple, and the interface is functional rather than highly polished.

These limitations are acceptable for an MVP, but they also show that building a more production-ready assistant would require additional engineering work.

## 9. What I Would Improve Next
If I continued developing PolicyPilot AI, I would improve it in several ways:
- expand the document set,
- improve ranking and confidence scoring,
- enhance the visual design of the interface,
- add administrative tools for updating the corpus,
- create a more formal automated test suite,
- and strengthen deployment for a broader audience.

I would also explore how to better distinguish between partially supported questions and clearly unsupported ones.

## 10. Personal Takeaway
Overall, this capstone helped me better understand how software engineering, retrieval systems, testing, and product thinking come together in a real project. It reinforced the importance of defining scope, validating assumptions through testing, and building systems that are not only functional but also trustworthy and explainable.

The most valuable outcome for me was not only producing a working artifact, but also seeing how iterative improvements can transform a rough prototype into a more credible and defensible final project.
