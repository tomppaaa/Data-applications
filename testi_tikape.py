import sqlite3
import os
import random
import string
import time

os.system("rm testi.db")

db = sqlite3.connect("testi.db")
db.isolation_level = None

db.execute("CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")

n = (10**6)+1
vuosi = [x for x in range(1900,2001)]
mlista = []
for j in range(1000):
    mjono = ""
    for i in range(1,7):
        mjono = mjono + random.choice(string.ascii_letters)
    mlista.append(mjono)

#db.execute("CREATE INDEX idx_vuosi ON Elokuvat (vuosi)") #Tehokkaan indeksin luominen ennen rivien lisäämistä.

alku = time.time()
db.execute("BEGIN")

for i in range(1,n):
    db.execute(f"INSERT INTO Elokuvat (nimi, vuosi) VALUES ('{random.choice(mlista)}', {random.choice(vuosi)} )")
print(f"Aikaa meni rivien lisäykseen {time.time()-alku} sekuntia")

db.execute("CREATE INDEX idx_vuosi ON Elokuvat (vuosi)") #Tehokkaan indeksin lisääminen ennen kyselyitä.

alku1 = time.time()
for i in range(1,1001):
    db.execute(f"SELECT COUNT(*) from Elokuvat E WHERE E.vuosi = {random.choice(vuosi)}").fetchall()

db.execute("COMMIT")   
print(f"Aikaa meni kyselyyn lisäykseen {time.time()-alku1} sekuntia")

