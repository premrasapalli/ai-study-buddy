# ⚙️ Setup Guide (From Scratch)

Follow these steps to run the project locally or deploy it.

---

## 🪜 Step 1: Install Python

Download Python (3.10+ recommended):
https://www.python.org/downloads/

Check installation:
```bash
python --version
🪜 Step 2: Clone Repository
git clone https://github.com/your-username/ai-study-buddy.git
cd ai-study-buddy
🪜 Step 3: Create Virtual Environment (Optional but Recommended)
python -m venv venv

Activate:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
🪜 Step 4: Install Dependencies
pip install -r requirements.txt
🪜 Step 5: Get Groq API Key
Go to https://console.groq.com
Sign up / login
Create API key
🪜 Step 6: Configure API Key
Option A: Local (.env file)

Create .env file:

GROQ_API_KEY=your_api_key_here
Option B: Environment Variable
export GROQ_API_KEY=your_api_key_here   # Mac/Linux
set GROQ_API_KEY=your_api_key_here      # Windows
Option C: Streamlit Cloud
Go to app settings
Add in secrets:
GROQ_API_KEY = "your_api_key_here"
🪜 Step 7: Run Application
streamlit run app.py
🌐 Step 8: Deploy to Streamlit Cloud
Push project to GitHub
Go to https://share.streamlit.io
Click "New App"
Select repo
Choose app.py
Deploy
🧪 Troubleshooting
❌ ModuleNotFoundError

Run:

pip install -r requirements.txt
❌ API Error
Check API key
Check model name
Ensure internet connection
❌ App Not Loading
Restart Streamlit
Check logs
✅ Recommended Model

Use this Groq model:

llama-3.1-8b-instant
🎉 Done!

Your AI Study Buddy app is now running successfully 🚀


---

# 🎉 What You Now Have

- ✅ Industry-level documentation  
- ✅ Beginner-friendly setup  
- ✅ Interview-ready explanation  
- ✅ GitHub professional structure  

---

# 🚀 If You Want Next

I can help you:

- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}
- :contentReference[oaicite:3]{index=3}

---

👉 Just say:  
**“prepare resume description”** or **“add screenshots section”**

access the app https://calculator-todo-nepp8n8rwgouvtssvdziah.streamlit.app/
