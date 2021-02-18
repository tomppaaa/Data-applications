import sqlite3

db = sqlite3.connect("testi.db")
db.isolation_level = None

laskuri = 1
db.execute("BEGIN")
for i in range(1,5001):
    db.execute(f"SELECT MAX(x) from Testi").fetchall()
    try:
        db.execute(f"INSERT INTO Testi (x) VALUES ({laskuri})")
    except:

        db.execute("ROLLBACK")
    laskuri += 1
    print(db.execute(f"SELECT MAX(x) from Testi T").fetchall()[0][0])

db.execute("COMMIT")  