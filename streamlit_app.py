import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = 'YOUR_OPENAI_API_KEY'
# Initialize OpenAI client using Streamlit's secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# Strict system prompt to restrict scope
system_prompt = """
You are a helpful and professional healthcare assistant AI.
You can answer questions about symptoms, general health advice, nutrition, and first-aid.
You are NOT a doctor, so always recommend users to consult a healthcare professional for medical advice.
You only provide information about:
- Health symptoms
- Common diseases
- Medications (general info)
- Nutrition and diet
- First-aid
- Preventive care
- Mental health
- Health checkups
- Exercise and wellness
You MUST refuse to answer any question not related to health or wellness.

If the user asks anything outside of the healthcare domain (e.g., tech, politics, history, movies, math), respond with:
"I'm sorry, I can only assist with healthcare-related topics."

You are not a doctor, so always remind the user to consult a licensed medical professional for any serious or personal concerns.
"""

def ask_chatbot(user_input):
    try:
        response = OpenAI.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.6,
            max_tokens=500
        )
        reply = response['choices'][0]['message']['content']
        return reply.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("👩‍⚕️ Healthcare Chatbot")
st.write("Ask any health-related question. (Not a substitute for medical consultation!)")

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input:
        response = ask_chatbot(user_input)
        st.success(f"Chatbot: {response}")

