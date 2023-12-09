# import streamlit as st
import numpy as np
import pandas as pd
import joblib

# loaded_model = joblib.load('churn_model.sav')
# st.title('Churn or Not Churn')
Gender='Male'
SeniorCitizen=1
Partner=yes
Dependents=yes
tenure=40
PhoneService=no
MultipleLines=no
InternetService=DS1
OnlineSecurity=no
OnlineBackup=yes
DeviceProtection=yes
TechSupport=no
StreamingTV=no
StreamingMovies=no
Contract=st.selectbox("Choose Contract",['Month-to-month','Two year','One year'])
PaperlessBilling=st.selectbox("PaperlessBilling", ['yes','no'])
PaymentMethod=st.selectbox("Choose PaymentMethod",['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
MonthlyCharges=st.number_input("Input MonthlyCharges")
TotalCharges=st.number_input("Input TotalCharges")

 
columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges']

row = np.array([Gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity
                  ,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod, 
                  MonthlyCharges,TotalCharges]) 
X = pd.DataFrame([row], columns = columns)

yes_no_columns = ['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup',
                  'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling']
for col in yes_no_columns:
        X[col].replace({'yes': 1,'no': 0},inplace=True)
X['gender'].replace({'Male': 1,'Female': 0},inplace=True)
X = pd.get_dummies(X,['Contract','PaymentMethod','InternetService'])
X.head()   
    