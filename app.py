import streamlit as st
import json
import os
import pandas as pd
from src.main import parse_file

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Statement Parser", layout="centered")

# --- HEADER ---
st.markdown("### Statement Parser") 
st.write("Upload a PDF statement to extract the 5 key data points as required.")



# --- SESSION STATE INITIALIZATION ---
if 'parsed_data' not in st.session_state:
    st.session_state.parsed_data = None

# --- UI LOGIC ---
if st.session_state.parsed_data is None:
    uploaded_file = st.file_uploader(
        "Choose a credit card statement PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        temp_dir = "temp_files"
        os.makedirs(temp_dir, exist_ok=True)
        temp_path = os.path.join(temp_dir, uploaded_file.name)

        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner(f"Analyzing {uploaded_file.name}..."):
            output_path = parse_file(temp_path, output_dir="streamlit_output")

        if output_path:
            with open(output_path, "r", encoding="utf-8") as f:
                st.session_state.parsed_data = json.load(f)
            os.remove(temp_path)
            st.rerun()
        else:
            st.error("Could not parse the PDF. Please try another file.")

else:
    st.success("Successfully extracted the key information!")
    data = st.session_state.parsed_data

    st.subheader("Statement Summary")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Cardholder Name", value=data.get("cardholder_name", "N/A"))
        total_due = data.get("total_due") or 0.0
        st.metric(label="Total Amount Due", value=f'₹ {total_due:,.2f}')
        st.metric(label="Bank", value=data.get("bank", "N/A"))

    with col2:
        st.metric(label="Card (Last 4 Digits)", value=data.get("card_last_4", "N/A"))
        st.metric(label="Payment Due Date", value=data.get("due_date", "N/A"))

    transactions = data.get("transactions")
    if transactions:
        with st.expander("View Full Transaction List"):
            df = pd.DataFrame(transactions)
            st.dataframe(df)

    st.markdown("---")

    if st.button("Parse Another Statement"):
        st.session_state.parsed_data = None
        st.rerun()