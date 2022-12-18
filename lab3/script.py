import sqlite3

con = sqlite3.connect("C:\Users\Xiaomi\WebProject\lab3\db.sqlite3")
cur = con.cursos()
cur.execute("SELECT * FROM ")