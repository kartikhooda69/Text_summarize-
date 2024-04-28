import streamlit as st
from text_sum import summarize_pdf

st.title('NLP Summarizer')

uploaded_file = st.file_uploader("Upload PDF", type=['pdf'])

if uploaded_file is not None:
    num_sentences = st.number_input("Number of Sentences", value=10)
    summary = summarize_pdf(uploaded_file, num_sentences)
    st.write("Summary:")
    st.write(summary)
