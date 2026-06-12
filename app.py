import streamlit as st
from ai_logic import sarathi_ai
from PyPDF2 import PdfReader

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Sarathi AI",
    page_icon="🧭",
    layout="wide"
)

# ---------------------------
# 🌍 i18n Language System
# ---------------------------
LANG = {
    "en": {
        "title": "🧭 Sarathi AI",
        "subtitle": "Your Career & Learning Guide Assistant",
        "welcome": "Welcome to Sarathi AI",
        "features": """
Get guidance for:
- 💼 Placements
- 🐍 Python Learning
- 🏆 Hackathons
- 📄 Resume Building
- 🚀 Career Planning
""",
        "nav": "Navigation",
        "sidebar_info": "Sarathi AI helps students plan their learning journey.",
        "language": "🌐 Language",
        "sample": "Choose a sample question",
        "input": "Ask Sarathi AI",
        "button": "🚀 Generate Guidance",
        "warn": "Please enter a question.",
        "success": "Guidance Generated Successfully!",
        "response": "📋 AI Response",
        "footer": "Built for Hackathon Demo",
        "lang_info_en": "🟢 AI is responding in English mode",
        "pdf_success": "📄 PDF loaded successfully!"
    },
    "te": {
        "title": "🧭 సారథి AI",
        "subtitle": "మీ కెరీర్ & లెర్నింగ్ గైడ్ అసిస్టెంట్",
        "welcome": "సారథి AIకి స్వాగతం",
        "features": """
మార్గదర్శనం పొందండి:
- 💼 ప్లేస్‌మెంట్స్
- 🐍 పైథాన్ లెర్నింగ్
- 🏆 హ్యాకథాన్లు
- 📄 రెజ్యూమ్ తయారీ
- 🚀 కెరీర్ ప్లానింగ్
""",
        "nav": "నావిగేషన్",
        "sidebar_info": "సారథి AI విద్యార్థుల కెరీర్ ప్లానింగ్‌లో సహాయపడుతుంది.",
        "language": "🌐 భాష",
        "sample": "ఉదాహరణ ప్రశ్న ఎంచుకోండి",
        "input": "సారథి AIని అడగండి",
        "button": "🚀 గైడెన్స్ పొందండి",
        "warn": "దయచేసి ప్రశ్న ఇవ్వండి.",
        "success": "గైడెన్స్ విజయవంతంగా తయారైంది!",
        "response": "📋 సమాధానం",
        "footer": "హ్యాకథాన్ డెమో కోసం రూపొందించబడింది",
        "lang_info_te": "🟢 AI తెలుగు మోడ్‌లో స్పందిస్తుంది",
        "pdf_success": "📄 PDF విజయవంతంగా లోడ్ అయింది!"
    }
}

# ---------------------------
# Language Selector
# ---------------------------
lang = st.sidebar.selectbox("🌐 Language / భాష", ["en", "te"])
t = LANG[lang]

# ---------------------------
# Title Section
# ---------------------------
st.title(t["title"])
st.subheader(t["subtitle"])

st.markdown(f"""
### {t["welcome"]}

{t["features"]}
""")

# ---------------------------
# Language Mode Info
# ---------------------------
if lang == "te":
    st.info(t["lang_info_te"])
else:
    st.info(t["lang_info_en"])

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title(t["nav"])
st.sidebar.info(t["sidebar_info"])

# ---------------------------
# 📄 STEP 5: PDF Upload Feature
# ---------------------------
uploaded_file = st.file_uploader("📄 Upload PDF Document", type=["pdf"])

pdf_text = ""

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"

    st.success(t["pdf_success"])

# ---------------------------
# Sample Questions
# ---------------------------
sample_question = st.selectbox(
    t["sample"],
    [
        "",
        "How to prepare for placements?",
        "How to become a Python developer?",
        "Give me hackathon tips",
        "How can I improve my resume?",
        "Career guidance after college"
    ]
)

# ---------------------------
# Input Section
# ---------------------------
user_input = st.text_area(
    t["input"],
    value=sample_question,
    height=150
)

# ---------------------------
# Button Action (STEP 5 UPDATED)
# ---------------------------
if st.button(t["button"]):

    if user_input.strip() == "":
        st.warning(t["warn"])
    else:
        # 📄 Combine PDF + user input
        context = pdf_text if uploaded_file else ""

        # 🧠 Pass language + document context to AI
        response = sarathi_ai(user_input, lang, context)

        st.success(t["success"])

        st.markdown(f"## {t['response']}")
        st.write(response)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption(t["footer"])
