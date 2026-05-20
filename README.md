# AI Chatbot Mentor 🤖

AI Chatbot Mentor is a domain-specific intelligent learning assistant built using Streamlit and LangChain.
The application provides focused AI mentoring for technical subjects like Python, SQL, Machine Learning, Deep Learning, Generative AI, and more.

Unlike generic chatbots, this system strictly answers only questions related to the selected learning module, ensuring accurate, relevant, and distraction-free learning support.

🚀 Features
📚 Module-based AI mentoring
🎯 Strict domain-restricted responses
❌ Rejects irrelevant questions
💬 Session-based conversation memory
📥 Download conversation history as .txt
🧠 Powered by LangChain + LLM
🖥 Clean and interactive Streamlit UI


📌 Available Modules
Python
SQL
Power BI
Exploratory Data Analysis (EDA)
Machine Learning (ML)
Deep Learning (DL)
Generative AI
Agentic AI


🛠 Tech Stack
Component	Technology
Frontend	Streamlit
AI Orchestration	LangChain
LLM	Groq / Open-source LLM
Environment Variables	python-dotenv
Export Format	.txt


📂 Project Structure
AI_Chatbot_Mentor/
│
├── app.py
├── llm_chain.py
├── modules.py
├── requirements.txt
├── .env
└── README.md


🧠 How It Works
User selects a learning module.
AI mentor initializes for that domain.
User asks questions.
LangChain checks relevance.
Relevant questions are answered.
Irrelevant questions are rejected with:
Sorry, I don’t know about this question. Please ask something related to the selected module.
Chat history is maintained during the session.
Users can download the conversation anytime.
