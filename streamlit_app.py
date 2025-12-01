import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # optional if you use .env locally

# Use Streamlit secrets or env var
OPENAI_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    st.error("OpenAI API key not found. Add OPENAI_API_KEY to Streamlit secrets or environment.")
    st.stop()

openai.api_key = OPENAI_KEY

system_prompt = """You are a helpful and professional healthcare assistant AI...
(keep your full system prompt here)
"""

def ask_chatbot(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.6,
            max_tokens=500
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("👩‍⚕️ Healthcare Chatbot")
st.write("Ask any health-related question. (Not a substitute for medical consultation!)")

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            reply = ask_chatbot(user_input)
        st.markdown(f"**Chatbot:** {reply}")
        
