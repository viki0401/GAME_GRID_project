import streamlit as st
import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

st.image("love123.JPEG")


# Title and description
st.markdown("""     
#  | Twitch Streaming Analysis|
            
Twitch has grown to become one of the leading platforms for live streaming, especially in the gaming industry.However, there are several factors that contribute to the success of streamers, including the choice of game to stream and the language used to broadcast.
 

This project involves collecting and analyzing publicly available Twitch data on the most streamed languages and popular games over a specific period. The analysis will examine trends, correlations, and visualizations to provide valuable insights.



Despite the large number of streamers on Twitch, still many creators struggle to grow their audience and attract more viewers, because making decision without clear guidance on language, timing, and which games to stream isn’t the easy one.Solving this problem would provide helpful insights for streamers, creators, and marketers on Twitch. By knowing which languages and games are trending, streamers can grow their audiences, and new creators have a better chance to succeed.It also helps developers, advertisers, and investors better target popular trends, making their efforts more effective and profitable.


            
### 📚 Data Sources
- 🌐 **Kaggle**: Accessed comprehensive twitch datasets.

### 🛠️ Tools Used
- **🧹 Data Cleaning & Analysis:**  
    - 🐼 Pandas for efficient data manipulation.
- **📊 Visualization:**  
    - 📈 Matplotlib for static graphs. 
    - 🖼️ Plotly for interactive graphs.  
    - 📋 Tableau for creating professional dashboards.
- **📱 Interactivity:**  
    - 📌 QR.io for generating QR codes linked to dashboards.
- **🤝 Collaboration:**   
    - 🗂️ GitHub for version control and team collaboration.
- **🤖 Insights:**  
    - 💬 ChatGPT for generating natural language summaries and insights.

---
""")
st.markdown("""
### 🎮 But Why Game Choice Matters on Twitch  ?

Understanding the most streamed games provides valuable insights into viewer trends and preferences. Selecting the right game can make a big difference for streamers, businesses, and marketers:  

- 🟠 **For Streamers**:  
   - Established streamers can diversify content by exploring trending titles or balancing popular games with niche categories to attract and retain viewers.  
   - New streamers can identify rising games or underserved niches to stand out and build a loyal audience.  

- 🟠 **For Businesses & Marketers**:  
   - Focus on games with the highest visibility and engagement to connect with the most active communities.  
   - Collaborate with streamers playing trending titles to ensure advertising reaches an engaged and relevant audience.  

 Let’s explore ways to ensure success and avoid failure by taking a closer look at what’s popular on the Twitch platform right now. By analyzing current trends, streamers can leverage these insights to make informed decisions and set themselves up for success in a fast-evolving streaming landscape
""")
import streamlit as st


st.page_link("pages/what.py", icon= "🗣️",label="Next Page", help="Navigate to the next page", disabled=False)
