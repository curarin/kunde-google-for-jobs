
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

########################################################################
########################################################################
########################################################################
#def check_password():
    """Returns `True` if the user had a correct password."""

#    def login_form():
 #       """Form with widgets to collect user information"""
  #      with st.form("Credentials"):
   #         st.text_input("Username", key="username")
    #        st.text_input("Password", type="password", key="password")
     #       st.form_submit_button("Log in", on_click=password_entered)

    #def password_entered():
    #    """Checks whether a password entered by the user is correct."""
    #    if st.session_state["username"] in st.secrets[
    #        "passwords"
    #    ] and hmac.compare_digest(
    #        st.session_state["password"],
    #        st.secrets.passwords[st.session_state["username"]],
    #    ):
    #        st.session_state["password_correct"] = True
    #        del st.session_state["password"]  # Don't store the username or password.
    #        del st.session_state["username"]
    #    else:
    #        st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    #if st.session_state.get("password_correct", False):
    #    return True

    ## Show inputs for username + password.
    #login_form()
    #if "password_correct" in st.session_state:
    #    st.error("😕 User not known or password incorrect")
    #return False
#if not check_password():
 #   st.stop()
########################################################################
########################################################################
########################################################################
# Main Streamlit app starts here
tab1, tab2 = st.tabs([
    "Step 1: Generate Title |",
    "Step 2: Ping Google"
    ])
with tab1:
    tnd.tnd()
with tab2:
    indexnow.indexnow_api_call()
