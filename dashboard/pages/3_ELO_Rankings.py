
import streamlit as st
from src.utils import elo_rankings

st.title('ELO Rankings')
st.dataframe(elo_rankings())
st.bar_chart(elo_rankings().set_index('driver'))
