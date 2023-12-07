import streamlit as st
import numpy as np
import pandas as pd
import joblib


loaded_model = joblib.load('finalized_model.sav')
st.title('predict house-price in tehran:')
Area = st.number_input("Input House area",0,1000)
Room=st.selectbox("Choose Room", [0,1,2,3,4,5])
Parking=st.selectbox("choose for parking: 1 for yes ,0 for no",[0,1])
Warehouse=st.selectbox("choose for Warehouse: 1 for yes ,0 for no",[0,1])
Elevator=st.selectbox("choose for Elevator: 1 for yes ,0 for no",[0,1])
Address=st.text_input("input Address","pasdaran")
Address=Address.capitalize()

columns=['Area', 'Room', 'Parking', 'Warehouse', 'Elevator', 'Abazar',
       'Abbasabad', 'Absard', 'Abuzar', 'Afsarieh', 'Ahang', 'Air force',
       'Ajudaniye', 'Alborz Complex', 'Aliabad South', 'Amir Bahador',
       'Amirabad', 'Amirieh', 'Andisheh', 'Aqdasieh', 'Araj', 'Argentina',
       'Atabak', 'Azadshahr', 'Azarbaijan', 'Azari', 'Baghestan', 'Bahar',
       'Baqershahr', 'Beryanak','Boloorsazi', 'Central Janatabad', 'Chahardangeh', 'Chardangeh',
       'Chardivari', 'Chidz', 'Damavand', 'Darabad', 'Darakeh', 'Darband',
       'Daryan No', 'Dehkade Olampic', 'Dezashib', 'Dolatabad', 'Dorous',
       'East Ferdows Boulevard', 'East Pars', 'Ekbatan', 'Ekhtiarieh',
       'Elahieh', 'Elm-o-Sanat', 'Enghelab','Eram', 'Eskandari', 'Fallah',
       'Farmanieh', 'Fatemi', 'Feiz Garden', 'Firoozkooh', 'Firoozkooh Kuhsar',
       'Gandhi', 'Garden of Saba', 'Gheitarieh', 'Ghiyamdasht', 'Ghoba',
       'Gholhak', 'Gisha', 'Golestan', 'Haft Tir', 'Hakimiyeh', 'Hashemi',
       'Hassan Abad', 'Hekmat', 'Heravi', 'Heshmatieh', 'Hor Square',
       'Islamshahr', 'Islamshahr Elahieh', 'Javadiyeh', 'Jeyhoon','Jordan', 'Kahrizak', 'Kamranieh', 'Karimkhan', 'Karoon', 'Kazemabad',
       'Keshavarz Boulevard', 'Khademabad Garden', 'Khavaran', 'Komeil',
       'Koohsar', 'Kook', 'Lavasan', 'Lavizan', 'Mahallati', 'Mahmoudieh',
       'Majidieh', 'Malard', 'Marzdaran', 'Mehrabad', 'Mehrabad River River',
       'Mehran', 'Mirdamad', 'Mirza Shirazi', 'Moniriyeh', 'Narmak',
       'Nasim Shahr', 'Nawab', 'Naziabad', 'Nezamabad', 'Niavaran',
       'North Program Organization', 'Northern Chitgar', 'Northern Janatabad',
       'Northern Suhrawardi', 'Northren Jamalzadeh', 'Ostad Moein', 'Ozgol',
       'Pakdasht', 'Pakdasht KhatunAbad','Parand', 'Parastar', 'Pardis', 'Pasdaran', 'Persian Gulf Martyrs Lake',
       'Pirouzi', 'Pishva', 'Punak', 'Qalandari', 'Qarchak', 'Qasr-od-Dasht',
       'Qazvin Imamzadeh Hassan', 'Railway', 'Ray', 'Ray - Montazeri',
       'Ray - Pilgosh', 'Razi', 'Republic', 'Robat Karim', 'Rudhen',
       'Saadat Abad', 'SabaShahr', 'Sabalan', 'Sadeghieh', 'Safadasht',
       'Salehabad', 'Salsabil', 'Sattarkhan', 'Seyed Khandan', 'Shadabad',
       'Shahedshahr', 'Shahr-e-Ziba', 'ShahrAra', 'Shahrake Apadana',
       'Shahrake Azadi', 'Shahrake Gharb', 'Shahrake Madaen', 'Shahrake Qods',
       'Shahrake Quds', 'Shahrake Shahid Bagheri', 'Shahrakeh Naft', 'Shahran',
       'Shahryar', 'Shams Abad', 'Shoosh', 'Si Metri Ji', 'Sohanak',
       'Southern Chitgar', 'Southern Janatabad',
       'Southern Program Organization', 'Southern Suhrawardi', 'Tajrish',
       'Tarasht', 'Taslihat', 'Tehran Now', 'Tehransar', 'Telecommunication',
       'Tenant', 'Thirteen November', 'Vahidieh', 'Vahidiyeh', 'Valiasr',
       'Vanak', 'Varamin - Beheshti', 'Velenjak', 'Villa',
       'Water Organization', 'Waterfall', 'West Ferdows Boulevard',
       'West Pars', 'Yaftabad', 'Yakhchiabad', 'Yousef Abad', 'Zafar',
       'Zaferanieh', 'Zargandeh', 'Zibadasht']
  
def andis():
    for i in columns:
      if Address== i:
         z=columns.index(i)
         return z
z1=andis()         
def predict(): 
    row =np.zeros((1,197))
    X = pd.DataFrame(row, columns = columns)
    X.iloc[0,0]=Area
    X.iloc[0,1]=Room
    X.iloc[0,2]=Parking
    X.iloc[0,3]=Warehouse
    X.iloc[0,4]=Elevator
    X.iloc[0,z1]=1

    
    
    prediction = loaded_model.predict(X)
    st.write('We will predict  price and show in app something.')
    st.write(prediction)
    

trigger = st.button('Predict', on_click=predict)
