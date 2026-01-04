import streamlit as st
from PyPDF2 import PdfReader
from model import classify_document, summarize_text, calculate_rouge

st.title("📄 Intelligent Document Classification & Summarization")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])

if uploaded_file is not None:

    # -------------------------------
    # TEXT EXTRACTION
    # -------------------------------
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    else:
        text = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Extracted Text (Preview)")
    st.write(text[:500])

    # -------------------------------
    # CLASSIFICATION
    # -------------------------------
    doc_type, confidence = classify_document(text)

    # -------------------------------
    # SUMMARY
    # -------------------------------
    summary = summarize_text(text)

    # -------------------------------
    # ROUGE
    # -------------------------------
    rouge_scores = calculate_rouge(text, summary)

    # -------------------------------
    # OUTPUT
    # -------------------------------
    st.subheader("🧠 Document Classification")
    st.write(f"**Type:** {doc_type}")
    st.write(f"**Confidence:** {confidence*100:.2f}%")

    st.subheader("📝 Summary")
    st.write(summary)

    st.subheader("📊 Evaluation Metrics")
    st.write(f"ROUGE-1: {rouge_scores['rouge1'].fmeasure:.2f}")
    st.write(f"ROUGE-2: {rouge_scores['rouge2'].fmeasure:.2f}")
    st.write(f"ROUGE-L: {rouge_scores['rougeL'].fmeasure:.2f}")
