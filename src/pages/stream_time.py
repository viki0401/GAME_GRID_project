import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
# Inject custom CSS to use Orbitron font for Streamlit UI and change background to beige
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Orbitron', sans-serif;
        color: white;
        background-color: #F5F5DC;  /* Beige background */
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Orbitron', sans-serif;
        color: #FF69B4;  /* Bright pink titles */
    }
    </style>
    """, unsafe_allow_html=True)

data = {
    'MOST_STREAMED_GAME': [
        'Just Chatting', 'League of Legends', 'Grand Theft Auto V', 'VALORANT', 
        'Casino', 'Fortnite', 'Dota 2', 'Counter-Strike', 'Minecraft', 'Virtual Casino',
        'Just Chatting', 'League of Legends', 'VALORANT', 'Just Chatting', 'Minecraft',
        'Fortnite', 'League of Legends', 'Dota 2', 'Grand Theft Auto V', 'VALORANT'
    ]
}
df_new = pd.DataFrame(data)

# Get the top 10 most streamed games
top_streamed_games = df_new['MOST_STREAMED_GAME'].value_counts().head(10)

# Display the results in Streamlit
st.write("Top 10 Most Streamed Games:")
st.write(top_streamed_games)

# Set the style for the dark background
plt.style.use('dark_background')

# Plot the top 10 most streamed games
fig, ax = plt.subplots(figsize=(10, 6))
top_streamed_games.plot(kind='bar', ax=ax, color='cyan', edgecolor='white')

# Title and labels with white font color for contrast
ax.set_title('Top 10 Most Streamed Games', fontsize=16, color='white')
ax.set_xlabel('Game', fontsize=12, color='white')
ax.set_ylabel('Total Streams', fontsize=12, color='white')

# Set x-axis tick labels to rotate for better readability
ax.tick_params(axis='x', rotation=45, labelcolor='white')

# Remove gridlines (optional for cleaner look)
ax.grid(False)

# Tight layout to ensure elements fit well within the figure
plt.tight_layout()

# Display the plot inline within the Streamlit app
st.pyplot(fig)



