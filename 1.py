import streamlit as st 
import datetime

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
        
        st.success(" Τα δεδομένα στάλθηκαν")