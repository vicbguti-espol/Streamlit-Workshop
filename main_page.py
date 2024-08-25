import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

if "salute" not in st.session_state:
    st.session_state.salute = "hello"