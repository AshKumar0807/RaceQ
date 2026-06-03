
import streamlit as st
from src.utils import team_summary

st.title('Team Analytics')
st.dataframe(team_summary())
