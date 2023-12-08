import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

loaded_model = joblib.load('churn_model.sav')
st.title('Churn or Not Churn')
Gender=st.selectbox("Choose sex", ['male','female'])
SeniorCitizen=st.selectbox("Choose SeniorCitizen", [1,0])
Partner=st.selectbox("Choose Partner", ['yes','no'])
Dependents=st.selectbox("Choose Dependents", ['yes','no'])
tenure=st.number_input("Input tenure",0,100)
PhoneService=st.selectbox("Choose PhoneService", ['yes','no'])
MultipleLines=st.selectbox("Choose MultipleLines", ['yes','no'])
InternetService=st.selectbox("Choose InternetService",['Fiber Optic','DSl','no'])
OnlineSecurity=st.selectbox("Choose OnlineSecurity", ['yes','no'])
OnlineBackup=st.selectbox("Choose OnlineBackup", ['yes','no'])
DeviceProtection=st.selectbox("Choose DeviceProtection", ['yes','no'])
TechSupport=st.selectbox("Choose TechSupport", ['yes','no'])
StreamingTV=st.selectbox("Choose StreamingTV", ['yes','no'])
StreamingMovies=st.selectbox("Choose StreamingMovies", ['yes','no'])
Contract=st.selectbox("Choose Contract",['Month-to-month','Two year','One year'])
PaperlessBilling=st.selectbox("PaperlessBilling", ['yes','no'])
PaymentMethod=st.selectbox("Choose PaymentMethod",['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
MonthlyCharges=st.number_input("Input MonthlyCharges")
TotalCharges=st.number_input("Input TotalCharges")

inter_fib=inter_dsl=inter_no=0
contract_month=contract_twoyear=Contract_oneyear=0
payment_elec=payment_mailed=payment_bank=payment_credit=0

if InternetService=='Fiber Optic':
    inter_fib=1
elif  InternetService=='DSl':   
    inter_dsl=1 
elif  InternetService=='no':      
    inter_no=1  

if   Contract== 'Month-to-month':
     contract_month=1
elif Contract== 'Two year': 
     contract_twoyear=1
elif Contract=='One year': 
     Contract_oneyear=1

if    PaymentMethod== 'Electronic check': 
     payment_elec=1
elif  PaymentMethod== 'Mailed check':
      payment_mailed=1   
elif  PaymentMethod== 'Bank transfer (automatic)':
      payment_bank=1 
elif  PaymentMethod== 'Credit card (automatic)':
      payment_credit=1       




columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
       'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
       'Contract_DSL', 'Contract_Fiber optic', 'Contract_No',
       'PaymentMethod_Month-to-month', 'PaymentMethod_One year',
       'PaymentMethod_Two year', 'InternetService_Bank transfer (automatic)',
       'InternetService_Credit card (automatic)',
       'InternetService_Electronic check', 'InternetService_Mailed check']

def predict(): 
    row = np.array([Gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,OnlineSecurity
                  ,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,PaperlessBilling, 
                  MonthlyCharges,TotalCharges,inter_fib,inter_dsl,inter_no,contract_month,contract_twoyear,Contract_oneyear,
                  payment_elec,payment_mailed,payment_bank,payment_credit]) 
    X = pd.DataFrame([row], columns = columns)

    yes_no_columns = ['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup',
                  'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling']
    for col in yes_no_columns:
        X[col].replace({'yes': 1,'no': 0},inplace=True)
    X['gender'].replace({'male': 1,'female': 0},inplace=True)

    cols_to_scale = ['tenure','MonthlyCharges','TotalCharges']
    scaler = MinMaxScaler()
    X[cols_to_scale] = scaler.fit_transform( X[cols_to_scale])
   
    prediction = loaded_model.predict(X)
    if prediction[0] == 0: 
        st.success('Custemer Not Churn:thumbsup:')
    else: 
        st.error('Custemer  Churn:thumbsdown:') 

trigger = st.button('Predict', on_click=predict)