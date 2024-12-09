import streamlit as st
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

# Title and description
st.title("The Impact of Twitch on Sales")
st.markdown("This is the description of the title")

import pandas as pd
import plotly.graph_objects as go


url = "https://storage.googleapis.com/kagglesdsdata/datasets/966275/9728664/Twitch_game_data.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241206T180624Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=980ed233b72a7add4ed92aea452b00e270b12451ace11229bf4cf831f4ff46b1d115006c760eeb79656b050415987cc20cd7a14843847022e8ec83cd655098dd7af79deb5bdbe738531ee642b5a6c727bb08aa36e8e84b9aa1463381c61bf5777b64d77a57f9eac672a2426050bf9241e7d82209dda78e10da5eaaf12eed4c72cd4e9d7d62c484cd4692b3c4adf2465ed4b1f47a072fd4e97c57b1971708e2796f864cdabd93db884db984ba9e038732d299d593e49ba8789a3a91e140a5bfa948a29710ab183f48f65d7efe6f260d26ed707b9bb40f3a39c8fe253744f1c1688cf6d2444934651fe300c54989e91d566b29c08f997b7493fb9e65ac49a157df"
