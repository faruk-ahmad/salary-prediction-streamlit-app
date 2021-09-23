import streamlit as st

# this will change the default page title
st.set_page_config(page_title="Salary Prediction", page_icon=None, layout="wide", initial_sidebar_state="auto")

from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))

if page == "Explore":
    show_explore_page()
else:
    show_predict_page()