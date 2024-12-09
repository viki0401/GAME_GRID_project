import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Set the font to 'sans-serif' to avoid issues with unsupported fonts like 'Courier New'
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
st.title("Genres Playtime Sales")

tab1, tab2 = st.tabs(["Playtime across Genres", "Playtime of age restricted games across Genres"])


#read the datafram
df = pd.read_csv(rf'C:\Users\tanju\Desktop\Project\GAME_GRID_project\data\games_prepped.csv', low_memory=False)
data = df[df['year'] != 2024]


#grouping some data
genre1_playtime = data.groupby('Genre_1')['average_playtime_forever_in_hours'].sum().sort_values(ascending=False)
genre2_playtime = data.groupby('Genre_2')['average_playtime_forever_in_hours'].sum().sort_values(ascending=False)
genre3_playtime = data.groupby('Genre_3')['average_playtime_forever_in_hours'].sum().sort_values(ascending=False)
genre4_playtime = data.groupby('Genre_4')['average_playtime_forever_in_hours'].sum().sort_values(ascending=False)


combined_data = {
    'Genre': list(genre1_playtime.keys()) + list(genre2_playtime.keys()) +
             list(genre3_playtime.keys()) + list(genre4_playtime.keys()),
    'Playtime': list(genre1_playtime.values) + list(genre2_playtime.values) +
                list(genre3_playtime.values) + list(genre4_playtime.values)
}

df_combined = pd.DataFrame(combined_data)
major_genres = ["Action", "Indie", "RPG", "Adventure", "Simulation", "Casual", "Strategy"]
df_combined['Genre'] = df_combined['Genre'].apply(lambda x: x if x in major_genres else 'Others')
df_final = df_combined.groupby('Genre', as_index=False).agg({'Playtime': 'sum'})

#first plot
fig = px.pie(
    df_final, 
    names='Genre', 
    values='Playtime', 
    title="Average Playtime Distribution Across Genres (with 'Others')",
    color_discrete_sequence=px.colors.qualitative.Set3
)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(height=700, width=700)

#st.plotly_chart(fig)




grouped_1 = data.groupby(['Genre_1', 'required_age'], as_index=False)['average_playtime_forever_in_hours'].sum()
grouped_1.rename(columns={
    'Genres_1': 'Genre_1',
    'required_age': 'Age Restriction',
    'average_playtime_forever_in_hours': 'Average Playtime (Forever)'
}, inplace=True)

grouped_2 = data.groupby(['Genre_2', 'required_age'], as_index=False)['average_playtime_forever_in_hours'].sum()
grouped_2.rename(columns={
    'Genres_2': 'Genre_2',
    'required_age': 'Age Restriction',
    'average_playtime_forever_in_hours': 'Average Playtime (Forever)'
}, inplace=True)

grouped_3 = data.groupby(['Genre_3', 'required_age'], as_index=False)['average_playtime_forever_in_hours'].sum()
grouped_3.rename(columns={
    'Genres_3': 'Genre_3',
    'required_age': 'Age Restriction',
    'average_playtime_forever_in_hours': 'Average Playtime (Forever)'
}, inplace=True)

grouped_4 = data.groupby(['Genre_4', 'required_age'], as_index=False)['average_playtime_forever_in_hours'].sum()
grouped_4.rename(columns={
    'Genres_4': 'Genre_4',
    'required_age': 'Age Restriction',
    'average_playtime_forever_in_hours': 'Average Playtime (Forever)'
}, inplace=True)





grouped_1['Genre_Level'] = 'Genre_1'
grouped_2['Genre_Level'] = 'Genre_2'
grouped_3['Genre_Level'] = 'Genre_3'
grouped_4['Genre_Level'] = 'Genre_4'

# Rename genre columns to a common name for consistency
grouped_1 = grouped_1.rename(columns={'Genre_1': 'Genre'})
grouped_2 = grouped_2.rename(columns={'Genre_2': 'Genre'})
grouped_3 = grouped_3.rename(columns={'Genre_3': 'Genre'})
grouped_4 = grouped_4.rename(columns={'Genre_4': 'Genre'})

# Combine all the grouped DataFrames
combined_grouped = pd.concat([grouped_1, grouped_2, grouped_3, grouped_4])

# Rename columns for clarity
combined_grouped = combined_grouped.rename(
    columns={'average_playtime_forever_in_hours': 'Average Playtime (Forever)', 
             'required_age': 'Age Restriction'})

combined_grouped_sorted = combined_grouped.sort_values(by=['Genre', 'Age Restriction'], ascending=[True, True])

# Create the stacked bar plot
fig2 = px.bar(
    combined_grouped_sorted, 
    x='Genre', 
    y='Average Playtime (Forever)', 
    color='Age Restriction', 
    barmode='stack',  
    title='Impact of Age Restrictions on Average Playtime Across Genres'
)

# Update axes and layout
fig2.update_xaxes(categoryorder='total descending')  # Keep sorting of total bar heights
fig2.update_layout(
    xaxis_title='Genre', 
    yaxis_title='Average Playtime (Forever)',
    legend_title='Age Restriction',
    xaxis_tickangle=45,
    height=600,
    width=1200
)

#st.plotly_chart(fig2)

with tab1:
    st.plotly_chart(fig)

with tab2:
    st.plotly_chart(fig2)