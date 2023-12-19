import streamlit as st
from streamlit_extras.switch_page_button import switch_page 


def select_cat(cat):
    st.session_state.select_category = True
    st.session_state.category_clicked = True
    st.session_state.category = cat


def custom_sidebar():
    categories = ['Laptop', 'outdoor', 'books', 'food']

    with st.sidebar: 
        for x in categories:
            st.button(x, key=f'sb_{x}', on_click=select_cat, args=[x])

if 'category_clicked' not in st.session_state:
    st.session_state.select_category = False
    st.session_state.category_clicked = False

if st.session_state.category_clicked:
    switch_page('category')
    