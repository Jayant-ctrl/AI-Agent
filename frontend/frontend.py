import streamlit as st
import requests

st.set_page_config(page_title="Langgraph Agent UI", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f5;
        }
        .stTextArea textarea { font-size: 16px; border-radius: 8px; }
        .stButton>button { background-color: #007bff; color: white; font-size: 18px; border-radius: 8px; padding: 10px; }
        .response-box { padding: 15px; background-color: #ffffff; border-radius: 10px; border: 1px solid #ddd; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
        .stRadio div[role="radiogroup"] label { color: #007bff; font-weight: bold; }
        .animated-response { animation: fadeIn 1s ease-in-out; }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 AI AGENT")
st.write("### 🔨 Create and Interact with AI Agents!")

# Define two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🔧 Agent Settings")
    system_prompt = st.text_area("✍️ Define your AI Agent:", height=70, placeholder='Type your system prompt here...')
    
    provider = st.radio("📡 Select Provider:", ("Groq", "OpenAI"))
    
    MODEL_NAMES_GROQ = ['llama3-70b-8192', 'deepseek-r1-distill-llama-70b', 'mixtral-8x7b-32768']
    MODEL_NAMES_OPENAI = ['whisper-large-v3']
    
    if provider == "Groq":
        selected_model = st.selectbox("🤖 Select Groq Model:", MODEL_NAMES_GROQ)
    else:
        selected_model = st.selectbox("🤖 Select OpenAI Model:", MODEL_NAMES_OPENAI)
    
    allow_web_search = st.checkbox("🌐 Allow Web Search")
    
    user_query = st.text_area("💬 Enter your query:", height=150, placeholder="Type your query here...")
    
    API_URL = 'http://127.0.0.1:9999/chat'
    
    if st.button("🚀 Ask Agent!", use_container_width=True):
        if user_query.strip():
            payload = {
                'model_name': selected_model,
                'model_provider': provider,
                'system_prompt': system_prompt,
                'messages': [user_query],
                'allow_search': allow_web_search,
            }
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                if 'error' in response_data:
                    st.error(response_data['error'])
                else:
                    st.session_state.response = response_data
            else:
                st.error("❌ Failed to fetch response. Try again.")

with col2:
    st.subheader("📜 Agent Response")
    response_placeholder = st.empty()
    
    if "response" in st.session_state:
        response_placeholder.markdown(
            f"""
            <div class="response-box animated-response">
                <h3>AI Response</h3>
                <p><b>✅ Final Response:</b></p>
                <blockquote>{st.session_state.response}</blockquote>
            </div>
            """,
            unsafe_allow_html=True
        )

