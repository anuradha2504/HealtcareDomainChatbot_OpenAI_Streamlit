# 🛍️ Retail Domain Chatbot – Streamlit + OpenAI

A conversational chatbot focused entirely on the **Retail domain**, built using **Streamlit** for the UI and **OpenAI's GPT-3.5** for natural language understanding. The chatbot responds only to retail-related questions and politely rejects unrelated queries to stay domain-specific.

---

## 🚀 Features

- 💬 Conversational interface using Streamlit's `st.chat_*`
- 🧠 Powered by OpenAI GPT-3.5
- 🔒 Domain-restricted: Only answers Retail industry topics
- 🛑 Filters non-retail questions with polite responses
- 🧾 Maintains session history using `st.session_state`

---

## 📸 Demo

I have created using streamlit and here is the link: 
https://sriramretaildomainchatbotapp.streamlit.app/

---

## 🧱 Tech Stack

- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- Python 3.8+

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/RetailDomainChatbot_Streamlit_OpenAI.git
cd RetailDomainChatbot_Streamlit_OpenAI
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your OpenAI API Key

#### Option A: Using `.streamlit/secrets.toml` (recommended)

Create a file at `.streamlit/secrets.toml` with:

```toml
[default]
OPENAI_API_KEY = "your-openai-api-key"
```

#### Option B: Set Environment Variable (alternative)

```bash
export OPENAI_API_KEY="your-openai-api-key"  # macOS/Linux
set OPENAI_API_KEY="your-openai-api-key"     # Windows
```

---

### 5. Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Deploy to Streamlit Cloud

1. Push this repo to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) → “New App”
3. Select your GitHub repo and branch.
4. In “Advanced settings” → **Secrets**, paste:

```toml
OPENAI_API_KEY = "your-openai-api-key"
```

5. Click “Deploy” 🎉

---


## 📄 License

This project is open-source
