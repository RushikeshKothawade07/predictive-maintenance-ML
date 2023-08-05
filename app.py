import streamlit as st
import joblib

rfc = joblib.load('model.joblib')

st.title("Machine Predictive Maintenance Classification")

#  Type
#  Air temperature [K]
#  Process temperature [K]
#  Rotational speed [rpm]
#  Torque [Nm]	
#  Tool wear [min]

# getting the input data from the user
col1, col2 = st.columns(2)

with col1:
    selected_type = st.selectbox('Select a Type', ['Low', 'Medium', 'High'])
    type_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    selected_type = type_mapping[selected_type]

  
with col2:
    air_temperature = st.text_input('Air temperature [K]')

with col1:
    process_temperature = st.text_input('Process temperature [K]')

with col2:
    rotational_speed = st.text_input('Rotational speed [rpm]')

with col1:
    torque = st.text_input('Torque [Nm]')

with col2:
    tool_wear = st.text_input('Tool wear [min]')


# code for Prediction
failure_pred = ''

# creating a button for Prediction

if st.button('Predict Failure'):
    failure_pred = rfc.predict([[selected_type,air_temperature, 
                                 process_temperature,rotational_speed,
                                 torque,
                                 tool_wear]])
    
    if (failure_pred[0] == 1):
        failure_pred = 'Failure'
    else:
        failure_pred = 'No Failure'
    
st.success(failure_pred)