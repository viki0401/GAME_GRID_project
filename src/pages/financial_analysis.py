import streamlit as st

# Set background color using CSS
st.markdown(
    """
    <style>
    body {
        background-color: beige;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit content
st.title("Streamlit App with Beige Background")
st.write("This app has a beige background color!")
