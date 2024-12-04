import matplotlib.pyplot as plt
import streamlit as st

# Set the font to 'sans-serif' to avoid issues with unsupported fonts like 'Courier New'
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'

# If you want to use a specific font, you can do:
# matplotlib.rcParams['font.family'] = 'Roboto Slab'  # Or another valid font

# Add your custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Roboto Slab', serif;
        color: white;
        background-color: #1E1E2F;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto Slab', serif;
        color: #FF69B4;  /* Bright pink titles */
    }
    </style>
    """, unsafe_allow_html=True)

# Main content
st.title("Home")
st.write("THIS IS THE MAIN PAGE")

# Matplotlib plot (this example should no longer trigger the font warning)
import numpy as np


