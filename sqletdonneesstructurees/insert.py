import sqlite3

with sqlite3.connect("database.db") as con:
    cur = con.cursor()
    cur.execute("INSERT INTO etudiants (nom,addr,pin) VALUES (?,?,?)", (" John Doe" ," 122 rue paul armangot" ," 123"))
    con.commit()
con.close()

