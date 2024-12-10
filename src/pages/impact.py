import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


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
st.title("The Impact of Twitch on Sales")
st.markdown("This is the description of the title")

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt
import seaborn as sns
# URL of the CSV file
import numpy as np # linear algebra
import matplotlib.pyplot as plt
import seaborn as sns

# URL of the new CSV file
url_new = "https://storage.googleapis.com/kagglesdsdata/datasets/5093789/8676135/datasetV2.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241209%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241209T121929Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9cc9ab54ff564f1e96b04abca871f41bfd01154e6624d7bdc7dbb7952ef7aa0829da4bb4ffa1f61db23a318121da496d77a1592076510ad9904efc2e8bc37d6292d8ac53aaa58821765c2b02e209bf28b8fc075da00a0e31ab8a59efbd974f09e1b01aec98a22da0d83bb985f4c293f631c2bc9e7f561eb84f43c13bf4fd8693f13632d7c9de3345817ff984e6709df672d9781e3a2ab6b97cfeebce626563048e3a766c2ec966226b50a3e7421b9fac2432745ed0712450e2807a344d848d96ce41d5d18bafb29aea61ad9953b871f588e74cc70248955843525520c6ff8fc2d4a4e8435f3ff32a8bbb9c76ea9b58697939ab47b41c5bfc9c07607a427f22c2"

# Try reading the file with a different encoding (ISO-8859-1)
df_new = pd.read_csv(url_new, encoding='ISO-8859-1')

# Check the first few rows of the new dataframe
print(df_new.head())
top_streamed_games = df_new['MOST_STREAMED_GAME'].value_counts().head(10)

# Display the results
print("Top 10 Most Streamed Games:")
print(top_streamed_games)
plt.style.use('dark_background')

# Plot the top 10 most streamed games
top_10_games.plot(kind='bar', figsize=(10, 6), color='cyan', edgecolor='white')

# Title and labels with white font color for contrast
plt.title('Top 10 Most Streamed Games', fontsize=16, color='white')
plt.xlabel('Game', fontsize=12, color='white')
plt.ylabel('Total Hours Streamed', fontsize=12, color='white')

# Set x-axis tick labels to rotate for better readability
plt.xticks(rotation=45, ha='right', color='white')

# Remove gridlines (optional for cleaner look)
plt.grid(False)

# Tight layout to ensure elements fit well within the figure
plt.tight_layout()

# Show the plot
plt.show()



