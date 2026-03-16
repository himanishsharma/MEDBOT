import streamlit as st
from pdf_loader import extract_text_from_pdf
from chat_engine import get_chat_response

# Page Configuration
st.set_page_config(page_title="🧬 Medical PDF Chatbot", layout="centered")

# Title and Description
st.markdown("""
    <div style='text-align: center; padding-bottom: 10px;'>
        <h1>🩺 Medical Report Chatbot</h1>
        <p style='font-size: 18px;'>An AI-powered assistant that reads your medical reports and answers your questions accurately and instantly.</p>
        <p style='font-size: 16px; color: #6c757d;'>Built using advanced language models and document understanding techniques.</p>
    </div>
""", unsafe_allow_html=True)

# File Upload and Question Input
uploaded_file = st.file_uploader("📄 Upload a PDF medical report", type="pdf")
user_question = st.text_input("💬 Ask a medical question based on the uploaded report")

# Response Section
if uploaded_file and user_question:
    with st.spinner("🧠 Reading report and thinking..."):
        context_text = extract_text_from_pdf(uploaded_file)
        response = get_chat_response(user_question, context_text)
    st.success("✅ Response")
    st.write(response)

elif not uploaded_file:
    st.info("📌 Please upload a medical report PDF to proceed.")
elif not user_question:
    st.info("📝 Please enter a question related to the report.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center; font-size: 14px; color: #888;'>
        © 2025 Medical Report Chatbot | Developed by <strong>Vaishnav Krishna P</strong>
    </div>
""", unsafe_allow_html=True)
