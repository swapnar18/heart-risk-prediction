import streamlit as st
st.set_page_config(layout="wide")
# title_alignment=
# """
# <style>
# #the-title {
#   text-align: center
# }
# </style>
# """
# st.markdown(title_alignment, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color:#056608;'>Welcome to Heart Risk Prediction App Using Machine Learning !!!</h1>", unsafe_allow_html=True)

# st.write('Hello world!')
# st.title("Welcome to Heart Risk Prediction App Using Machine Learning", anchor=None, *, help=None)
st.caption(' ')
st.caption(' ')
st.caption('Please enter your health details below to get your personalized heart risk probability :heartpulse:')
# st.caption('A caption with _italics_ :blue[colors] and emojis :heartpulse:')
columns = ['Gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds','prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',\
           'diaBP', 'BMI', 'heartRate', 'glucose']
single_select_cols= ['Gender','Education','Habitual Smoking' ,'BP Medication' , 'Any Prevalent Stroke','Any Prevalent Hypertension']
single_select_dict = {'Gender' :['Male','Female','Others'],
                      'Education' : ['Primary','Secondary','Graduate','Post Grad','Others'],
                      'Habitual Smoking' : ['Yes','No'],
                      'BP Medication' : ['Yes','No'],
                      'Any Prevalent Stroke' : ['Yes','No'],
                      'Any Prevalent Hypertension' : ['Yes','No']}
with st.form(key='columns_in_form'):
    cols = st.columns(6)
    for i, col in enumerate(cols):
        col.selectbox(single_select_cols[i], single_select_dict[single_select_cols[i]], key=i)
    submitted = st.form_submit_button('Submit')
