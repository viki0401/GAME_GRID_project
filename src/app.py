import streamlit as st
# Define the navigation menu
pg = st.navigation([
    st.Page("pages/intro.py", title="Problem Statement", icon="🔸", default=True),
      st.Page("pages/what.py", title="What?", icon="🗣️"),
    st.Page("pages/twitch.py", title ="How?", icon ="🔸"),
     st.Page("pages/timing.py",title ="When?", icon ="🔸"),
     st.Page("pages/recomendation.py",title ="Key Takeaways", icon ="🔑")
])

# Run the navigation system
pg.run()