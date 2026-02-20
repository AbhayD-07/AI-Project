import streamlit as st
import numpy as np
import pandas as pd

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="My Streamlit App",
    layout="wide"
)

# -------------------------------
# Main Title & Introduction
# -------------------------------
st.title("🚀 My Streamlit App")
st.write(
    "This is a simple Streamlit app demonstrating how to build interactive "
    "user interfaces using Streamlit."
)

# -------------------------------
# User Input Section
# -------------------------------
st.header("👤 User Interaction")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Welcome to Streamlit!")
    else:
        st.warning("Please enter your name before submitting.")

# -------------------------------
# Data & Charts Section
# -------------------------------
st.header("📊 Data Visualization")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["A", "B"]
)

st.subheader("Line Chart")
st.line_chart(df)

st.subheader("Bar Chart")
st.bar_chart(df)

# -------------------------------
# Sidebar Section
# -------------------------------
st.sidebar.title("📌 Navigation")
st.sidebar.write("This is the sidebar section.")

# -------------------------------
# Media Section
# -------------------------------
st.header("🖼️ Media")

st.image(
    "https://tse3.mm.bing.net/th/id/OIP.iCfB7084Mkn-HeiA8WCG2QHaEK?pid=Api&P=0&h=180",
    caption="Sample Image"
)

st.video("https://youtu.be/MBKgWORXkYk")

# -------------------------------
# File Upload Section
# -------------------------------
st.header("📂 File Upload")

uploaded_file = st.file_uploader(
    "Upload a CSV or TXT file",
    type=["csv", "txt"]
)

if uploaded_file is not None:
    try:
        df_uploaded = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df_uploaded)
    except Exception as e:
        st.error("Error reading file.")

# -------------------------------
# Text & Formatting Section
# -------------------------------
st.header("📝 Text & Formatting")

st.subheader("Subheader Example")
st.markdown("This is a markdown text with **bold** and *italic* formatting.")
st.code("for i in range(5):\n    print(i)")

# -------------------------------
# Input Widgets Section
# -------------------------------
st.header("🎛️ Widgets")

st.text_input("Enter some text:")
st.text_area("Enter a longer text:")
st.number_input("Enter a number:")
st.slider("Select a value", 0, 100, 50)
st.checkbox("Check me out")
st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.multiselect("Select multiple options", ["Option A", "Option B", "Option C"])
st.radio("Choose one", ["Choice 1", "Choice 2", "Choice 3"])