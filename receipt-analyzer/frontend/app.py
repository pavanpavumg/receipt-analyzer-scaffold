import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend import database, algorithms

# Custom CSS using st.markdown
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4F8BF9;
        color: white;
        border-radius: 8px;
        padding: 0.5em 2em;
        font-size: 1.1em;
        font-weight: bold;
        border: none;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #4F8BF9;
    }
    .stFileUploader>div>div {
        border-radius: 8px;
        border: 2px dashed #4F8BF9;
        background-color: #eaf0fb;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Receipt/Bill Analyzer")

# Load all receipts from DB
receipts = database.get_all_receipts()

st.subheader("Uploaded Receipts")
st.dataframe(receipts)

# Search by vendor
search_term = st.text_input("Search by Vendor")
if search_term:
    results = algorithms.linear_search(receipts, keyword=search_term, field='vendor')
    st.write("Search Results")
    st.dataframe(results)

# Sort by field
sort_field = st.selectbox("Sort by Field", ['amount', 'date', 'vendor', 'category'])
sorted_receipts = algorithms.sort_records(receipts, sort_field)
st.subheader(f"Sorted by {sort_field}")
st.dataframe(sorted_receipts)

# Aggregation statistics
st.subheader("Statistics")
stats = algorithms.aggregate_stats(receipts, 'amount')
st.write(stats)

# Vendor frequency bar chart
st.subheader("Vendor Frequency")
vendor_counts = algorithms.vendor_histogram(receipts)
st.bar_chart(vendor_counts)

# Monthly spend trend line chart
st.subheader("Monthly Spend Trend")
monthly = algorithms.monthly_trend(receipts)
st.line_chart(monthly)
