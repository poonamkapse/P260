# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:14:02 2023

@author: LENOVO
"""
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('D:\Project\Dataset_Objective\Dataset _ Objective/trained_model.sav', 'rb'))


# creating a function for Prediction

def machine_failure(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'MAachine not failed'
    else:
      return 'Maachine failed'
  
    
  
def main():
    
    
    # giving a title
    st.title('MAchine Failure Web App')
    
    
    # getting the input data from the user
   
    
    Type = st.text_input('Type')
    Airtemperature = st.text_input('Air temperature [K]')
    Processtemperature = st.text_input('Process temperature')
    Rotationalspeed = st.text_input('Rotational speed')
    Torque = st.text_input('Torque')
    Toolwear = st.text_input('Tool wear [min]')
      
    
    # code for Prediction
    machine_failed = ''
    
    # creating a button for Prediction
    
    if st.button('Result'):
        machine_failed = machine_failure([Type,Airtemperature ,Processtemperature ,Rotationalspeed ,Torque,Toolwear	])
        
        
    st.success(machine_failed)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    