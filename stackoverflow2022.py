import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('stackoverflow2022.sav')
st.title('Salary Prediction in 2022')
st.write("""### We need some information to predict the salary""")

countries = {
    "United States of America":29,
    "Iran, Islamic Republic of...":12,
    "India":11,
    "United Kingdom of Great Britain and Northern Ireland":28,
    "Germany":9,
    "Canada":4,
    "Brazil":3,
    "France":8,
    "Spain":24,
    "Australia":0,
    "Netherlands":16,
    "Poland":20,
    "Italy":14,
    "Russian Federation":22,
    "Sweden":25,
    "Switzerland":26,
    "Israel":13,
    "Austria":1,
    "Portugal":21,
    "Denmark":6,
    "Turkey":27,
    "Belgium":2,
    "Norway":18,
    "Finland":7,
    "Greece":10,
    "Czech Republic":5,
    "New Zealand":17,
    "Mexico":15,
    "South Africa":23,
    "Pakistan":19

}


education = (
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree"
)

country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education)
expericence = st.slider("Years of Experience", 0, 50, 3)

columns = ['Country', 'EdLevel', 'YearsCodePro']

ok = st.button("Calculate Salary")
if ok:
    row =np.zeros((1,3))
    X = pd.DataFrame(row, columns = columns)
    if  education== 'Less than a Bachelors':
        X.iloc[0,1]=1
    elif education== 'Bachelor’s degree': 
        X.iloc[0,1]=0
    elif education=='Master’s degree': 
        X.iloc[0,1]=2
    X.iloc[0,2]=expericence
    X.iloc[0,0]=countries[country]
    salary = model.predict(X)
    
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")\

