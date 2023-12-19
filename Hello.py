import streamlit as st
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page 
import utils.page_setup as page_setup

# if 'find_product_reviews' not in st.session_state:
#     st.session_state.find_product_reviews = False

# def click_button():
#     st.session_state.find_product_reviews = True
# st.set_page_config(initial_sidebar_state="collapsed")

# st.session_state.category = False

# if st.session_state['category']:
#     st.session_state.category = False

st.markdown('''# Welcome to SentiLens''')

find_product = st.button('Find your product\'s reviews')

if find_product:
    switch_page('select category')

page_setup.setup_page('home')
# page_setup.reset_session()

