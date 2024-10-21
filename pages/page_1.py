import streamlit as st

st.set_page_config(page_title="Page 1")

if st.session_state.get("authentication_status") is not None:
    authenticator = st.session_state.get("authenticator")
    authenticator.login(location="unrendered", key="authenticator-page-1")


if st.session_state == {} or st.session_state["authentication_status"] is None:
    st.page_link("Home.py", label="Home", icon="🏠")
    st.warning("Please use the button above to navigate to Home and log in.")
    st.stop()

else:
    st.title("Page 1")
    st.write(f"Hello {st.session_state.get('name')}, welcome to Page 2!")

# Quick check of the session state.
with st.expander("Session State for Debugging", icon="💾"):
    st.session_state