import os
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
st.title("Sales")



#Data Frames selection
if os.name == 'nt': # if its windows
    data = pd.read_csv(rf'C:\Users\tanju\Desktop\Project\GAME_GRID_project\data\games_prepped.csv', low_memory=False)
else:
    data = pd.read_csv("../data/games_prepped.csv", low_memory=False)

df = data[data['year'] != 2024]

df_agg = df.groupby(['year']).agg({'estimated_revenue': 'sum'}).reset_index()
filtered_df =df_agg[(df_agg['year'] >= 2009) & (df_agg['year'] <= 2023)]

count_sorted_df=df["month_year"].value_counts().reset_index().sort_values(by='count',ascending=False)
count_sorted_df[["Month","Year"]]=count_sorted_df["month_year"].str.split("-",expand=True)
split_data_df=count_sorted_df[["Month","Year","count"]]
split_data_df.set_index("Month")

yearly_sum=split_data_df.groupby(["Year"])["count"].sum()
monthly_sum=split_data_df.groupby(["Month"])["count"].sum()

monthly_sum_df=monthly_sum.reset_index().rename(columns={"index": "value", 0: "count"})
yearly_sum_df=yearly_sum.reset_index().rename(columns={"index": "value", 0: "count"})

customOrder=["January","February","March","April","May","June","July","August","September","October","November","December"]
monthly_sum_df["Month"]=pd.Categorical(monthly_sum_df["Month"],categories=customOrder,ordered=True)

monthly_sum_df=monthly_sum_df.sort_values(by="Month")
year_sum_df=yearly_sum_df.sort_values(by="Year")



tab1, tab2, tab3, tab4 = st.tabs(["Yearly Games Released", "Yearly Revenue", "Revenue Trendline", "Monthly Releases"])



#First graphs
fig1 = px.line(year_sum_df, x='Year', y='count', title='Number of games released (1997-2023)')
fig1.update_layout(
    title={'x': 0.5, 'xanchor': 'center'},
    showlegend=False
)
fig1.update_xaxes(
    title='Year',
    showgrid=True, gridcolor='lightgray', gridwidth=1)
fig1.update_yaxes(
    title='Number of games released (K for Thousands)',
    showgrid=True, gridcolor='lightgray', gridwidth=1)


fig2 = px.line(df_agg, x='year', y='estimated_revenue', title='Estimated revenue over all years')
fig2.update_layout(
    title={'x': 0.5, 'xanchor': 'center'},
    showlegend=False
)
fig2.update_xaxes(
    title='Year',
    showgrid=True, gridcolor='lightgray', gridwidth=1
)
fig2.update_yaxes(
    title='Estimated Revenue (B for Billions)',
    showgrid=True, gridcolor='lightgray', gridwidth=1)


fig3 = px.scatter(filtered_df, x='year', y='estimated_revenue',
                 title='Estimated Revenue (2009-2023) with trendline',
                 trendline="ols",
                 color_continuous_scale='Viridis')
fig3.update_layout(
    xaxis_title='Year',
    yaxis_title='Estimated Revenue (B for Billions)',
    title={'x': 0.5, 'xanchor': 'center'},
    showlegend=False
)
fig3.update_xaxes(
    showgrid=True, gridcolor='lightgray', gridwidth=1
)
fig3.update_yaxes(
    showgrid=True, gridcolor='lightgray', gridwidth=1)




fig4 = px.line(monthly_sum_df, x='Month', y='count', title='Number of games released each month over all years')
fig4.update_layout(
    title={'x': 0.5, 'xanchor': 'center'},
    showlegend=False
)
fig4.update_xaxes(
    showgrid=True, gridcolor='lightgray', gridwidth=1
)
fig4.update_yaxes(
    title='Number of games released (Thousands)',
    showgrid=True, gridcolor='lightgray', gridwidth=1)

with tab1:
    st.plotly_chart(fig1)

with tab2:
    st.plotly_chart(fig2)

with tab3:
    st.plotly_chart(fig3)

with tab4:
    st.plotly_chart(fig4)
#st.plotly_chart(fig1)
#st.plotly_chart(fig2)
#st.plotly_chart(fig3)
#st.plotly_chart(fig4)