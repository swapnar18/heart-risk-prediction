import streamlit as st

# title_alignment=
# """
# <style>
# #the-title {
#   text-align: center
# }
# </style>
# """
# st.markdown(title_alignment, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: green;'>Welcome to Heart Risk Prediction App Using Machine Learning</h1>", unsafe_allow_html=True)

# st.write('Hello world!')
# st.title("Welcome to Heart Risk Prediction App Using Machine Learning", anchor=None, *, help=None)

with st.form(key='columns_in_form'):
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.selectbox(f'Make a Selection', ['click', 'or click'], key=i)
    submitted = st.form_submit_button('Submit')
