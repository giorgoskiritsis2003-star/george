import streamlit as st 
import datetime
import requests

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FF0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Game Night")


catagory = st.radio(
    "Τι θέλετε να παίξουμε;",
    ["League of Legends", "Fortnite", "GTA VI", "F1", "Άλλο"],
    index=None,
)

final_game = catagory


if catagory == "Άλλο":
    custom_game = st.text_input("Γράψε ποιο παιχνίδι:")
    final_game = custom_game 


if final_game:
   
    event_date = st.date_input("Ποια μέρα θέλετε να παίξουμε;", datetime.date(2026, 11, 19))
    event_time = st.time_input("Τι ώρα;", datetime.time(16, 45))
    st.write("Event scheduled for", event_date, "στις", event_time)
    
if st.button('Submit my picks '):
    webhook_url = st.secrets["discord_url2"] 
    
    to_minima_mou = f"Game Night!\n"
    to_minima_mou += f"Παιχνίδι: {final_game}\n"
    to_minima_mou += f"Πότε:{event_date} στις {event_time}"
        
    data = {"content": to_minima_mou}
    requests.post(webhook_url, json=data)

    st.success(" Τα δεδομένα στάλθηκαν")