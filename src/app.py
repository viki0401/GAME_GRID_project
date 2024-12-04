import streamlit as st

# Define the navigation menu
pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon="🏠"),
    st.Page("pages/intro.py", title="Intro", icon="🥲"),
    st.Page("pages/second.py", title="Second", icon="🥳"),
    st.Page("pages/third.py", title ="Third", icon ="🥳")
])

# Run the navigation system
pg.run()