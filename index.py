import json
import os
import random
leaderboard_file ="alle_stemmene.json"
partier = ["ap","krf","mdg","frp","sp","sv","rødt","høyre","venstre"]

if os.path.exists(leaderboard_file): #skjekker om stemme filen finnes
    with open (leaderboard_file,"r") as f: #bruker den riktige filen som "leaderboard" som en read
        alle_stemmene = json.load(f) #loader json filen
else: #hvis json filen ikke finnes så lager den en.
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


def save_leaderboard(): #lagrer leaderboardet av stemmende
    with open(leaderboard_file, "w") as f:
        json.dump(alle_stemmene, f, indent=4, ensure_ascii=False)

def show_leaderboard():#viser leaderboardet. den viser parti navnet og hvor mange stemmer de har fått
    print("\nALLE STEMMENE")
    for navn, stemme_amount in alle_stemmene.items():
        print(f"{navn}: {stemme_amount}")

def ki_stemme():
    return random.choice(1,94)
def valget(): #denne variablen kjører valger
    global stemme
    stemme = input("Avgi din stemme\n").lower() #her skriver du hva du vil stemme på
    if stemme in alle_stemmene: #denne gjør at hvis det partiet du har stemt på finnes i "partier" variablen så skal den plusse på 1 stemme til x parti
        alle_stemmene[stemme] +=1
        save_leaderboard()
        print("Du stemte på",stemme)
    else:
        print("ugyldig parti") #hvis du skriver ett parti som ikke er i variablen så skriver den "ugyldig"
def kjør_valget():
    valget()
    show_leaderboard()
    ki_stemme()
    if ki_stemme() == 1 or 2 or 3 or 4:
        stemme["venstre"] +=1
    elif ki_stemme() == 5 or 6 or 7 or 8:
        stemme["krf"] +=1
    elif ki_stemme == 9 or 10 or 11 or 12 or 13:
        stemme["mdg"] +=1
    elif ki_stemme == 14 or 15 or 16 or 17 or 18:
        stemme["rødt"] +=1
    elif ki_stemme == 19 or 20 or 21 or 22 or 23:
        stemme["sp"] +=1
    elif ki_stemme == 24 or 25 or 26 or 27 or 28:
        stemme["sv"] +=1
    elif ki_stemme == 29 or 30 or 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 40 or 41 or 42:
        stemme ["høyre"] +=1
    elif ki_stemme == 43 or 44 or 45 or 46 or 47 or 48 or 49 or 50 or 51 or 52 or 53 or 54 or 55 or 56 or 57 or 58 or 59 or 60 or 61 or 62 or 63 or 64 or 65 or 66:
        stemme["frp"] +=1
    elif ki_stemme == 67 or 68 or 69 or 70 or 71 or 72 or 73 or 74 or 75 or 76 or 77 or 78 or 79 or 80 or 81 or 82 or 83 or 84 or 85 or 86 or 87 or 88 or 89 or 90 or 91 or 92 or 93 or 94:
        stemme ["ap"] +=1


