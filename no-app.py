import streamlit as st

counter = 0
counter += 1

st.header(f"This page has run {counter} times.")
st.button("Run it again")