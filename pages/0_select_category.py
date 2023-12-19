import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import utils.page_setup as page_setup

page_setup.setup_page('select category')

def click_button(category):
    st.session_state.category = category



st.markdown('''# Select your product's category:''')

categories = ['Laptop', 'outdoor', 'books', 'food']

for x in categories:
    st.button(x, on_click=click_button, args=[x])

if st.session_state.category:
    switch_page('select item')

