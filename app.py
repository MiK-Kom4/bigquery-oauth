import streamlit as st
import requests

st.title("Google BigQuery Authentication")

login_button = st.button("Googleでログイン", type="primary")
if login_button:
    login_url = "http://localhost:8000/login"
    st.write("Redirecting to the login page...")
    st.markdown(f'<meta http-equiv="refresh" content="0; url={login_url}" />', unsafe_allow_html=True)

