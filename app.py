import streamlit as st
from pypdf import PdfReader

from ai_logic import generate_summary, ask_question
from translations import LANG

st.set_page_config(
    page_title="Sarathi AI",
    page_icon="🧭",
    layout="wide"
)

language = st.sidebar.selectbox(
    "🌍 Language",
    ["English", "Telugu", "Hindi"]
)

t = LANG[language]

st.title(t["title"])

st.write(
    "Upload a PDF and generate summaries or ask questions using Local AI (Llama3)"
)

uploaded_file = st.file_uploader(
    t["upload"],
    type=["pdf"]
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    text = ""

    st.write("📄 Number of pages:", len(pdf.pages))

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.write("📝 Characters extracted:", len(text))

    if len(text) > 0:

        st.subheader("📖 Document Preview")

        st.text_area(
            "Document Text",
            text[:3000],
            height=300
        )

        st.subheader(t["summary"])

        if st.button(t["summary"]):

            with st.spinner(
                "Generating summary using Llama3..."
            ):

                summary = generate_summary(
                    text,
                    language
                )

            st.success("Summary Generated!")

            st.write(summary)

        st.divider()

        st.subheader(t["question"])

        question = st.text_input(
            "Enter your question"
        )

        if st.button(t["answer_btn"]):

            if question.strip():

                with st.spinner(
                    "Generating answer..."
                ):

                    answer = ask_question(
                        text,
                        question,
                        language
                    )

                st.success("Answer Found!")

                st.write(answer)

            else:
                st.warning("Please enter a question.")

    else:

        st.error(
            "No text extracted from PDF. This PDF may be scanned and require OCR."
        )