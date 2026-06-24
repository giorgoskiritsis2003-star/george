import streamlit as st 
import datetime
import requests

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6e6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("Date")


catagory = st.radio(
    "Τι θέλεις να κάνουμε;",
    ["Game night :video_game:","Movie night :popcorn:", "Drink night :cocktail:", " Food night :pizza:"," Walking :athletic_shoe:"],
    index=None,
)

st.write("You selected:", catagory)

Game = None
Movie = None
Drink = None
Food = None
Walk = None


if catagory == "Game night :video_game:":

    Game = st.radio(
    "Τι θές να παίξουμε;",
    ["Split", "Dont starve together", "We Were Here", "Minecraft"],
    index=None,
)
    st.write("You selected:", Game)


if catagory == "Movie night :popcorn:":

    Movie = st.radio(
    "Τι θές να δούμε;",
    ["Τανια", "Anime", "Σειρα στο Netflix", "Disney"],
    index=None,
)
    st.write("You selected:", Movie)

if catagory == "Drink night :cocktail:":

    Drink = st.radio(
    "Που θες να παμε να πιουμε;",
    ["Σε Βar", "Σε Τσιπουράδικο ", "Σε Παγκάκι στο παραλίμνιο", "Σπίτι","Καφέτέρια"],
    index=None,
)
    st.write("You selected:", Drink)

if catagory == " Food night :pizza:":

    Food = st.radio(
    "Τι θες να φάμε ;",
    ["Πίτα", "Κρέπα", "Πίτσα", "Burger","Τσιπουράδικο"],
    index=None,
)
    st.write("You selected:", Food)

if catagory == " Walking :athletic_shoe:":

    Walk = st.radio(
    "Που θες να πάμε βόλτα;",
    ["Παραλίμνιο", "Μαγαζιά", "Στο κέντρο", "Γέφυρα"],
    index=None,
)
    st.write("You selected:", Walk)

if Game or Movie or Drink or Food or Walk:

    event_date = st.date_input("Ποια μέρα θες να πάμε;", datetime.date(2026, 11, 19))
    event_time = st.time_input("Τι ώρα;", datetime.time(16, 45))
    
    st.write("Event scheduled for", event_date, "στις", event_time)
    
if st.button('Submit my picks '):
    webhook_url = "https://discord.com/api/webhooks/1519280679433801779/gCcudWI8zYoQ25bRt-9qcjMF8QycRKgCFZbiwvf1zQXhqXyL9pEHCjPVi0zvPGSUO6Us"
    
    to_minima_mou = f" Έχεις νέο ραντεβού\n"
    to_minima_mou += f"**Τι θα κάνετε:** {catagory}\n"
    
    
    if Game: to_minima_mou += f"**Παιχνίδι:** {Game}\n"
    if Movie: to_minima_mou += f"**Ταινία:** {Movie}\n"
    if Drink: to_minima_mou += f"**Ποτό:** {Drink}\n"
    if Food: to_minima_mou += f"**Φαγητό:** {Food}\n"
    if Walk: to_minima_mou += f"**Βόλτα:** {Walk}\n"
    
    to_minima_mou += f"**Πότε:** {event_date} στις {event_time}"
    
    data = {"content": to_minima_mou}
    requests.post(webhook_url, json=data)

    st.success(" Τα δεδομένα στάλθηκαν")