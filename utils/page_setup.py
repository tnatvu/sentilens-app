import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from st_clickable_images import clickable_images

def click_button(category):
    st.session_state.category = category

def custom_sidebar():
    categories = ['Laptop', 'outdoor', 'books', 'food']
    
    with st.sidebar: 
        home_button = st.button('Home')

        # Category buttons
        for x in categories:
            st.button(x, key=f'sb_{x}', on_click=click_button, args=[x])


        clicked = clickable_images(
            [
                "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
                "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
                "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
                "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
                "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
            ],
            titles=[f"Image #{str(i)}" for i in range(5)],
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
            img_style={"margin": "5px", "height": "200px"},
        )
        products = ['Laptop','food','books', 'outdoor']
    
        if clicked>-1:
            st.markdown(f"Image #{clicked}")
            st.markdown(f"Image #{clicked} - {products[clicked]} clicked" if clicked > -1 else "No image clicked")
            click_button(products[clicked])
    
    if home_button:
        # st.session_state.find_product_reviews = False
        st.session_state.category = False
        switch_page('Hello')

            
def no_side_pages():
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

# def reset_state():
#     st.session_state.setdefault

def setup_page(current_page):
    no_side_pages()
    custom_sidebar()
    
    if 'category' not in st.session_state:
        st.write('hello no cate')
        st.session_state.category = False
        
    elif (st.session_state.category != False) & (current_page != 'select item'):
        # st.session_state.category = 'Laptop'
        switch_page('select item')

