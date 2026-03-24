from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="AI Bot", page_icon="🤖", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0e0e10;
    color: #f0f0f0;
}

.stApp { background-color: #0e0e10; }

h1 {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2.4rem;
    background: linear-gradient(135deg, #f9d423, #ff4e50);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}

.subtitle {
    font-size: 0.9rem;
    color: #888;
    margin-top: 2px;
    margin-bottom: 28px;
    letter-spacing: 0.05em;
}

.msg-user {
    display: flex;
    justify-content: flex-end;
    margin: 10px 0;
}
.msg-bot {
    display: flex;
    justify-content: flex-start;
    margin: 10px 0;
}
.bubble-user {
    background: linear-gradient(135deg, #f9d423, #ff4e50);
    color: #0e0e10;
    padding: 12px 18px;
    border-radius: 20px 20px 4px 20px;
    max-width: 72%;
    font-size: 0.95rem;
    font-weight: 500;
    line-height: 1.5;
}
.bubble-bot {
    background: #1e1e22;
    color: #f0f0f0;
    padding: 12px 18px;
    border-radius: 20px 20px 20px 4px;
    max-width: 72%;
    font-size: 0.95rem;
    line-height: 1.5;
    border: 1px solid #2e2e34;
}

div[data-testid="stSelectbox"] label {
    color: #aaa;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("<h1>🤖 AI Bot</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by DeepSeek-R1 · HuggingFace</p>', unsafe_allow_html=True)

# ── Mode selection ────────────────────────────────────────────────────────────
MODES = {
    "1. Funny assistant":        "You are a funny assistant",
    "2. Professional assistant": "You are a professional assistant",
    "3. Sarcastic assistant":    "You are a sarcastic assistant",
    "4. Friendly assistant":     "You are a friendly assistant",
    "5. Helpful assistant":      "You are a helpful assistant",
    "6. Expert assistant":       "You are an expert assistant",
    "7. Wise assistant":         "You are a wise assistant",
    "8. Creative assistant":     "You are a creative assistant",
}

selected_mode = st.selectbox("Select your bot mode:", list(MODES.keys()))

# ── Model init (cached) ───────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1",
        task="text-generation",
        max_new_tokens=1000,
        temperature=0.7,
        huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    )
    return ChatHuggingFace(llm=llm)

model = load_model()

# ── Session state: reset messages when mode changes ───────────────────────────
if "current_mode" not in st.session_state:
    st.session_state.current_mode = selected_mode
    st.session_state.messages = [SystemMessage(content=MODES[selected_mode])]

if st.session_state.current_mode != selected_mode:
    st.session_state.current_mode = selected_mode
    st.session_state.messages = [SystemMessage(content=MODES[selected_mode])]

# ── Render chat history ───────────────────────────────────────────────────────
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.markdown(f'<div class="msg-user"><div class="bubble-user">{msg.content}</div></div>', unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f'<div class="msg-bot"><div class="bubble-bot">{msg.content}</div></div>', unsafe_allow_html=True)

# ── Chat input ────────────────────────────────────────────────────────────────
prompt = st.chat_input("Say something...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.markdown(f'<div class="msg-user"><div class="bubble-user">{prompt}</div></div>', unsafe_allow_html=True)

    with st.spinner("Thinking..."):
        resp = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=resp.content))
    st.markdown(f'<div class="msg-bot"><div class="bubble-bot">{resp.content}</div></div>', unsafe_allow_html=True)
