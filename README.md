☁️ 🚀 Deploy on Streamlit Cloud (Free)
🌐 Step 1: Create GitHub Account

Go to:
👉 GitHub official website

Sign up (if you don’t have one)
This is where your code will live
📁 Step 2: Upload Your Project to GitHub
Create a new repository:
Click New Repository
Name: ai-study-buddy
Make it Public
Upload files:

You need these 2 files:

📄 app.py

(your Streamlit code)

📄 requirements.txt

Create this file:

streamlit
openai
🔐 Step 3: Store API Key Safely

⚠️ Never put API key in code!

In Streamlit Cloud, you’ll add it securely.

☁️ Step 4: Deploy on Streamlit Cloud

Go to:
👉 Streamlit Cloud

Steps:
Click "New app"
Connect your GitHub
Select your repo: ai-study-buddy
Choose file: app.py
Click Deploy
🔑 Step 5: Add API Key (IMPORTANT)

After deployment:

Go to App Settings → Secrets
Add this:
OPENAI_API_KEY = "your_api_key_here"
🔁 Step 6: Update Your Code (if needed)

Make sure your code uses:

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
🎉 Done!

You’ll get a live link like:

https://your-app-name.streamlit.app

You can:

Share it
Add to resume
Show in interviews 💼
⚠️ Common Beginner Mistakes
❌ Forgetting requirements.txt
❌ Wrong file name (must be app.py)
❌ API key in code (never do this)
❌ Repo is private (make it public)
🚀 Want Next Level?

I can help you:

🔥 Make your app look professional
Sidebar navigation
Better UI design
📊 Add features
Topic history
Download notes as PDF
💼 Make it resume + GitHub ready
README file
Screenshots
Project description

👉 Just say:
“improve UI” or “make GitHub README”
