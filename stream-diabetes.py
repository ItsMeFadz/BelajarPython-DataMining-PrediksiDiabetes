import pickle 
import streamlit as st

# Membaca model 
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# judul Web
st.title ('Data Mining Prediksi Diabetes')

# form inputan 
# membagi Kolom 
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input('Input Nilai Pregnecies')
with col1 :
    Glucose = st.text_input('Input Nilai Glucose')
with col1 :
    BloodPressure = st.text_input('Input Nilai Blood Preasure')
with col1 :
    SkinThickness = st.text_input('Input Nilai Skin Thickness')
with col2 :
    Insulin = st.text_input('Input Nilai Insulin')
with col2 :
    BMI = st.text_input('Input Nilai BMI')
with col2 :
    DiabetesPedigreeFunction = st.text_input('Input Nilai Diabetes Pedigree Funcition ')
with col2 :
    Age = st.text_input('Input Nilai Age')

# Code untuk prediksi 
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes') :
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                            Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if diab_prediction == 1 :
        diab_diagnosis = 'Pasien tidak terkena diabetes'
    elif diab_prediction == 0 :
        diab_diagnosis = 'Pasien Terkena Diabetes'
    
    st.success(diab_diagnosis)