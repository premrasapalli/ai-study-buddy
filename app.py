import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🧠 AI Study Buddy")

topic = st.text_input("Enter a topic:")

def explain(topic):
    prompt = f"You are a friendly teacher. Explain {topic} simply with examples."
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content

def quiz(topic):
    prompt = f"Generate 3 MCQs about {topic} with answers."
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content

def emoji_mode(topic):
    prompt = f"""
    Explain with emojis:

    Gravity → Objects fall down ⬇️🌍  
    Plants grow → Need sunlight ☀️🌱  

    {topic} →
    """
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content

def summarize(topic):
    prompt = f"Summarize {topic} in 5 bullet points."
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return res.choices[0].message.content

if st.button("📘 Explain") and topic:
    st.write(explain(topic))

if st.button("❓ Quiz") and topic:
    st.write(quiz(topic))

if st.button("🎨 Emoji Mode") and topic:
    st.write(emoji_mode(topic))

if st.button("📝 Summary") and topic:
    st.write(summarize(topic))

st.markdown("---")
st.caption("Built with Prompt Engineering 🚀")
