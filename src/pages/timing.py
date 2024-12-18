
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
df_new= pd.read_csv('./data/twitch_star.csv')
st.title("Being in the Right Place at the Right Time")
st.markdown ("""Let's explore if any trends emerge in terms of which days are the most effective for streamers, helping them engage with viewers, attract more followers, and optimize their streaming schedule""")
# Define the custom order for the days of the week
import streamlit as st


from streamlit.components.v1 import html
import time





days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Step 1: Analyze MOST_ACTIVE_DAY
active_day_counts = df_new['MOST_ACTIVE_DAY'].value_counts()
active_day_counts = active_day_counts[days_order]  # Reorder counts based on days_order

# Step 2: Analyze DAY_WITH_MOST_FOLLOWERS_GAINED
followers_day_counts = df_new['DAY_WITH_MOST_FOLLOWERS_GAINED'].value_counts()
followers_day_counts = followers_day_counts[days_order]  # Reorder counts based on days_order

# Step 3: Plot the results
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Subplot 1: Most Active Days
sns.barplot(x=active_day_counts.index, y=active_day_counts.values, palette='rocket', ax=axes[0])
axes[0].set_title('Most Active Days', fontsize=16)
axes[0].set_xlabel('Day of the Week', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].tick_params(axis='x', rotation=45)

# Subplot 2: Days with Most Followers Gained
sns.barplot(x=followers_day_counts.index, y=followers_day_counts.values, palette='rocket', ax=axes[1])
axes[1].set_title('Days with Most Followers Gained', fontsize=16)
axes[1].set_xlabel('Day of the Week', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

# Optionally display some additional info
st.write("""The above graphs show the distribution of the most active days and the days when streamers gained the most followers.""")
st.markdown("""During the middle of the week, especially on Tuesday and Wednesday, people seem to have more time for exploring content.
              On Sundays, they tend to be more focused on following new streamers. This shift shows that people are more engaged with content during the week, but Sundays are more about following and connecting.""")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df_new is already loaded in your environment
# Step 1: Identify the top 3 languages
top_5_languages = df_new['LANGUAGE'].value_counts().head(5).index

# Step 2: Filter the data to include only rows with these top 3 languages
filtered_data = df_new[df_new['LANGUAGE'].isin(top_5_languages)]

# Step 3: Convert 'MOST_ACTIVE_DAY' to a categorical type with the correct order (Monday to Sunday)
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
filtered_data['MOST_ACTIVE_DAY'] = pd.Categorical(filtered_data['MOST_ACTIVE_DAY'], categories=days_order, ordered=True)

# Step 4: Count the occurrences of each language by day of the week
language_day_counts = filtered_data.groupby(['MOST_ACTIVE_DAY', 'LANGUAGE'], observed=True).size().reset_index(name='count')


# Step 5: Plot the data
plt.figure(figsize=(10, 6))
sns.barplot(x='MOST_ACTIVE_DAY', y='count', hue='LANGUAGE', data=language_day_counts, palette='rocket')

# Add titles and labels
plt.title('Top 5 Languages Streamed by Day of the Week', fontsize=16)
plt.xlabel('Day of the Week', fontsize=12)
plt.ylabel('Number of Streamers', fontsize=12)
plt.xticks(rotation=45)

# Display the plot in Streamlit
st.pyplot(plt)

st.markdown("""This graph shows the streaming activity for the top 5 languages: English, Japanese, Russian, Spanish, and Portuguese, across different days of the week. 
            English dominates the graph with extremely high streaming activity compared to the other languages.
             Japanese, in contrast, has relatively low activity levels throughout the week, indicating a smaller streaming audience. 
            Russian, while not as dominant as English, shows more consistent activity, likely due to the influence of post-Soviet countries. 
            However, this trend may decrease over time as regional preferences shift. 
            Portuguese displays a steady presence, with specific peaks on certain days, indicating strong engagement from millions of viewers.
             Spanish also shows significant activity, driven by the large Latin American audience. 
            Overall, the graph highlights the global reach of English, while other languages like Russian and Portuguese exhibit significant but more localized engagement patterns.""")