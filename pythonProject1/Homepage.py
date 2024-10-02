import streamlit as st
import streamlit_authenticator as stauth
from credentials import data
from menu import menu



st.set_page_config(layout="wide")

authenticator = stauth.Authenticate(data(), "WNW_APP","abcdefg",30)
number, name, authentication_status = authenticator.login("main")




if authentication_status == False:
    st.error("Username/Password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    
    st.session_state["number"]=number
    st.session_state["authentication_status"]=authentication_status
    
    
    st.title("Abitur 2025")
    

    menu()
    authenticator.logout("Logout","sidebar")


    

    

   
