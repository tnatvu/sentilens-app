import streamlit as st
from streamlit_extras.switch_page_button import switch_page 


if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button(cat):
    st.session_state.clicked = True
    st.session_state.category = cat

st.markdown('# Select product categories:')

categories = ['laptop', 'outdoor', 'books', 'food']

for x in categories:
    st.button(x, on_click=click_button, args=[x])
# st.button('Food', on_click=click_button, args=['Food'])

if st.session_state.clicked:
    switch_page('category')