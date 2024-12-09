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
st.title(" ☾⋆⁺₊🎮✩°｡ Intro ☾⋆⁺₊👾✩°｡")
st.markdown("In 2024, video games continue to dominate entertainment, combining cutting-edge technology and creative innovation. Millions of players dive into new releases, fueled by exciting gameplay, digital downloads, and expanding cloud gaming services. With next-gen consoles in full swing and live-service models keeping players engaged, the gaming industry is smashing records and evolving fast. This year, gaming isn’t just about playing—it’s about shaping how people connect and experience stories worldwide")


