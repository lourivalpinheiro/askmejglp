# CÓDIGO

import streamlit as st

st.set_page_config("ASK ME", page_icon='askme.ico', layout='wide')
ico = "askme.ico"
st.image('askme.png')
menu = st.sidebar.selectbox("MENU", options=["CONHECIMENTO"], index=0)
st.header("BEM-VINDOS AO ASK ME!")
st.divider()
st.write(
    '''
Pesquise sobre temas extramamente relevantes ao período de gravidez e que exigem atenção dos pais.
'''
)