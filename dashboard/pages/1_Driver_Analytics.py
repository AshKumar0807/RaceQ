
import streamlit as st
from src.utils import driver_summary

st.title('Driver Analytics')
st.dataframe(driver_summary())
