import streamlit as st
from username import username
import streamlit_authenticator as stauth
from credentials import data

def menu():
    st.sidebar.title(f'{username()}')
    st.sidebar.page_link("Homepage.py",label="Home")
    st.sidebar.page_link("Punkte.py",label="Punkte")
    st.sidebar.page_link("Kuchen.py",label="Pausenverkauf")
    st.sidebar.page_link("Motto.py",label="Abi Motto")
    
   
   
    


    
