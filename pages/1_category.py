# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from streamlit_extras.switch_page_button import switch_page 

import utils.custom_sidebar as custom_sidebar

custom_sidebar.custom_sidebar()

st.session_state.select_category = False
st.session_state.category_clicked = False

if 'category' not in st.session_state:
    st.session_state.category = 'Laptop' # Default

cat = st.session_state.category

st.write(f'# Pick one item in *{st.session_state.category}*:')
# Load all products from this category
items = {'Laptop':['laptop 1', 'laptop 2'],
         'food': ['food 1', 'food 2']}

if 'item' not in st.session_state:
    st.session_state.item = 'laptop 1'

def item_selected():
    st.session_state.item = option
    st.session_state.item_selected = True
    # st.write('Hello tina')
    
if 'item_selected' not in st.session_state:
    st.session_state.item_selected = False

option = st.selectbox(
    'Pick a product',
    items[cat],
    on_change=item_selected,
    )

if st.session_state.item_selected:
    switch_page('item')

st.write('Item page - You selected:', option)



