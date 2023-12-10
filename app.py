
import streamlit as st
import hmac

import tabs.sidebar as sidebar
import tabs.indexnow as indexnow
import tabs.tnd as tnd

st.set_page_config(
    layout="centered",
    page_title="Google for Jobs Optimization for Hello Jobs | by Paul Herzog",
    initial_sidebar_state="expanded", #collapsed
    page_icon="🤖"
)

with st.sidebar:
    sidebar.sidebar()

tab1, tab2 = st.tabs([
    "Step 1: Generate Title |",
    "Step 2: Ping Google"
    ])
with tab1:
    tnd.tnd()
with tab2:
    indexnow.indexnow_api_call()
