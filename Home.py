import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import LoginError
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Home")
st.title("Streamlit-Authenticator")
st.write("Multi-Page App")
st.write("https://github.com/mkhorasani/Streamlit-Authenticator")

st.write("Login with the following credentials:")
st.code("Username: brian\nPassword: password")

# Load credentials from the YAML file
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize the authenticator
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

# Store the authenticator object in the session state
st.session_state["authenticator"] = authenticator
# Store the config in the session state so it can be updated later
st.session_state["config"] = config

# Authentication logic
try:
    authenticator.login()
except LoginError as e:
    st.error(e)


if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar", key="logout-demo-app-home")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")

# Quick check of the session state.
with st.expander("Session State for Debugging", icon="💾"):
    st.session_state
