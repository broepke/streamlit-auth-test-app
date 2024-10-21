import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import LoginError
import yaml
from yaml.loader import SafeLoader

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

# Authentication logic
try:
    authenticator.login()
    st.session_state["authenticator"] = authenticator
    st.session_state["config"] = config
except LoginError as e:
    st.error(e)


if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar", key="logout-demo-app")
    st.sidebar.write(f'Welcome *{st.session_state["name"]}*')
    st.title("Streamlit-Autheticator")
    st.subheader("Multi-Page App")
    st.write("https://github.com/mkhorasani/Streamlit-Authenticator")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
