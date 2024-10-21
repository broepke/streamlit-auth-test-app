import streamlit as st

st.set_page_config(page_title="Page 1")
st.title("Page 1")
st.write(f"Hello {st.session_state.get('name')}, welcome to Page 2!")
st.write("""
On the second page, we're going to first check to see if the user is authenticated by looking at session state.  if it's not, then render a button to go back home.  If the user is authenticated, display the page content.
""")

if st.session_state.get("authentication_status") is not None:
    authenticator = st.session_state.get("authenticator")
    authenticator.login(location="unrendered", key="authenticator-page-1")


if st.session_state == {} or st.session_state["authentication_status"] is None:
    st.warning("Please use the button below to navigate to Home and log in.")
    st.page_link("Home.py", label="Home", icon="🏠")
    st.stop()

else:
    st.success("You are logged in!")

# Quick check of the session state.
with st.expander("Session State for Debugging", icon="💾"):
    st.session_state