import streamlit as st
from modules import MODULES
from llm_chain import get_response

st.set_page_config(
    page_title="AI Chatbot Mentor",
    page_icon="🤖",
    layout="centered"
)

st.title("👋 Welcome to AI Chatbot Mentor")
st.write("Your personalized AI learning assistant.")
st.write("Please select a learning module to begin your mentoring session.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

selected_module = st.selectbox(
    "📌 Available Modules:",
    list(MODULES.keys())
)

if selected_module != st.session_state.selected_module:
    st.session_state.selected_module = selected_module
    st.session_state.messages = []

if selected_module:
    st.divider()

    emoji_map = {
        "Python": "🐍",
        "SQL": "🗄️",
        "Power BI": "📊",
        "Exploratory Data Analysis (EDA)": "🔍",
        "Machine Learning (ML)": "🤖",
        "Deep Learning (DL)": "🧠",
        "Generative AI": "✨",
        "Agentic AI": "🛠️"
    }

    st.subheader(f"Welcome to {selected_module} AI Mentor {emoji_map.get(selected_module, '')}")
    st.write(f"I am your dedicated mentor for {selected_module}.")
    st.write("How can I help you today?")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_question = st.chat_input(f"Ask something related to {selected_module}")

    if user_question:
        st.session_state.messages.append({
            "role": "user",
            "content": user_question
        })

        with st.chat_message("user"):
            st.write(user_question)

        chat_history = ""
        for msg in st.session_state.messages:
            chat_history += f"{msg['role'].upper()}: {msg['content']}\n"

        answer = get_response(
            selected_module,
            MODULES[selected_module],
            chat_history,
            user_question
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):
            st.write(answer)

    st.divider()

    conversation_text = f"AI Chatbot Mentor Conversation\nSelected Module: {selected_module}\n\n"

    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "AI Mentor"
        conversation_text += f"{role}: {msg['content']}\n\n"

    st.download_button(
        label="📥 Download Chat History",
        data=conversation_text,
        file_name=f"{selected_module}_chat_history.txt",
        mime="text/plain"
    )