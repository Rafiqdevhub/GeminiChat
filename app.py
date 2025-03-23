import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in environment variables. Please set it in a .env file.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(
    page_title="GeminiChat",
    page_icon="🤖",
    layout="wide"
)

def get_chat_session():
    if "chat" not in st.session_state:
        st.session_state.chat = genai.GenerativeModel('gemini-2.0-flash').start_chat(
            history=[],
        )
    return st.session_state.chat

st.title("🤖 GeminiChat: Your AI Companion")

with st.sidebar:
    st.header("Settings")
    
    temperature = st.slider(
        "Temperature", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.7, 
        step=0.1,
        help="Higher values make output more creative but potentially less accurate"
    )
    
    model_option = st.selectbox(
        "Select Gemini Model",
        ["gemini-2.0-flash", "gemini-2.0"],
        index=0
    )
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.pop("chat", None)
        st.success("Chat history cleared!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        try:
            chat = get_chat_session()
            
            response = chat.send_message(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                )
            )
            
            message_placeholder.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        
        except Exception as e:
            message_placeholder.markdown(f"Error: {str(e)}")
            st.error(f"An error occurred: {str(e)}")