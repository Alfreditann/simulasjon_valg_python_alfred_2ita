import json
import os 
leaderboard_file ="alle_stemmene.json"

if os.path.exists(leaderboard_file): #skjekker om stemme filen finnes
    with open (leaderboard_file,"r") as f: #bruker den riktige filen som "leaderboard" som en read
        alle_stemmene = json.load(f) 
else:
    alle_stemmene = {
        "ap": 0,
        "krf": 0,
        "mdg": 0,
        "frp": 0,
        "sp": 0,
        "sv": 0,
        "rødt": 0,
        "høyre": 0,
        "venstre": 0
    }


def save_leaderboard():
    with open(leaderboard_file, "w") as f:
        json.dump(alle_stemmene, f, indent=4, ensure_ascii=False)


partier = ["ap","krf","mdg","frp","sp","sv","rødt","høyre","venstre"]

def valget():
    stemme = input("Avgi din stemme\n").lower()
    if stemme in alle_stemmene:
        alle_stemmene[stemme] +=1
        save_leaderboard()
        print("Du stemte på",stemme)
    else:
        print("ugyldig parti")
valget()