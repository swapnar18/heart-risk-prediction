import streamlit as st
import joblib

def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == 'spring':
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

file_name = "xgb_reg.pkl"
# joblib.dump(xg_clf, file_name) 
xgb = joblib.load(file_name)

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


def run_prediction():
    # st.write('Hello world!')
    # st.title("Welcome to Heart Risk Prediction App Using Machine Learning", anchor=None, *, help=None)
    st.caption(' ')
    st.caption(' ')
    st.caption('Please enter your health details below to get your personalized heart risk probability :heartpulse:')
    # st.caption('A caption with _italics_ :blue[colors] and emojis :heartpulse:')
    columns = ['Gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds','prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',\
               'diaBP', 'BMI', 'heartRate', 'glucose']
    single_select_cols= ['Gender','Education','Habitual Smoking' ,'BP Medication' , 'Any Prevalent Stroke','Any Prevalent Hypertension','Any Diabetes']
    single_select_dict = {'Gender' :{1:'Male',0:'Female',2:'Others'},
                          'Education' : {1:'Primary',2:'Secondary',3:'Graduate',4:'Post Grad',5:'Others'},
                          'Habitual Smoking' : {1:'Yes',0:'No'},
                          'BP Medication' : {1:'Yes',0:'No'},
                          'Any Prevalent Stroke' :{1:'Yes',0:'No'},
                          'Any Prevalent Hypertension' :{1:'Yes',0:'No'},
                          'Any Diabetes' : {1:'Yes',0:'No'}}
    # used_widget_key = st.get_last_used_widget_key()
    def format_func(key,option):
        return single_select_dict[key][0]
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
            cols_dict[single_select_cols[i]] = int(col.selectbox(single_select_cols[i], options = single_select_dict[single_select_cols[i]].keys() ,format_func= lambda x: single_select_dict[single_select_cols[i]][x], key=4+i))
        Age = int(st.slider(label='Select Age', min_value=5, max_value=100, key=11))
        # st.slider(label='Ciggaretes Per Day (if smoking)', min_value=5, max_value=100, key=6)
        col4, col5,col6 = st.columns(3)
        with col4:
            ciggs_per_day = int(st.text_input('Ciggaretes Per Day (if smoking)','0',key=12))
        with col5:
            tot_cholestrol = int(st.text_input('Total Cholestrol','0',key=13))
        with col6:
            h_rate = int(st.text_input('Heart Rate','0',key=14))
        col7, col8 = st.columns(2)
        with col7:
            sys_bp = int(st.slider(label='Select Systolic BP', min_value=80, max_value=200, key=15))
        with col8:
            dia_bp = int(st.slider(label='Select Diastolic BP', min_value=20, max_value=140, key=16))
        submitted = st.form_submit_button('Submit')
    if submitted:
        st.write(f'Hello {Name} , Thanks for submitting your health records !!! ')
        
        # st.write(f"Hello {cols_dict['Gender']}")
        # st.write(f'Your BMI is : {str(int(int(Weight)/(int(Height/10)**2)))}')
        # st.write(f'Your Weight  is : {Weight}')
        # st.write(f'Your Height  is : {Height}')
        Weight = int(Weight)
        Height = pow(int(Height)/100 , 2)
        # st.write(pow(int(Weight),2))
        BMI = int(Weight/Height)
        gender = 0 if cols_dict['Gender']<1 else 1
        education = 1 if cols_dict['Education']==5 else cols_dict['Education']
        st.write(f'{gender},{education},{cols_dict},{Age},{ciggs_per_day},{tot_cholestrol},{h_rate},{sys_bp},{dia_bp} ,{BMI}')
        st.write(f'Your BMI is : {str(BMI)}')

if check_password():
    run_prediction()
