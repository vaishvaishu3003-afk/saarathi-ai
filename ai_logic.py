from gtts import gTTS
import os

# ---------------------------
# 🧠 MAIN AI LOGIC
# ---------------------------
def sarathi_ai(query, lang="en", context=""):
    query = query.lower()

    response = ""

    # ------------------ PYTHON ------------------
    if "python" in query:
        response = """
🐍 Python Developer Roadmap

1. Learn Python fundamentals
2. Practice OOP concepts
3. Learn Git & GitHub
4. Build mini projects
5. Learn Flask/Streamlit
6. Deploy projects online
"""

    # ------------------ PLACEMENT ------------------
    elif "placement" in query:
        response = """
💼 Placement Preparation Plan

1. Practice DSA daily
2. Improve aptitude skills
3. Build strong projects
4. Create a professional resume
5. Attend mock interviews
"""

    # ------------------ HACKATHON ------------------
    elif "hackathon" in query:
        response = """
🏆 Hackathon Success Guide

1. Identify a real-world problem
2. Build an MVP first
3. Focus on deployment
4. Prepare a clear demo
5. Explain impact and future scope
"""

    # ------------------ PDF / CONTEXT MODE ------------------
    elif context:
        response = f"""
📄 Document-Based Answer

Summary:
{context[:500]}

1. Read document carefully
2. Extract key points
3. Focus on deadlines
4. Follow instructions step-by-step
"""

    # ------------------ DEFAULT ------------------
    else:
        response = f"""
🧭 Sarathi AI Guidance

Topic: {query}

1. Understand the fundamentals
2. Create a learning roadmap
3. Build practical projects
4. Practice consistently
5. Showcase your work

🚀 Success comes from continuous learning.
"""

    # ---------------------------
    # 🌍 LANGUAGE ADAPTATION (L10N)
    # ---------------------------
    if lang == "te":
        response = response.replace("Learn", "నేర్చుకోండి")
        response = response.replace("Practice", "అభ్యాసం చేయండి")

    return response


# ---------------------------
# 🎤 VOICE FUNCTION (NEW)
# ---------------------------
def generate_voice(text, lang="en"):
    """
    Converts AI response to speech (English / Telugu)
    """
    try:
        tts = gTTS(text=text, lang=lang)
        file_path = "voice.mp3"
        tts.save(file_path)
        return file_path
    except Exception as e:
        return None
