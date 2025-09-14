import json
import os
import random
import math
leaderboard_file ="alle_stemmene.json"
partier = ["ap","krf","mdg","frp","sp","sv","rødt","høyre","venstre"]
teller = 0
fylker = ["Akershus","Buskerud", "Finnmark","Innlandet","Møre og Romsal","Oslo","Rogaland","Telemark","Trøndelag","Vestfold","Vestland","Viken og Østfold"]
mandater = 150
mandaterPrFylke = mandater / len(fylker)

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
    elif tall in range(67, 94):  
        alle_stemmene["ap"] += 1

def prosentStemmer():
    total = sum(alle_stemmene.values())
    for parti, antall in alle_stemmene.items():
       prosent = (antall / total) * 100
       print(f"{parti}: {prosent:.1f}%")
 
def beregeMandater():
    # tildelt_mandat =[]
    # stemmer = dict(sorted(alle_stemmene.items(), key=lambda item: item[1], reverse=True))
    # for navn, stemme_amount in stemmer.items():
    #     stemmer[navn] = stemme_amount/1.4
        
    
    # for _ in range(mandater):
        # stemmer = dict(sorted(stemmer.items(), key=lambda item: item[1], reverse=True))
        # first_item = next(iter(stemmer.items()))
        # first_key, first_value = first_item
       
        # if(first_key in tildelt_mandat):
        #     tildelt_mandat[first_key] += 1
        #     stemmer[first_key] = first_value / 
        # else:
        #     tildelt_mandat[first_key] = 1
        #     stemmer[first_key] = first_value / 3

        # print(tildelt_mandat)

    
    




     total = sum(alle_stemmene.values())
     for navn, stemme_amount in alle_stemmene.items():
         print(f"{navn} fikk: {round(mandater*(stemme_amount/total))} mandater!")


def kjør_valget():
    valget()
    global antall
    antall = int(input("Hvor mange KI-stemmer vil du generere? "))
    for _ in range(antall):
        registrer_ki_stemme()
    save_leaderboard()
    prosentStemmer()

    
beregeMandater()

