# app.py
import streamlit as st
import json
import os
import matplotlib.pyplot as plt
from src.main import parse_file

st.set_page_config(page_title="Credit Card Parser", layout="wide")

# --- Sidebar ---
st.sidebar.title("About")
st.sidebar.info(
    "This is a Smart Credit Card Statement Parser that extracts key information "
    "from your credit card statements."
)
st.sidebar.title("How to use")
st.sidebar.markdown(
    "1. **Upload your PDF statement.**\n"
    "2. **The app will parse the data.**\n"
    "3. **View and download the extracted JSON.**"
)

# --- Main Page ---
st.title("Smart Credit Card Statement Parser 💳")

uploaded_file = st.file_uploader("Upload a credit card PDF", type=["pdf"])

if uploaded_file:
    # Save uploaded file temporarily
    temp_dir = "temp_files"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, uploaded_file.name)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner(f"Parsing {uploaded_file.name}..."):
        # Parse PDF
        output_path = parse_file(temp_path, output_dir="streamlit_output")

    if output_path:
        # Display parsed JSON
        with open(output_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        st.success("Successfully parsed the statement!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Extracted Information")
            st.json(data)

            # Add a download button for the JSON data
            st.download_button(
                label="Download JSON",
                data=json.dumps(data, indent=2),
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}.json",
                mime="application/json",
            )

        with col2:
            # Plot transactions chart if available
            if data.get("transactions"):
                st.subheader("Spending Chart")
                dates = [t["date"] for t in data["transactions"]]
                amounts = [t["amount"] for t in data["transactions"]]

                fig, ax = plt.subplots(figsize=(10, 4))
                ax.bar(dates, amounts, color="skyblue")
                plt.xticks(rotation=45)
                ax.set_ylabel("Amount")
                ax.set_title("Transaction Amounts")
                st.pyplot(fig)
            else:
                st.info("No transactions found to display a chart.")

    else:
        st.error("Could not parse the PDF. Please try another file.")

    # Remove temporary file
    os.remove(temp_path)