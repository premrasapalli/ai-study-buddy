import streamlit as st

st.title("🧠 AI Study Buddy (Demo Mode)")

topic = st.text_input("Enter a topic:")

# 📘 Explain
def explain(topic):
    return f"""
📘 **Explanation:**
{topic} is an important concept.

👉 In simple words:
It helps us understand how things work in real life.

👉 Example:
Think about {topic} like something you use daily.

(This is demo mode — add API for real AI responses)
"""

# ❓ Quiz
def quiz(topic):
    return f"""
❓ **Quiz on {topic}:**

1. What is {topic}?
A) Option 1  
B) Option 2  
C) Option 3  
D) Option 4  
✅ Answer: A  

2. Why is {topic} important?
A) Reason 1  
B) Reason 2  
C) Reason 3  
D) Reason 4  
✅ Answer: B  
"""

# 🎨 Emoji Mode
def emoji_mode(topic):
    return f"""
🎨 **Fun Learning with Emojis:**

{topic} → Learn it easily 📘✨  

Example:
Understanding {topic} makes life easier 💡😊  

(This is demo mode)
"""

# 📝 Summary
def summarize(topic):
    return f"""
📝 **Summary of {topic}:**

- Key point 1  
- Key point 2  
- Key point 3  
- Key point 4  
- Key point 5  

(Demo content)
"""

# 🎛️ Buttons
if st.button("📘 Explain"):
    if topic:
        st.write(explain(topic))

if st.button("❓ Quiz"):
    if topic:
        st.write(quiz(topic))

if st.button("🎨 Emoji Mode"):
    if topic:
        st.write(emoji_mode(topic))

if st.button("📝 Summary"):
    if topic:
        st.write(summarize(topic))

st.markdown("---")
st.caption("🚀 Built with Prompt Engineering (Demo Mode)")
