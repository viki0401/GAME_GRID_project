import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.pyplot as plt

# URL of the new CSV file
url_new = "https://storage.googleapis.com/kagglesdsdata/datasets/5093789/8676135/datasetV2.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241209%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241209T121929Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9cc9ab54ff564f1e96b04abca871f41bfd01154e6624d7bdc7dbb7952ef7aa0829da4bb4ffa1f61db23a318121da496d77a1592076510ad9904efc2e8bc37d6292d8ac53aaa58821765c2b02e209bf28b8fc075da00a0e31ab8a59efbd974f09e1b01aec98a22da0d83bb985f4c293f631c2bc9e7f561eb84f43c13bf4fd8693f13632d7c9de3345817ff984e6709df672d9781e3a2ab6b97cfeebce626563048e3a766c2ec966226b50a3e7421b9fac2432745ed0712450e2807a344d848d96ce41d5d18bafb29aea61ad9953b871f588e74cc70248955843525520c6ff8fc2d4a4e8435f3ff32a8bbb9c76ea9b58697939ab47b41c5bfc9c07607a427f22c2"

# Try reading the file with a different encoding (ISO-8859-1)
df_new = pd.read_csv(url_new, encoding='ISO-8859-1')
tab1, tab2, tab3, tab4 = st.tabs(["The most streamed Day", "Top 10 streaming Games", "Top 10 languages", "Z"])
most_active_days = df_new['MOST_ACTIVE_DAY'].value_counts()

# Sort the result from most to least active
most_active_days_sorted = most_active_days.sort_values(ascending=False)
print("Most Active Days:")
print(most_active_days_sorted)

# Create a bar chart with pink color
fig, ax = plt.subplots()

# Create a bar chart and set the color to pink
ax.bar(most_active_days_sorted.index, most_active_days_sorted.values, color='#8A2BE2')  # Pink color

# Add labels and title
ax.set_title("Most Active Days of Streaming", fontsize=16)
ax.set_xlabel("Days", fontsize=12)
ax.set_ylabel("Count", fontsize=12)

# Rotate x-axis labels for better readability if necessary
plt.xticks(rotation=45)

# Optional: Tight layout for better fitting
plt.tight_layout()

# Show the plot using Streamlit
st.pyplot(fig)
plt.style.use('dark_background')




# Assuming df_new is your DataFrame
top_languages = df_new['LANGUAGE'].value_counts().head(10)




# Add a title to your Streamlit page
st.title("Top 10 Languages by Frequency")

# Optional: Add a short description to explain the chart
st.markdown("""
This chart displays the top 10 most common languages used in the dataset.
It shows the frequency of each language, helping to understand the distribution of languages.
""")

# Create a bar chart with skyblue color
fig, ax = plt.subplots(figsize=(10, 6))  # Set the size of the figure

# Plot the top 10 languages with a skyblue color
ax.bar(top_languages.index, top_languages.values, color='skyblue')

# Add labels and title with a more stylish font
ax.set_title("Top 10 Languages by Frequency", fontsize=20, fontweight='bold', color='#2F4F4F')
ax.set_xlabel("Language", fontsize=14, fontweight='bold', color='#2F4F4F')
ax.set_ylabel("Frequency", fontsize=14, fontweight='bold', color='#2F4F4F')

# Customize the x-axis labels with rotation for better readability
plt.xticks(rotation=45, fontsize=12, ha='right')

# Customize the y-axis ticks
ax.tick_params(axis='y', labelsize=12)

# Optional: Add grid lines for better clarity
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout for a cleaner fit
plt.tight_layout()

# Show the plot using Streamlit
st.pyplot(fig)

# URL of the CSV file
url = "https://storage.googleapis.com/kagglesdsdata/datasets/966275/9728664/Twitch_game_data.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241206T180624Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=980ed233b72a7add4ed92aea452b00e270b12451ace11229bf4cf831f4ff46b1d115006c760eeb79656b050415987cc20cd7a14843847022e8ec83cd655098dd7af79deb5bdbe738531ee642b5a6c727bb08aa36e8e84b9aa1463381c61bf5777b64d77a57f9eac672a2426050bf9241e7d82209dda78e10da5eaaf12eed4c72cd4e9d7d62c484cd4692b3c4adf2465ed4b1f47a072fd4e97c57b1971708e2796f864cdabd93db884db984ba9e038732d299d593e49ba8789a3a91e140a5bfa948a29710ab183f48f65d7efe6f260d26ed707b9bb40f3a39c8fe253744f1c1688cf6d2444934651fe300c54989e91d566b29c08f997b7493fb9e65ac49a157df"

# Try reading the file with a different encoding (ISO-8859-1)
df = pd.read_csv(url, encoding='ISO-8859-1')

# Check the first few rows of the dataframe
print(df.head())

# Group by 'Game' and sum the 'Streamers' for each game
top_10_streamers = df.groupby('Game')['Streamers'].sum()

# Sort the games by the total 'Streamers' in descending order and get the top 10
top_10_streamers = top_10_streamers.sort_values(ascending=False).head(10)

# Plot the data
plt.style.use('dark_background')
top_10_streamers.plot(kind='bar', figsize=(10, 6), color='cyan', edgecolor='white')

# Title and labels with white font color for contrast
plt.title('Top 10 Games with the Most Streamers', fontsize=16, color='white')
plt.xlabel('Game', fontsize=12, color='white')
plt.ylabel('Total Streamers', fontsize=12, color='white')

# Set x-axis tick labels to rotate for better readability
plt.xticks(rotation=45, ha='right', color='white')

# Remove gridlines for a cleaner look
plt.grid(False)

# Tight layout to ensure elements fit well within the figure
plt.tight_layout()

# Show the plot
plt.show()




