import streamlit as st

def show():
    st.title("This is Page 2")
    st.write("Welcome to Page 2!")

    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()
