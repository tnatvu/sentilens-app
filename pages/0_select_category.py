import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import utils.page_setup as page_setup


page_setup.setup_page('select category')

def click_button(category):
    st.session_state.category = category

with open('css/main.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown('''# Select your product's category:''')

categories = ['Laptop', 'outdoor', 'books', 'food', 'meat', 'sports', 'fashion', 'skincare']

n_columns = 5
col1, col2, col3 = st.columns([1,16,1])

with col2:
    
    
    rounds = len(categories)//n_columns+ 1 if len(categories)%n_columns > 0 else len(categories)//n_columns
    for i in range(0, rounds):
        for j,x in enumerate(st.columns(n_columns)):
            k = i*n_columns + j
            if k < len(categories):
                with x:
                    st.button(categories[k], on_click=click_button, args=[categories[k]])
    

if st.session_state.category:
    switch_page('select item')


