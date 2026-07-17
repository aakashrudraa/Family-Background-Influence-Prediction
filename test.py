import streamlit as st

st.set_page_config(page_title="Deployment Test")

st.title("🚀 Streamlit Deployment Test")

st.success("If you can see this page, Streamlit deployment is working correctly!")

st.write("Python environment is working.")
st.write("Streamlit is installed successfully.")

if st.button("Click Me"):
    st.balloons()
    st.success("Everything is working!")