import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import streamlit_authenticator as stauth
from credentials import data
from username import username
from menu import menu

def punkte_übersicht(number):

    conn= st.connection("gsheets",type=GSheetsConnection)
    points_table = conn.read(worksheet="Tabellenblatt2")

    df=pd.DataFrame(points_table)
    points=df['Punkte'].to_list()
    punkte=points[int(number)-1]

    personal_points=pd.DataFrame(df.loc[df["Nummer"]==int(number)])
    personal_points=personal_points.fillna(0).head().astype(str)
    st.table(personal_points)
    return df, punkte

def points_sidebar(df,punkte):

    #Erstellen der Sidebar
    

    # Gesamtpunktzahl des User
    if punkte <=15:
        st.sidebar.write(f'''
                        Deine Punkte: {punkte}
                        <br>
                        :red[Dir fehlen noch {15-punkte} Punkte!]
                        ''',unsafe_allow_html=True)
    elif punkte >15:
        st.sidebar.write(f':green[Du hast {punkte-15} Punkte mehr als benötigt!]')
    menu()
    
    authenticator.logout("Logout","sidebar")
    




authenticator = stauth.Authenticate(data(), "APP","abcde",30)
authentication_status = st.session_state["authentication_status"]
if authentication_status:
    # Übersicht welche Punkte es gibt (Fix)
    st.title("Punktesystem")
    st.subheader("Wofür gibt es wie viele Punkte?")

    #Zugriff auf Sheets
    conn= st.connection("gsheets",type=GSheetsConnection)
    points_ov= conn.read(worksheet="Tabellenblatt3")

    #Tabelle Punkteübersicht Generell
    st.table(pd.DataFrame(points_ov))

    #Nummer des User nach Login
    number=st.session_state["number"]


    #Erklärung Punkte
    st.subheader("Wie setzen sich deine Punkte zusammen?")
    st.caption('''
            Die Faktoren der ersten Spalten sind nicht die Punkte!
            <br>
                Sie werden addiert und mal 3 gerechnet. Die gültigen Punkte stehen in der letzten Spalte!
            ''',unsafe_allow_html=True)

    # Verarbeitung der persönlichen Punkte in Tabelle / leere Zellen werden durch 0 ersetzt / Werte werden in der Tabelle zu Strings, um Nachkommastellen zu vermeiden
    sidebar=punkte_übersicht(number)    
    points_sidebar(sidebar[0],sidebar[1])

else:
    st.switch_page("Homepage.py")


    


