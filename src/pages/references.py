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

import streamlit as st

st.title("☾⋆⁺₊📊✩°｡ References ☾⋆⁺₊🧩✩°｡")

st.markdown("### 📚 Data Sources")
st.markdown("- 🌐 **Kaggle**: Accessed comprehensive gaming datasets.")
st.markdown("### 🛠️ Tools Used")
st.markdown("- **🧹 Data Cleaning & Analysis:**  - 🐼 Pandas for efficient data manipulation.")
st.markdown("- **📊 Visualization:**  - 📈 Matplotlib for static graphs.  - 🖼️ Plotly for interactive graphs.  - 📋 Tableau for creating professional dashboards.")
st.markdown("- **📱 Interactivity:**  - 📌 QR.io for generating QR codes linked to dashboards.")
st.markdown("- **🤝 Collaboration:**   - 🗂️ GitHub for version control and team collaboration.")
st.markdown("- **🤖 Insights:**  - 💬 ChatGPT for generating natural language summaries and insights.")

st.markdown("---")  # Divider line for separation

st.markdown("✨ **GameDrig brings it all together to uncover insights and tell the story behind the numbers!**")







