import streamlit as st
import pygwalker as pyg
# Define the navigation menu
pg = st.navigation([
    st.Page("pages/intro.py", title="Intro", icon="🥲"),
    st.Page("pages/analysis.py", title="Analysis", icon="🥳"),
    st.Page("pages/references.py", title=" References", icon="🥳"),
    st.Page("pages/impact.py", title ="Impact", icon ="🥳"),
    st.Page("pages/financial.py", title="Financial", icon="🥲"),
    st.Page("pages/financial_analysis.py", title ="Financial analysis", icon ="🥳"),
    st.Page("pages/genres.py", title ="Genres", icon ="🥳"),
    st.Page("pages/genre.py", title ="Genre", icon ="🥳"),
    st.Page("pages/platform.py", title ="Platform", icon ="🥳")
])

# Run the navigation system
pg.run()