import streamlit as st
import os
from groq import Groq
import time

st.set_page_config(page_title="AI Study Buddy", page_icon="🧠", layout="wide")

# 🎨 DARK THEME CSS
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: white;
}

/* Chat bubbles */
.user-msg {
    background-color: #1e293b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.bot-msg {
    background-color: #020617;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
}

/* Buttons */
.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🧠 Header
st.title("🧠 AI Study Buddy")
st.caption("Chat + Prompt Engineering 🚀")

# 📌 Sidebar
st.sidebar.title("⚙️ Control Panel")

mode = st.sidebar.selectbox(
    "Mode",
    ["Explain", "Quiz", "Emoji", "Summary"]
)

prompt_type = st.sidebar.selectbox(
    "Prompt Technique",
    ["Zero-shot", "Few-shot", "Role"]
)

# 🧠 Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# 💬 Display chat with avatars
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="user-msg">
        👤 <b>You:</b><br>{msg["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bot-msg">
        🤖 <b>AI:</b><br>{msg["content"]}
        </div>
        """, unsafe_allow_html=True)

# ✍️ Input
user_input = st.chat_input("Ask anything...")

# 🧠 Prompt builder
def build_prompt(user_input):
    if prompt_type == "Zero-shot":
        return f"Explain {user_input} clearly."

    elif prompt_type == "Few-shot":
        return f"""
        Explain with examples:

        Gravity → Objects fall ⬇️🌍  
        Plants → Need sunlight ☀️🌱  

        {user_input} →
        """

    else:
        return f"""
        You are a friendly teacher.

        Explain {user_input} in simple terms with examples.
        """

from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(user_input):
    prompt = build_prompt(user_input)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
# 💬 Chat logic
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show typing animation
    with st.spinner("🤖 AI is thinking..."):
        time.sleep(1.5)  # simulate delay
        response = generate_response(user_input)

    # Add AI response
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()

# Footer
st.markdown("---")
st.caption("💼 Industry-Level Prompt Engineering Chat App")
