import sqlite3

db = sqlite3.connect("testi.db")
db.isolation_level = None

laskuri = 1

for i in range(1,5001):
    db.execute(f"SELECT MAX(x) from Testi").fetchall()
    db.execute(f"INSERT OR REPLACE INTO Testi (x) VALUES ({laskuri})")

    laskuri += 1
    print(db.execute(f"SELECT MAX(x) from Testi T").fetchall()[0][0])

