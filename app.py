import streamlit as st

st.set_page_config(page_title="AI Study Buddy", page_icon="🧠", layout="wide")

# 🎨 Custom CSS (Industry UI)
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #1e293b;
    margin-bottom: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}
.header {
    font-size: 40px;
    font-weight: bold;
}
.sub {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# 🧠 Header
st.markdown('<div class="header">🧠 AI Study Buddy</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Learn smarter with AI-powered prompts</div>', unsafe_allow_html=True)

st.markdown("---")

# 📌 Sidebar
st.sidebar.title("⚙️ Control Panel")

mode = st.sidebar.radio(
    "Select Mode",
    ["📘 Explain", "❓ Quiz", "🎨 Fun Mode", "📝 Summary"]
)

difficulty = st.sidebar.select_slider(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

language = st.sidebar.selectbox(
    "Language",
    ["English", "Telugu", "Hindi"]
)

# 🧠 Session state
if "history" not in st.session_state:
    st.session_state.history = []

# 📥 Input
col1, col2 = st.columns([3,1])

with col1:
    topic = st.text_input("Enter topic", placeholder="e.g. Newton’s Laws")

with col2:
    generate = st.button("🚀 Generate")

# 📘 Functions
def explain(topic):
    return f"""
### 📘 Explanation ({difficulty})
{topic} explained simply.

👉 Example:
Think of it in real life.

🌍 Language: {language}
"""

def quiz(topic):
    return f"""
### ❓ Quiz ({difficulty})

1. What is {topic}?  
A) Option 1  
B) Option 2  
C) Option 3  
D) Option 4  
✅ Answer: A  
"""

def emoji_mode(topic):
    return f"""
### 🎨 Fun Learning

{topic} → Learn easily 📘✨  
💡 Makes learning fun 😄
"""

def summary(topic):
    return f"""
### 📝 Summary

- Point 1  
- Point 2  
- Point 3  
- Point 4  
"""

# 🚀 Generate Output
if generate and topic:
    if mode == "📘 Explain":
        result = explain(topic)
    elif mode == "❓ Quiz":
        result = quiz(topic)
    elif mode == "🎨 Fun Mode":
        result = emoji_mode(topic)
    else:
        result = summary(topic)

    st.session_state.history.append(topic)

    st.markdown(f'<div class="card">{result}</div>', unsafe_allow_html=True)

# 📚 History Panel
st.sidebar.markdown("---")
st.sidebar.subheader("📚 Recent Topics")

for t in st.session_state.history[-5:]:
    st.sidebar.write(f"• {t}")

# 📥 Download
if topic:
    st.download_button(
        "📥 Download Notes",
        data=f"Notes on {topic}",
        file_name=f"{topic}.txt"
    )

# Footer
st.markdown("---")
st.caption("🚀 Industry-Level Prompt Engineering Project")
