import streamlit as st
import plotly.express as px

# Inject custom CSS to use Orbitron font for Streamlit UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Orbitron', sans-serif;
        color: white;
        background-color: #1E1E2F;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Orbitron', sans-serif;
        color: #FF69B4;  /* Bright pink titles */
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("The Impact Twitch on Sales")
st.markdown("This is the description of the title")



