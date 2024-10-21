import streamlit as st
from streamlit_authenticator.utilities import LoginError

# Quick check of the session state.
st.session_state



try:
    authenticator = st.session_state["authenticator"]
    config = st.session_state["config"]
    authenticator.login(location="unrendered", key="login")
except LoginError:
    st.session_state["authentication_status"] = False
except KeyError:
    st.session_state['authentication_status'] = None
    st.warning("Please log in first.")
except Exception as e:
    st.error(e)    

    
    # try:
    #     authenticator.login()
    #     st.session_state["authenticator"] = authenticator
    #     st.session_state["config"] = config
    # except LoginError as e:
    #     st.error(e)
        
    

# authenticator = st.session_state.authenticator
# name, _, _ = authenticator.login(location='main')
else:
    st.title("Page 1")
