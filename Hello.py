import streamlit as st
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page 
import utils.custom_sidebar as custom_sidebar

if 'select_category' not in st.session_state:
    st.session_state.select_category = False

def click_button():
    st.session_state.select_category = True

st.markdown('''# Welcome to SentiLens''')

st.button('Find your product\'s reviews', on_click=click_button)

if st.session_state.select_category:
    switch_page('select category')

custom_sidebar.custom_sidebar()