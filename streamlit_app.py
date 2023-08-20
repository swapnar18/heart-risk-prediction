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
# used_widget_key = st.get_last_used_widget_key()
with st.form(key='columns_in_form'):
    col1, col2,col3 = st.columns(3)
    with col1:
        Name = st.text_input('Enter Your Name','Name',key=1) 
    with col2:
        Weight  = st.text_input('Enter Your Weight in Kgs','1',key=2) 
    with col3:
        Height = st.text_input('Enter Your Height in cms','10',key=3) 
    cols = st.columns(7)
    cols_dict = {}
    for i, col in enumerate(cols):
        cols_dict[single_select_cols[i]] = col.selectbox(single_select_cols[i], single_select_dict[single_select_cols[i]], key=4+i)
    Age = st.slider(label='Select Age', min_value=5, max_value=100, key=11)
    # st.slider(label='Ciggaretes Per Day (if smoking)', min_value=5, max_value=100, key=6)
    col4, col5,col6 = st.columns(3)
    with col4:
        ciggs_per_day = st.text_input('Ciggaretes Per Day (if smoking)','0',key=12)
    with col5:
        tot_cholestrol = st.text_input('Total Cholestrol','0',key=13)
    with col6:
        h_rate = st.text_input('Heart Rate','0',key=14)
    col7, col8 = st.columns(2)
    with col7:
        sys_bp = st.slider(label='Select Systolic BP', min_value=80, max_value=200, key=15)
    with col8:
        dia_bp = st.slider(label='Select Diastolic BP', min_value=20, max_value=140, key=16)
    submitted = st.form_submit_button('Submit')
if submitted:
    st.write(f'Hello {Name}')
    # st.write(f'Your BMI is : {str(int(int(Weight)/(int(Height/10)**2)))}')
    st.write(f'Your Weight  is : {Weight}')
    st.write(f'Your Height  is : {Height}')
    print(type(Weight))
    print(type(int(Weight)))
    # BMI = int(int(Weight)/(int(Height/10)**2))
    st.write(f'Your BMI is : {str(BMI)}')
