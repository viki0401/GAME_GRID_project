from pygwalker.api.streamlit import StreamlitRenderer
import pygwalker as pyg
import pandas as pd
# import streamlit.components.v1 as components
import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="Using Pygwalker with Streamlit",
    layout="wide"
)

# Add a title
st.title("Using Pygwalker with Streamlit")

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df=pd.read_csv('./data/TwitchDataSet.csv')
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df)


# Embed the generated HTML into the Streamlit app
renderer = get_pyg_renderer()

renderer.explorer()