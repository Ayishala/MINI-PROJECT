import streamlit as st
import joblib
model_nb = joblib.load('POEM-CLASSIFICATION')
st.title('POEM CLASSIFICATION') #creates a title in web app
ip = st.text_input('Enter POEM:') #creates a text box in web app
op = model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0])
  
