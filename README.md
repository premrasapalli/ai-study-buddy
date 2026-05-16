# 🧠 AI Study Buddy (Chat-Based Learning Assistant)

## 📌 Overview

AI Study Buddy is a chat-based learning assistant built using Streamlit and Groq API.  
It allows users to interact with an AI model using different prompt engineering techniques.

The app simulates a ChatGPT-like interface and helps users:
- Understand concepts
- Generate quizzes
- Learn using structured prompts

---

## 🎯 Objectives

- Build a real-world AI application
- Apply prompt engineering techniques
- Create a modern chat-based UI
- Integrate free AI APIs (Groq)

---

## 🚀 Features

### 💬 Chat Interface
- ChatGPT-style UI
- User and AI message separation
- Chat history maintained

### 🧠 Prompt Engineering Techniques
- Zero-shot prompting
- Few-shot prompting
- Role-based prompting

### ⚙️ Modes
- 📘 Explain → Concept explanation
- ❓ Quiz → Generate MCQs
- 🎨 Emoji Mode → Fun learning
- 📝 Summary → Short notes

### 🎨 UI/UX
- Dark theme (professional look)
- Sidebar control panel
- Chat bubbles with avatars
- Typing animation (AI thinking)

### 🤖 AI Integration
- Uses Groq API
- Fast inference with LLM models
- Dynamic responses based on prompts

---

## 🛠️ Tech Stack

| Technology | Purpose |
|----------|--------|
| Python | Core programming |
| Streamlit | Web UI |
| Groq API | AI model inference |
| Prompt Engineering | Response control |

---

## 🧠 Prompt Engineering Implementation

### 1. Zero-shot Prompting
- Direct instruction without examples

Example:

Explain gravity in simple terms.


---

### 2. Few-shot Prompting
- Provide examples to guide output

Example:

Gravity → Objects fall down ⬇️🌍
Plants → Need sunlight ☀️🌱

Explain electricity →


---

### 3. Role Prompting
- Assign AI a role/personality

Example:

You are a friendly teacher.
Explain photosynthesis.


---

## 🔄 Application Flow

1. User enters input
2. App builds prompt using selected technique
3. Prompt is sent to Groq API
4. AI generates response
5. Response displayed in chat UI

---

## 📁 Project Structure


ai-study-buddy/
│
├── app.py # Main application
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── setup.md # Setup instructions
└── .github/workflows/ # CI/CD pipeline


---

## 🌐 Deployment

- Hosted on Streamlit Cloud
- Auto-deploy via GitHub
- CI/CD using GitHub Actions

---

## 💼 Real-World Relevance

This project demonstrates:
- AI application development
- Prompt engineering skills
- UI/UX design in Streamlit
- API integration
- Deployment workflow

---

## ⚠️ Limitations

- Depends on API availability
- Free tier may have limits
- No user authentication (yet)

---

## 🚀 Future Enhancements

- Add conversation memory
- Implement streaming responses
- Add login system
- Save chat history
- Multi-language support

---

## 👨‍💻 Author

Your Name

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
