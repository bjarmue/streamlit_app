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
    # Überschrifft
    st.title("Abimotto 2025")
    st.subheader("Vorschläge:")

    conn= st.connection("gsheets",type=GSheetsConnection)
    motto = conn.read(worksheet="Tabellenblatt8")
    motto=pd.DataFrame(motto).fillna("")
    abstimmung = conn.read(worksheet="Tabellenblatt9")
    abstimmung=pd.DataFrame(abstimmung).fillna("")
    result = conn.read(worksheet="Tabellenblatt10")
    result=pd.DataFrame(result).fillna("")
    
    
    menu()
    
    authenticator.logout("Logout","sidebar")
    with st.form(key="motto",clear_on_submit=True):    
        motto_vorschlag=st.text_input(label="Was ist dein Vorschlag?*")
        vorschlaege=pd.DataFrame(
            [
                {
                    "Vorschläge":motto_vorschlag,
                    "Name":username(),
                    
                    
                }
            ]
        )
        updated_df=pd.concat([motto,vorschlaege], ignore_index=True)
        submit_button=st.form_submit_button(label="Submit")
        st.markdown(":red[*Muss ausgefüllt sein]")

        if not motto_vorschlag:
            st.warning("*Muss ausgefüllt sein!")

        elif submit_button==True:
            conn.update(worksheet="Tabellenblatt7",data=updated_df)
            st.rerun()

            
    st.table(motto["Vorschläge"])

    st.subheader("Abstimmung:")
    st.write("Jeder hat eine Stimmen. Doppelte Stimmen werden entfernt!")

    with st.form(key='abstimmung',clear_on_submit=True):
        stimme=st.selectbox("Für welches Motto bist du?*",options=motto['Vorschläge'] ,index=None)
        
        
        stimmen=pd.DataFrame(
            [
                {
                    "Name":username(),
                    "Stimme":stimme,
                    
                }
            ]
        )
        updated_stimmen=pd.concat([abstimmung,stimmen], ignore_index=True)
        button=st.form_submit_button(label="Submit")
        st.markdown(":red[*Muss ausgewählt werden]")

        if not stimme:
            st.warning("*Muss ausgewählt werden!")

        elif button==True:
            conn.update(worksheet="Tabellenblatt9",data=updated_stimmen)
            st.rerun()

   
    st.bar_chart(result,x="Vorschläge",color="Stimmen" )
    

else:
    st.switch_page("Homepage.py")