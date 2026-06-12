import streamlit as st
from ai_logic import sarathi_ai
from pypdf import PdfReader
from gtts import gTTS
import base64
import os

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Sarathi AI",
    page_icon="🧭",
    layout="wide"
)

# ---------------------------
# 🌍 i18n SYSTEM
# ---------------------------
LANG = {
    "en": {
        "title": "🧭 Sarathi AI",
        "subtitle": "Your Career & Learning Assistant",
        "welcome": "Welcome to Sarathi AI",
        "features": "Placements | Python | Hackathons | Resume | Career",
        "language": "🌐 Language",
        "sample": "Choose a question",
        "input": "Ask Sarathi AI",
        "button": "🚀 Generate",
        "warn": "Please enter a question",
        "success": "Generated Successfully!",
        "response": "📋 Response",
        "actions": "📌 Important Actions",
        "pdf_success": "PDF loaded successfully",
        "footer": "Built for Hackathon"
    },
    "te": {
        "title": "🧭 సారథి AI",
        "subtitle": "మీ కెరీర్ అసిస్టెంట్",
        "welcome": "సారథి AIకి స్వాగతం",
        "features": "ప్లేస్‌మెంట్స్ | పైథాన్ | హ్యాకథాన్ | రెజ్యూమ్ | కెరీర్",
        "language": "🌐 భాష",
        "sample": "ప్రశ్న ఎంచుకోండి",
        "input": "AIని అడగండి",
        "button": "🚀 పొందండి",
        "warn": "దయచేసి ప్రశ్న ఇవ్వండి",
        "success": "విజయవంతంగా తయారైంది!",
        "response": "📋 సమాధానం",
        "actions": "📌 ముఖ్యమైన చర్యలు",
        "pdf_success": "PDF లోడ్ అయింది",
        "footer": "హ్యాకథాన్ కోసం రూపొందించబడింది"
    }
}

# ---------------------------
# LANGUAGE SELECTOR
# ---------------------------
lang = st.sidebar.selectbox("Language", ["en", "te"])
t = LANG[lang]

# ---------------------------
# TITLE
# ---------------------------
st.title(t["title"])
st.subheader(t["subtitle"])
st.write(t["features"])

# ---------------------------
# PDF UPLOAD
# ---------------------------
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
pdf_text = ""

if uploaded_file:
    try:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            pdf_text += page.extract_text() or ""

        st.success(t["pdf_success"])

    except Exception as e:
        st.error(f"PDF error: {e}")

# ---------------------------
# INPUT
# ---------------------------
sample_question = st.selectbox(
    t["sample"],
    ["", "Python roadmap", "Placement tips", "Hackathon guide"]
)

user_input = st.text_area(t["input"], value=sample_question)

# ---------------------------
# AUDIO FUNCTION
# ---------------------------
def speak(text, lang_code):
    try:
        tts = gTTS(text=text, lang=lang_code)
        file = "voice.mp3"
        tts.save(file)

        audio_bytes = open(file, "rb").read()
        b64 = base64.b64encode(audio_bytes).decode()

        st.markdown(
            f'<audio autoplay controls src="data:audio/mp3;base64,{b64}"></audio>',
            unsafe_allow_html=True
        )
    except:
        st.warning("Voice not available")

# ---------------------------
# BUTTON ACTION
# ---------------------------
if st.button(t["button"]):

    if not user_input.strip():
        st.warning(t["warn"])
    else:

        context = pdf_text if uploaded_file else ""

        # AI RESPONSE
        response = sarathi_ai(user_input, lang, context)

        st.success(t["success"])

        st.markdown(f"## {t['response']}")
        st.write(response)

        # VOICE OUTPUT
        speak(response, "te" if lang == "te" else "en")

        # ACTIONS EXTRACTION
        st.markdown("---")
        st.subheader(t["actions"])

        action_prompt = f"""
Extract actions, deadlines, and tasks:

{context}
Question: {user_input}
"""

        actions = sarathi_ai(action_prompt, lang, context)
        st.write(actions)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.caption(t["footer"])
