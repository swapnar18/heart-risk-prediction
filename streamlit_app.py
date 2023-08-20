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
single_select_cols= ['Gender','Education','Habitual Smoking' ,'BP Medication' , 'Any Prevalent Stroke','Any Prevalent Hypertension','Any Diabetes']
single_select_dict = {'Gender' :['Male','Female','Others'],
                      'Education' : ['Primary','Secondary','Graduate','Post Grad','Others'],
                      'Habitual Smoking' : ['Yes','No'],
                      'BP Medication' : ['Yes','No'],
                      'Any Prevalent Stroke' : ['Yes','No'],
                      'Any Prevalent Hypertension' : ['Yes','No'],
                      'Any Diabetes' : ['Yes','No']}
with st.form(key='columns_in_form'):
    col1, col2,col3 = st.columns(3)
    with col1:
        st.text_input('Enter Your Name',placeholder = 'Name',key=1) 
    with col2:
        st.text_input('Enter Your Weight in Kgs',placeholder = '1',key=2) 
    with col3:
        st.text_input('Enter Your Height in cms',placeholder = '10',key=3) 
    cols = st.columns(7)
    for i, col in enumerate(cols):
        col.selectbox(single_select_cols[i], single_select_dict[single_select_cols[i]], key=4+i)
    st.slider(label='Select Age', min_value=5, max_value=100, key=11)
    # st.slider(label='Ciggaretes Per Day (if smoking)', min_value=5, max_value=100, key=6)
    col4, col5,col6 = st.columns(3)
    with col4:
        st.text_input('Ciggaretes Per Day (if smoking)',placeholder = '0',key=12)
    with col5:
        st.text_input('Total Cholestrol',placeholder = '0',key=13)
    with col6:
        st.text_input('Heart Rate',placeholder = '0',key=14)
    submitted = st.form_submit_button('Submit')
