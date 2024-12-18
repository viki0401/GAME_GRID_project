import streamlit as st
import pandas as pd
import plotly as plt
import matplotlib.pyplot as plt

import altair as alt
import streamlit as st
# Load the data
st.title("What?")
st.markdown("""What refers to picking the best game for streaming based on popularity, competition, whether it’s an esports game, and how well it engages viewers. On Twitch, choosing the right game can affect how many people see your stream, as popular esports games usually have large audiences and regular tournaments. However, highly competitive games can make it harder to stand out unless you have something unique to offer. Picking the right game is important for growing your channel and building a loyal community that keeps returning.""")
df_new = pd.read_csv('./data/twitch_star.csv')
st.title("Top 50 Streamed Games")
# Group by 'MOST_STREAMED_GAME' and sum the 'TOTAL_TIME_STREAMED'
top_streamed_games = df_new.groupby('MOST_STREAMED_GAME')['TOTAL_TIME_STREAMED'].sum().sort_values(ascending=False)
# Select top 50 games and reset index for use in Altair
top_50_games = top_streamed_games.head(50).reset_index()
# Create the bar chart using Altair
bars = alt.Chart(top_50_games).mark_bar().encode(
    x=alt.X('TOTAL_TIME_STREAMED:Q', title='Total Time Streamed (hours)', scale=alt.Scale(domain=[0, top_streamed_games.max()])),
    y=alt.Y('MOST_STREAMED_GAME:N', sort='-x', title='Game'),
    tooltip=['MOST_STREAMED_GAME:N', 'TOTAL_TIME_STREAMED:Q']
).properties(
    width=800,
    height=600 
)

# Display the chart in Streamlit
st.altair_chart(bars, use_container_width=True)
st.markdown("Displaying the top 50 games helps us identify trends in what’s popular, even though the game names might be small. It gives a clear picture of which titles are dominating the streams and how preferences are shifting. By showing such a large range, we can better understand the diversity of content being watched, while also highlighting the dominant games that stand out in terms of popularity.")
st.markdown("""
### Do Some of the Top Streamed Games Belong to the Esports World?
""")
st.image("monkey.jpg")



st.markdown("""


Esports is just like regular sports, but instead of kicking a ball or running on a field, players compete in video games. 

These players or teams are super skilled, and they play in organized tournaments or leagues, just like football or basketball players. 

It’s competitive gaming, with tons of fans watching live on streams or at big events! And just like traditional sports, players can win a lot of money from prizes, sponsorships, and streaming.
""")

st.markdown("""
**Esports Games:**
- Counter-Strike (e.g., CS:GO) 🎮
- League of Legends 🏆
- Apex Legends 🔫
- Overwatch 🌟
- PUBG (PlayerUnknown's Battlegrounds) 🏃‍♂️
- Valorant 🕹️
- World of Warcraft (WoW) 🧙‍♂️
- Teamfight Tactics (TFT) ♟️
- Dota 2 ⚔️ """)


import pandas as pd
import altair as alt
import streamlit as st

# Load the dataset
df_new = pd.read_csv('./data/twitch_star.csv')

# Get the top 10 most streamed games based on the total time streamed
top_10_streamed_games = df_new.groupby('MOST_STREAMED_GAME')['TOTAL_TIME_STREAMED'].sum().sort_values(ascending=False).head(10)

# Get the total hours streamed for the top 10 games
total_hours = top_10_streamed_games.sum()

# Calculate the percentage of total hours streamed for each game
percentage_streamed = (top_10_streamed_games / total_hours) * 100

# Create a DataFrame to hold the games and their corresponding percentages
top_10_percentage_df = pd.DataFrame({
    'Game': top_10_streamed_games.index,
    'Total Time Streamed (Hours)': top_10_streamed_games.values,
    'Percentage of Total Streamed Time (%)': percentage_streamed.values
}).reset_index(drop=True)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Assuming df_new is your dataset
df_new = pd.read_csv('./data/twitch_star.csv')  # Load your dataset

# Group by 'MOST_STREAMED_GAME' and calculate the total time streamed for each game
top_streamed_games = df_new.groupby('MOST_STREAMED_GAME')['TOTAL_TIME_STREAMED'].sum().sort_values(ascending=False)

# Extract the top 10 games
top_10_games_df = top_streamed_games.head(10).reset_index()
top_10_games_df.columns = ['Game', 'Hours_Streamed']  # Rename columns

# Calculate the total hours for the top 10 games
top_10_total_hours = top_10_games_df['Hours_Streamed'].sum()

# Calculate the percentage for each game
top_10_games_df['Percentage'] = (top_10_games_df['Hours_Streamed'] / top_10_total_hours) * 100
top_10_games_df['Percentage'] = top_10_games_df['Percentage'].round(1)  # Round to 1 decimal

# Prepare data for the pie chart
labels = top_10_games_df['Game']
sizes = top_10_games_df['Hours_Streamed']
explode = [0.1 if i == 1 else 0 for i in range(len(sizes))]  # Explode the second slice (Just Chatting)

# Create a pie chart using matplotlib
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90,
        shadow=True, colors=plt.cm.Paired.colors)  # Use a color palette for better distinction
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart in Streamlit
st.write("### Top 10 Most Streamed Games by Total Time Streamed in %")
st.pyplot(fig1)

st.markdown(""" As you can see, "Just Chatting" ranks as the number one category compared to other games. 

After "Just Chatting," **League of Legend** holds the second spot, continuing to be a major game in the competitive scene. Its esports tournaments are still going strong, and the game's changing strategies keep both players and viewers interested.

In third place is **Grand Theft Auto V (GTA V)**, which stays popular because of its massive online mode, "GTA Online." Players have fun causing chaos and interacting with each other in the large world of Los Santos, making it a top pick for both fun and interactive gameplay.

These categories show how Twitch offers a variety of content that appeals to all kinds of viewers, whether they prefer chatting, competitive gaming, or roleplaying in open worlds. 

**But what exactly is "Just Chatting" on Twitch, and why has it taken the platform by storm?**
            
        
""")





st.image("love.png")
st.markdown("""
## 🎙️ What is "Just Chatting" on Twitch?  
        

On Twitch, **"Just Chatting"** is when streamers focus on interacting with their viewers rather than playing games. It’s like hanging out online with friends! Sometimes there’s no gaming at all, or gaming takes a back seat to the conversation.  

---

### 🔹 Examples of “Just Chatting” Content:
- **🗣️ Talking About Life**: Sharing stories, answering questions, or discussing trending topics.  
- **🍳 Cooking or Hobbies**: Streaming live cooking, drawing, or working on creative projects while chatting.  
- **❓ Q&A Sessions**: Letting viewers ask questions and creating a personal connection.  
- **🎮 Casual Gaming**: Playing simple games while chatting and reacting to the audience.  
- **🎉 Fun Activities**: Watching videos, hosting party games, or even live-streaming travel adventures.  

---
""")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import streamlit as st

# Load your data (replace with your actual data file)
df_new = pd.read_csv('./data/twitch_star.csv')

# Filter data for "Just Chatting" and other games
just_chatting = df_new[df_new["MOST_STREAMED_GAME"] == "Just Chatting"]
other_games = df_new[df_new["MOST_STREAMED_GAME"] != "Just Chatting"]

# Sort by RANK as a proxy for time progression
just_chatting = just_chatting.sort_values("RANK")
other_games = other_games.sort_values("RANK")

# Calculate cumulative views as a trend metric
just_chatting["CUMULATIVE_VIEWS"] = just_chatting["TOTAL_VIEWS"].cumsum()
other_games["CUMULATIVE_VIEWS"] = other_games["TOTAL_VIEWS"].cumsum()

# Streamlit app title and description
st.title("Trend of 'Just Chatting' vs Other Games Over Rank")
st.write("""
    This visualization compares the cumulative views for 'Just Chatting' 
    and other games, based on the rank as a proxy for time progression.
""")

# Plot the trend for Just Chatting vs Other Games
plt.figure(figsize=(12, 6))
plt.plot(just_chatting["RANK"], just_chatting["CUMULATIVE_VIEWS"], label="Just Chatting", color='darkorchid', marker='o', linewidth=2)
plt.plot(other_games["RANK"], other_games["CUMULATIVE_VIEWS"], label="Other Games", color='black', marker='o', linewidth=2)

# Customize the plot

plt.xlabel("Rank (Proxy for Time Progression)", fontsize=12)
plt.ylabel("Cumulative Views", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot in Streamlit
st.pyplot(plt)

# Get top 10 games based on total hours streamed
top_streamed_games = df_new.groupby('MOST_STREAMED_GAME')['TOTAL_TIME_STREAMED'].sum().sort_values(ascending=False).head(10)

# Convert to DataFrame for pie chart
top_10_games_df = top_streamed_games.reset_index()
top_10_games_df.columns = ['Game', 'Total_Hours_Streamed']

# Create pie chart with Altair for top 10 games based on hours streamed
pie_chart = alt.Chart(top_10_games_df).mark_arc().encode(
    theta=alt.Theta(field='Total_Hours_Streamed', type='quantitative', title="Total Hours Streamed"),
    color=alt.Color(field='Game', type='nominal', legend=alt.Legend(title="Game")),
    tooltip=[
        alt.Tooltip('Game:N', title='Game'),
        alt.Tooltip('Total_Hours_Streamed:Q', title='Total Hours Streamed')
    ]
).properties(
    title="Top 10 Most Streamed Games by Total Hours Streamed"
)
st.title("🤝 **Why It’s Popular?**")  
st.markdown("**'Just Chatting'** is all about building connections in a fun, relaxed way—whether gaming is part of it or not! It's the ultimate mix of entertainment and community-building.")  
st.markdown("'Just Chatting' has stable viewership, growing steadily without major fluctuations. This indicates that it has reached a point of consistent popularity, unlike other games that still experience shifts in audience interest.")

st.page_link("pages/twitch.py", icon= "🗣️",label="Next Page", help="Navigate to the next page", disabled=False)