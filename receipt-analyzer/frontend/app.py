import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend import ingestion, parser, database

st.title("Receipt/Bill Analyzer")

uploaded_file = st.file_uploader("Upload a receipt (.jpg, .png, .pdf)", type=['jpg', 'png', 'pdf'])

if uploaded_file:
    filepath = ingestion.save_file(uploaded_file)
    text = parser.extract_text_from_image(filepath)
    parsed_data = parser.parse_text(text)

    st.write("Extracted Data:", parsed_data)

    if st.button("Save to Database"):
        database.insert_receipt(parsed_data)
        st.success("Receipt saved!")
