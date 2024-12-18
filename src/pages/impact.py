import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
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


st.title("| Language  |")
st.image("viki.jpg")
st.markdown(""" Language has a big impact on streaming, affecting how many people watch and interact.                                
                 Streamers who speak popular languages usually reach more people. 
                
            
    However, those using less common languages may have smaller audiences but can build strong, loyal communities.
    Let's take a look at the next graphs to see how this plays out.""")





# Title and description
st.title("| The Influence of Language on Streaming |")
df_new= pd.read_csv('./data/twitch_star.csv')

# Get the top 10 languages
top_languages = df_new['LANGUAGE'].value_counts().head(10)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for top 10 languages
top_languages.plot(kind='bar', color='hotpink', ax=ax)

# Adding title and labels
ax.set_title('| Top 10 Languages by Frequency |', fontsize=16)
ax.set_xlabel('Language', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.tick_params(axis='x', rotation=45)

# Adjust layout for better visualization
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

# URL to the dataset
df_new= pd.read_csv('../GAME.GRID.project/data/twitch_star.csv')

# Group by language and most streamed game, summing up total views
game_language_analysis = df_new.groupby(['LANGUAGE', 'MOST_STREAMED_GAME'])['TOTAL_VIEWS'].sum().unstack().fillna(0)

# Get the total views for each language (sum across all games)
total_views_per_language = game_language_analysis.sum(axis=1).sort_values(ascending=False)

# Select the top 10 most popular languages
top_10_languages = total_views_per_language.head(10)

# Filter the game_language_analysis to only include the top 10 languages
game_language_analysis_top_10 = game_language_analysis.loc[top_10_languages.index]

# Get the total views for each game in the filtered dataset
total_views_per_game = game_language_analysis_top_10.sum(axis=0).sort_values(ascending=False)

# Select the top 10 most popular games from the filtered dataset
top_10_games = total_views_per_game.head(10)

# Filter the data to include only the top 10 games
game_language_analysis_top_10_games = game_language_analysis_top_10[top_10_games.index]

# Transpose the data for better visualization
game_language_analysis_top_10_games = game_language_analysis_top_10_games.T

st.markdown("The top three languages by frequency are English, Russian, and Spanish. This means these languages are the most commonly used in streaming, reaching the largest number of viewers.")


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the data (assumes your DataFrame is already loaded as df_new)
# df_new = pd.read_csv('your_file.csv')  # Uncomment and load your actual data here

# Group by language and most streamed game, summing up total views
game_language_analysis = df_new.groupby(['LANGUAGE', 'MOST_STREAMED_GAME'])['TOTAL_VIEWS'].sum().unstack().fillna(0)

# Get the total views for each language (sum across all games)
total_views_per_language = game_language_analysis.sum(axis=1).sort_values(ascending=False)

# Select the top 10 most popular languages
top_10_languages = total_views_per_language.head(10)

# Filter the game_language_analysis to only include the top 10 languages
game_language_analysis_top_10 = game_language_analysis.loc[top_10_languages.index]

# Get the total views for each game in the filtered dataset
total_views_per_game = game_language_analysis_top_10.sum(axis=0).sort_values(ascending=False)

# Select the top 10 most popular games from the filtered dataset
top_10_games = total_views_per_game.head(10)

# Filter the data to include only the top 10 games
game_language_analysis_top_10_games = game_language_analysis_top_10[top_10_games.index]

# Transpose the data for better visualization
game_language_analysis_top_10_games = game_language_analysis_top_10_games.T

# Define custom electro color palette (neon-like colors)
electro_colors = ['#362730',  # Dark brownish-purple
                  '#4682B4',  # Muted grayish-blue
                  '#5733FF',  # Electric blue
                  '#FEF433',  # Bright yellow
                  '#BCB369',  # Dark teal
                  '#4E4151',  # Soft purple-gray
                  '#FF83C1',  # Hot pink
                  '#8D6E63',  # Warm brownish-pink
                  '#33FFBB',  # Bright turquoise green
                  '#F25930']  # Bright coral-orange

# Identify the most popular game (the one with the highest total views)
most_popular_game = game_language_analysis_top_10_games.sum(axis=1).idxmax()

# Streamlit app layout
st.title("Top 10 Most Popular Games by Top 10 Languages")
st.write("This chart visualizes the top 10 most popular games by the top 10 languages on Twitch.")

# Plot the top 10 games by the top 10 languages using a stacked bar plot
fig, ax = plt.subplots(figsize=(12, 8))
game_language_analysis_top_10_games.plot(kind='bar', stacked=True, color=electro_colors, ax=ax)

# Highlight the most popular game with color #FF007F
for i, bar in enumerate(ax.patches):
    # Find which bar belongs to the most popular game
    if game_language_analysis_top_10_games.index[i // len(game_language_analysis_top_10_games.columns)] == most_popular_game:
        bar.set_facecolor('#FF007F')  # Set color for the most popular game

# Add titles and labels
ax.set_title('Top 10 Most Popular Games by Top 10 Languages', fontsize=16)
ax.set_xlabel('Game', fontsize=12)
ax.set_ylabel('Total Views', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.legend(title='Language', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot in Streamlit
st.pyplot(fig)




st.markdown("Let's take a look at how many followers are gained per stream by language. This analysis will help us understand which languages are leading in follower growth. By examining this, we can see which language communities are growing the fastest in terms of engagement.")

# Title for Streamlit app
st.title("| Followers Gained Per Stream by Language |")

# Create the box plot manually using Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))

languages = df_new['LANGUAGE'].unique()
data = [df_new[df_new['LANGUAGE'] == language]['FOLLOWERS_GAINED_PER_STREAM'].dropna() for language in languages]
# Boxplo
ax.boxplot(data, labels=languages, patch_artist=True, boxprops=dict(facecolor='hotpink', color='hotpink'))
# Customize the plot
ax.set_title('Followers Gained Per Stream by Language', fontsize=16)
ax.set_xlabel('Language', fontsize=12)
ax.set_ylabel('Followers Gained Per Stream', fontsize=12)
ax.tick_params(axis='x', rotation=45)
# Display the plot in Streamlit
st.pyplot(fig)
st.markdown("""In conclusion, English has become the dominant language in the streaming world, shaping the global landscape of streaming platform. As the most widely spoken second language, it allows streamers to connect with audiences across continents, making it essential for those seeking to grow their reach and engage with the largest viewer base. By using English, streamers can access more sponsorships, collaborations, and exposure, which leads to greater success.

The language's influence extends beyond just communication—it fosters a shared cultural space where trends, memes, and communities thrive globally. While regional languages are growing, English remains the key to unlocking the widest audience and driving the streaming industry forward. Its role is integral to the ongoing evolution of digital entertainment, connecting people worldwide and shaping content creation.""")

