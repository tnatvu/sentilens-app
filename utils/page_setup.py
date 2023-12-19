import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from st_clickable_images import clickable_images
import pandas as pd

def click_button(category):
    st.session_state.category = category
    if (st.session_state.category != False) & (st.session_state.current_page not in ('select item')):
        switch_page('select item')
    elif (st.session_state.category != False) & (st.session_state.current_page =='item'):
        st.write(st.session_state.current_page)
        switch_page('select item')
        
def custom_sidebar():
    categories = pd.DataFrame({'category': ['Laptop', 'outdoor', 'food', 'books']
                              ,'url': ["https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700"
                                       ,"https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700"
                                       ,"https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700"
                                       ,"https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700"
                                       ]})
    
    
    with st.sidebar: 
        home_button = st.button('Home')

        clicked = clickable_images(list(categories['url']),
            titles=[categories['category'][i] for i in range(len(categories))],
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
            img_style={"margin": "5px", "height": "100px", 'width':'100px'},
        )
        
    
        if clicked>-1:
            st.markdown(f"Image #{clicked}")
            st.markdown(f"Image #{clicked} - {categories['category'][clicked]} clicked" if clicked > -1 else "No image clicked")
            click_button(categories['category'][clicked])
    
    if home_button:
        st.session_state.category = False
        switch_page('Hello')

            
def no_side_pages():
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)


def setup_page(current_page):
    no_side_pages()
    custom_sidebar()
    st.session_state.current_page = current_page
    if 'category' not in st.session_state:
        st.session_state.category = False
       