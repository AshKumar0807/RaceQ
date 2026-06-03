
import streamlit as st

st.title('Podium Predictor')

grid=st.slider('Grid Position',1,20,1)
prob=max(5,90-grid*8)

st.metric('Podium Probability',f'{prob}%')
