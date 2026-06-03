import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from src.utils import driver_summary,team_summary

st.set_page_config(page_title='PitWall AI')
st.title('🏎️ PitWall AI')

d=driver_summary()
t=team_summary()

c1,c2,c3=st.columns(3)
c1.metric('Drivers',len(d))
c2.metric('Teams',len(t))
c3.metric('Results',6)

st.subheader('Top Drivers')
st.dataframe(d[['driver','wins','avg_finish']])
