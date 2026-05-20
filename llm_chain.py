from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_response(module, domain, chat_history, user_question):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""
You are a strict domain-specific AI mentor.

Selected module: {module}
Allowed domain: {domain}

Rules:
1. Answer only if the question is related to the selected module.
2. If the question is outside the selected module, reply exactly:
Sorry, I don’t know about this question. Please ask something related to the selected module.
3. Give clear, structured, educational answers.
4. Use previous chat history only for continuity.
"""),
        ("human", """
Chat history:
{chat_history}

User question:
{user_question}
""")
    ])

    chain = prompt | llm

    response = chain.invoke({
        "chat_history": chat_history,
        "user_question": user_question
    })

    return response.content