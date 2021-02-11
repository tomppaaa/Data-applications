 # -*- coding: utf-8 -*-

#Data application by Thomas Tran

import sqlite3
db = sqlite3.connect("kurssit-2.db")
db.isolation_level = None

#Lasketaan annettuna vuonna saatujen opintopisteiden yhteismäärä.
def hae_opintopisteet(vuosi: int):
    opintopisteet = db.execute(f"SELECT SUM(K.laajuus) FROM Kurssit K, Suoritukset S WHERE K.id = S.kurssi_id and S.paivays LIKE '{vuosi}%%'").fetchall()
    return f"Vuonna {vuosi} yhteenlaskettujen opintopisteiden määrä oli: {opintopisteet[0][0]}"

#Tulostetaan annetun opiskelijan kaikki suoritukset aikajärjestyksessä.
def hae_suoritukset(nimi: str):
    suoritukset = db.execute(f"SELECT K.nimi, K.laajuus, S.paivays, S.arvosana FROM Opiskelijat O, Suoritukset S, Kurssit K WHERE O.id = S.opiskelija_id and K.id = S.kurssi_id and O.nimi = '{nimi}' ORDER by S.paivays").fetchall()
    print("kurssi         op   päiväys        arvosana")
    for kurssi in suoritukset:
        if kurssi[1] > 9:
            print(f"{kurssi[0]}         {kurssi[1]}   {kurssi[2]}        {kurssi[3]}")
        else:
            print(f"{kurssi[0]}         {kurssi[1]}    {kurssi[2]}        {kurssi[3]}")
    return ""

#Tulostetaan annetun kurssin suoritusten arvosanojen jakauma.
def hae_kurssit(arvosanat: str):
    arvosanat = db.execute(f"SELECT S.arvosana, COUNT(S.arvosana) FROM Suoritukset S, Kurssit K WHERE K.id = S.kurssi_id and K.nimi = '{arvosanat}' GROUP BY S.arvosana").fetchall()
    for arvosana in arvosanat:
            print(f"Arvosana {arvosana[0]}: {arvosana[1]} kpl")
    return ""

#Tulostetaan top x eniten opintopisteitä antaneet opettajat.
def hae_top_opet(opet: int):
    top_opet = db.execute(f"SELECT O.nimi, SUM(K.laajuus) FROM Suoritukset S, Kurssit K, Opettajat O WHERE O.id = K.opettaja_id and K.id = S.kurssi_id GROUP BY O.nimi ORDER BY sum(K.laajuus) DESC LIMIT {opet}").fetchall()
    print("opettaja             op")
    for ope in top_opet:
        space = " " * (21 - len(ope[0]))
        print(f"{ope[0]}{space}{ope[1]}")    
    return ""
    
#Tulostetaan alkuvalikko.
print("1 - Hae opintopisteiden määrä.")
print("2 - Hae opiskelijan suoritukset aikajärjestyksessä.")
print("3 - Hae kurssin suorituksen arvosanojen jakauma.")
print("4 - Hae eniten opintopisteitä antaneet opettajat.")
print("5 - Sulje ohjelma.")

#Toimintorivit joista kutsutaan annetuilla parametreillä haetun toiminnon funktioita.
while True:
    toiminto = int(input("Valitse toiminto: "))

    if toiminto == 1:
        vuosi = input("Anna vuosi: ")
        print(hae_opintopisteet(vuosi))

    if toiminto == 2:
        nimi = input("Anna opiskelijan nimi:")
        print(hae_suoritukset(nimi))

    if toiminto == 3:
        kurssi = input("Anna kurssin nimi:")
        print(hae_kurssit(kurssi))

    if toiminto == 4:
        opet = input("Anna opettajien määrä:")
        print(hae_top_opet(opet))

    if toiminto == 5:
        break

    


        
    

