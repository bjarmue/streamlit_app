import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
def username():
    #Zugriff auf Nummer des User durch Login
    number=st.session_state["number"]

    #Zugriff auf Sheets
    conn= st.connection("gsheets",type=GSheetsConnection)

    #Zugriff auf den Namen des User in Abhängigkeit seiner Nummer
    personal_name= conn.read(worksheet="Tabellenblatt1",usecols=[0,1],ttl=1)
    df=pd.DataFrame(personal_name)
    names=df['Name'].to_list()
    name=names[int(number)-1]
    
    return name
