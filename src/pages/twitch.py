import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

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




# Read the data
df_new = pd.read_csv('./data/twitch_star.csv')
st.image("zebra.jpeg")
st.title(""""Do Smaller Languages Hold the Key to Streaming Success? Top 100 vs.1000""")
st.markdown (""" When we analyze the top 100 streamers versus the top 1000, one question stands out: do language preferences and trends follow the same patterns in both groups? Are smaller languages, which are less common among top streamers, a barrier to growth, or can they still offer a chance for success?

By examining language distribution, we can see how larger languages like English dominate the top 100, but what about the top 1000? Are there notable differences in the types of languages used, and how do these trends affect the chances of breaking into the top 1000? Let's dive into these language trends to understand how they shape the streaming landscape for both the elite and aspiring streamers.""")
# Sort the dataframe by 'TOTAL_FOLLOWERS' to get the top 1000 streamers
top_1000_streamers = df_new.nlargest(1000, 'TOTAL_FOLLOWERS')

# Count the number of streamers for each language in the top 1000
language_counts_1000 = top_1000_streamers['LANGUAGE'].value_counts()

# Calculate the percentage for each language
language_percentages = (language_counts_1000 / language_counts_1000.sum()) * 100

# Group languages with less than 2.8% into 'Others'
others = language_counts_1000[language_percentages < 2.8].sum()
language_counts_1000_filtered = language_counts_1000[language_percentages >= 2.8]

# Add the 'Others' category
language_counts_1000_filtered['Others'] = others

# Get the languages that were grouped into "Others" and their percentages
others_languages = language_percentages[language_percentages < 2.8].sort_values(ascending=False)

# Streamlit: Show pie chart with custom labels and percentages
st.title("Languages Used by Top 1000 Streamers")

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(language_counts_1000_filtered, labels=language_counts_1000_filtered.index, autopct='%1.1f%%', 
       colors=sns.color_palette('viridis', len(language_counts_1000_filtered)), startangle=140)

# Title for the pie chart
ax.set_title('Languages Used by Top 1000 Streamers', fontsize=16)

# Display the pie chart
st.pyplot(fig)
st.markdown("From the pie charts, we can see that English dominates, with Spanish and Russian not too far behind. The 'Others' category groups together the smaller languages.")

import streamlit as st

# Example data for 'others_languages'
others_languages = {
    'Polish': 1.80,
    'Italian': 1.30,
    'Turkish': 0.70,
    'Thai': 0.50,
    'Czech': 0.30,
    'Ukrainian': 0.30,
    'Korean': 0.20,
    'Cantonese': 0.20,
    'Hungarian': 0.10,
    'Arabic': 0.10,
    'Romanian': 0.10
}

# Display subheader
st.subheader("Languages Included in 'Others' (less than 2.8%):")

# Create two columns to display the languages and percentages neatly
col1, col2 = st.columns(2)

# Display the languages and percentages in the two columns
with col1:
    for lang in others_languages.keys():
        st.write(f"**{lang}**")
        
with col2:
    for perc in others_languages.values():
        st.write(f"{perc:.2f}%")


# Load your dataset (make sure your path to the CSV is correct)
df_new = pd.read_csv('./data/twitch_star.csv')
st.write("This pie chart shows the distribution of languages used by the top 100 streamers based on total followers.")
# Sort the dataframe by 'TOTAL_FOLLOWERS' to get the top 100 streamers
top_100_streamers = df_new.nlargest(100, 'TOTAL_FOLLOWERS')

# Count the number of streamers for each language in the top 100
language_counts = top_100_streamers['LANGUAGE'].value_counts()

# Create a pie chart with Matplotlib
plt.figure(figsize=(8, 8))
plt.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', 
        colors=sns.color_palette('viridis', len(language_counts)), startangle=140)

# Add title to the pie chart
plt.title('Languages Used by Top 100 Streamers', fontsize=16)

# Show the pie chart in Streamlit
st.pyplot(plt)


# Optionally, add some descriptive text or analysis

st.markdown("""          
            Smaller languages like Polish or Turkish do have dedicated audiences, but they often face limitations in terms of global reach. Streamers using these languages typically have a more localized following, which can make it harder for them to gain traction internationally. The pool of potential viewers is smaller compared to languages like English, which is used by audiences from all around the world.

As a result, Polish or Turkish streamers may find it more challenging to grow a large, diverse audience, especially if their content is focused on specific regional interests. They may also face difficulties in securing international sponsorships, which often prefer streamers who can reach a broader, global market. However, despite these challenges, streamers in smaller languages can build strong, loyal communities within their regions, where they have the advantage of creating deeper connections with viewers who share similar cultural backgrounds.Smaller languages tend to have a more limited audience, which makes it harder for streamers to grow a substantial following.""")



