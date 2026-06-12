import streamlit as st
from ai_logic import sarathi_ai

# Page settings
st.set_page_config(
    page_title="Sarathi AI",
    page_icon="🧭",
    layout="wide"
)

# Title
st.title("🧭 Sarathi AI")
st.subheader("Your Career & Learning Guide Assistant")

st.markdown("""
Welcome to **Sarathi AI**.

Get guidance for:
- 💼 Placements
- 🐍 Python Learning
- 🏆 Hackathons
- 📄 Resume Building
- 🚀 Career Planning
""")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.info("Sarathi AI helps students plan their learning journey.")

# Sample Questions
sample_question = st.selectbox(
    "Choose a sample question",
    [
        "",
        "How to prepare for placements?",
        "How to become a Python developer?",
        "Give me hackathon tips",
        "How can I improve my resume?",
        "Career guidance after college"
    ]
)

# Input
user_input = st.text_area(
    "Ask Sarathi AI",
    value=sample_question,
    height=150
)

# Button
if st.button("🚀 Generate Guidance"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = sarathi_ai(user_input)

        st.success("Guidance Generated")

        st.markdown("## 📋 Response")
        st.write(response)

# Footer
st.markdown("---")
st.caption("Built for Hackathon Demo")
