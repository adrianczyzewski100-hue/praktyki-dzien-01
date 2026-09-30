import sqlite3

conn = sqlite3.connect("baza.db")
cursor = conn.cursor()

nazwa = "jan kowalski"
cursor.execute("insert into uzytkownicy (nazwa) VALUES (?)", (nazwa,))

conn.commit()
conn.close()