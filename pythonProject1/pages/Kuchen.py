import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import streamlit_authenticator as stauth
from credentials import data
from username import username
from menu import menu

authenticator = stauth.Authenticate(data(), "APP","abcde",30)
authentication_status = st.session_state["authentication_status"]
if authentication_status:
    # Übersicht welche Punkte es gibt (Fix)
    st.title("Pausenverkauf")
    st.subheader("Wann macht welches Tutorat den Pausenverkauf?")

    #Zugriff auf Sheets
    conn= st.connection("gsheets",type=GSheetsConnection)
    kuchen_ov = conn.read(worksheet="Tabellenblatt4")
    kuchen_sale=conn.read(worksheet="Tabellenblatt5")
    
    #Tabelle übersicht Generell
    st.table(pd.DataFrame(kuchen_ov))

    #Nummer des User nach Login
    number=st.session_state["number"]
    menu()
    
    authenticator.logout("Logout","sidebar")

    st.title("Nächster Verkauf:")
    st.subheader("Wer macht was beim nächsten Verkauf:")

    #Tabelle Verkauf
    st.table(pd.DataFrame(kuchen_sale).fillna("/"))

    with st.form(key="verkauf",clear_on_submit=True):    
        pause=st.selectbox("Wann machst du Verkauf?*",options=["1. Pause","2. Pause","/"],index=None)
        mitbringen=st.text_input(label="Was bringst du mit?*")
        sale_data=pd.DataFrame(
            [
                {
                    "Name":username(),
                    "Verkauf":pause,
                    "Mitbringen":mitbringen,
                }
            ]
        )
        updated_df=pd.concat([kuchen_sale,sale_data], ignore_index=True)
        submit_button=st.form_submit_button(label="Submit")
        st.markdown(":red[*mindestens ein Feld muss ausgefüllt sein]")
        if not pause and not mitbringen:
            st.warning("Mindestens eines der beiden Felder muss ausgefüllt sein!")

        elif submit_button==True:
            conn.update(worksheet="Tabellenblatt5",data=updated_df)
            st.rerun()
            
            
        




else:
    st.switch_page("Homepage.py")