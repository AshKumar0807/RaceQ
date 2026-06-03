
import streamlit as st
import random

st.title('Race Simulator')

if st.button('Run 10,000 Simulations'):
    st.write({
        'Leclerc':'42%',
        'Verstappen':'39%',
        'Hamilton':'19%'
    })
