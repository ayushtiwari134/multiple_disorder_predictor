import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler

# Load the pickled model
pipe = pickle.load(open('pipe.pkl', 'rb'))
diabetes = pickle.load(open('diabetes.pkl', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                            ['Obesity Prediction',
                            'Diabetes Prediction',]
                            ,default_index=0)

# Obesity Prediction
if (selected=='Obesity Prediction'):
    st.title('Obesity Prediction')
    col1,col2,col3= st.columns(3)
    with col1:
        age = st.number_input('Age',min_value=0, step=1,value=0)
    with col2:
        gender = st.selectbox("Gender",['Male','Female'])
    with col3:
        height = st.number_input('Height',min_value=0, step=1,value=0)
    with col1:
        weight = st.number_input('Weight',min_value=0, step=1,value=0)
    with col2:
        bmi = st.number_input('BMI',min_value=0, step=1,value=0)
    
    if st.button('Predict'):
        input = np.array([[age,gender,height,weight,bmi]])
        prediction = pipe.predict(input)
        # st.write(prediction)
        type =['Normal Weight', 'Obese', 'Overweight', 'Underweight']
        value = 0
        for i in range(4):
            if prediction[0][i] == 1:
                value = i
                break
        st.success('You are '+type[value])
            


# Diabetes Prediction
if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction')
    col1,col2,col3= st.columns(3)
    with col1:
        pregnancies = st.number_input('Pregnancies',min_value=0, step=1,value=0)
    with col2:
        glucose = st.number_input('Glucose',min_value=0, step=1,value=0)
    with col3:
        blood_pressure = st.number_input('Blood Pressure',min_value=0, step=1,value=0)
    with col1:
        skin_thickness = st.number_input('Skin Thickness',min_value=0, step=1,value=0)
    with col2:
        insulin = st.number_input('Insulin',min_value=0, step=1,value=0)
    with col3:
        bmi = st.number_input('BMI',min_value=0.0, step=0.1,value=0.0)
    with col1:
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function',min_value=0.0, step=0.1,value=0.0)
    with col2:
        age = st.number_input('Age')
    
    if st.button('Predict'):
        input = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]).astype(np.float64)
        standardScaler = StandardScaler()
        input = standardScaler.fit_transform(input)
        prediction = diabetes.predict(input)
        if prediction[0] == 0:
            st.success('You are not diabetic')
        else:
            st.error('You are diabetic')