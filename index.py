import json
import os
import random
leaderboard_file ="alle_stemmene.json"
partier = ["ap","krf","mdg","frp","sp","sv","rødt","høyre","venstre"]
teller = 0


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
    return random.randint(1, 94) 

def valget(): #denne variablen kjører valger
    global stemme
    stemme = input("Avgi din stemme\n").lower() #her skriver du hva du vil stemme på
    if stemme in alle_stemmene: #denne gjør at hvis det partiet du har stemt på finnes i "partier" variablen så skal den plusse på 1 stemme til x parti
        alle_stemmene[stemme] +=1
        save_leaderboard()
        print("Du stemte på",stemme)
    else:
        print("ugyldig parti") #hvis du skriver ett parti som ikke er i variablen så skriver den "ugyldig"

def registrer_ki_stemme():
    tall = ki_stemme()
    if tall in range(1, 5):      
        alle_stemmene["venstre"] += 1
    elif tall in range(5, 9):    
        alle_stemmene["krf"] += 1
    elif tall in range(9, 14):   
        alle_stemmene["mdg"] += 1
    elif tall in range(14, 19):  
        alle_stemmene["rødt"] += 1
    elif tall in range(19, 24):  
        alle_stemmene["sp"] += 1
    elif tall in range(24, 29):  
        alle_stemmene["sv"] += 1
    elif tall in range(29, 43):  
        alle_stemmene["høyre"] += 1
    elif tall in range(43, 67):  
        alle_stemmene["frp"] += 1
    elif tall in range(67, 95):  
        alle_stemmene["ap"] += 1


def kjør_valget():
    valget()
    antall = int(input("Hvor mange KI-stemmer vil du generere? "))
    for _ in range(antall):
        registrer_ki_stemme()
    save_leaderboard()
    show_leaderboard()

    
kjør_valget()

