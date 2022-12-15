import streamlit as st
import joblib
model_nb = joblib.load('stress detection')
st.title('stress detection') #creates a title in web app
ip = st.text_input('Enter text:') #creates a text box in web app
op = model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0])
            
          
