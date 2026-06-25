import streamlit as st 
import datetime
import requests
import random

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

st.title("Game Roulette ")
st.write("Διαλέξτε παιχνίδι για τον Γιώργο. Πρέπει να το κάνω ή plat ή να έχω κάνει όλα τα side missions και το story.")

user_name = st.text_input("Γράψτε το όνομά σας:")


catagory = st.radio(
    "Τι θέλετε να παίξει ο Γιώργος;",
    ["Devil May Cry (1-5)", "Nioh (1, 2)", "Metaphor", "P5 Strikers", "Dark Souls (2, 3)", "Persona DLC", "Sekiro", "Ghost of Tsushima", "Prince of Persia", "Soul Hackers 2", "Little Nightmares 3", "Sackboy", "Nine Sols", "Blasphemous", "Final Fantasy", "Resident Evil 7 (με παρέα μόνο)", "Spider-Man(1, 2)"],
    index=None,
)

final_game = catagory

if st.button('Submit my picks '):
   
    webhook_url = st.secrets["discord_url3"] 
    
    
    with open("votes.txt", "a", encoding="utf-8") as myfile:
        myfile.write(f"{user_name}|{final_game}\n")

    to_minima_mou = f"Game Roulette!\n"
    to_minima_mou += f"Άτομο: {user_name}\n"
    to_minima_mou += f"Παιχνίδι: {final_game}\n"
        
    data = {"content": to_minima_mou}
    requests.post(webhook_url, json=data)

    st.success("Τα δεδομένα στάλθηκαν επιτυχώς!")

st.write("---")
st.header(" Admin")

admin_password = st.text_input("Κωδικός:", type="password")

if admin_password == "2905":
    if st.button("Λήξη Ψηφοφορίας & Αποτελέσματα "):
        
        webhook_url = st.secrets["discord_url"] 
        
        try:
            with open("votes.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                
            votes_count = {}
            for line in lines:
               
                parts = line.strip().split("|")
                if len(parts) == 2:
                    game = parts[1]
                    if game in votes_count:
                        votes_count[game] += 1
                    else:
                        votes_count[game] = 1
            
            if votes_count:
                results_msg = " Η ΨΗΦΟΦΟΡΙΑ ΕΚΛΕΙΣΕ! ΟΡΙΣΤΕ ΤΑ ΑΠΟΤΕΛΕΣΜΑΤΑ: \n\n"
                
                for game, count in votes_count.items():
                    bar = "🟩" * count  
                    results_msg += f"**{game}**: {bar} ({count})\n"
                
                max_votes = max(votes_count.values())
                
                tied_games = [game for game, count in votes_count.items() if count == max_votes]
                
                if len(tied_games) > 1:
                    winner = random.choice(tied_games)
                    tied_names = " και ".join(tied_games)
                    results_msg += f"\n ΕΧΟΥΜΕ ΙΣΟΠΑΛΙΑ! Τα παιχνίδια {tied_names} πήραν από {max_votes} ψήφους!"
                    results_msg += f"\n  Ο ΝΙΚΗΤΗΣ ΤΗΣ ΚΛΗΡΩΣΗΣ ΕΙΝΑΙ: {winner} \n"
                else:
                    winner = tied_games[0]
                    results_msg += f"\n Ο ΝΙΚΗΤΗΣ ΕΙΝΑΙ: {winner}  \n"
                
                data = {"content": results_msg}
                requests.post(webhook_url, json=data)
                
                st.success("Τα αποτελέσματα στάλθηκαν στο Discord με επιτυχία!")
                st.balloons()
                
                with open("votes.txt", "w", encoding="utf-8") as file:
                    pass
                st.info("Το αρχείο των ψήφων καθαρίστηκε αυτόματα και είναι έτοιμο για την επόμενη φορά! ")
                
            else:
                st.warning("Δεν υπάρχουν ψήφοι ακόμα στο αρχείο!")
                
        except FileNotFoundError:
            st.error("Το αρχείο των ψήφων δεν υπάρχει. Πρέπει να ψηφίσει κάποιος πρώτα!")