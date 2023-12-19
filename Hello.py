import streamlit as st
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page 
import utils.page_setup as page_setup

with open('css/main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,8,1])

with col2:
    st.markdown("# Welcome to SentiLens! :)") 
    find_product = st.button('Find your product\'s reviews')


if find_product:
    switch_page('select category')

page_setup.setup_page('home')