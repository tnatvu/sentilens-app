import streamlit as st
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page 
import utils.page_setup as page_setup

st.markdown('''# Welcome to SentiLens''')

find_product = st.button('Find your product\'s reviews')

if find_product:
    switch_page('select category')

page_setup.setup_page('home')


