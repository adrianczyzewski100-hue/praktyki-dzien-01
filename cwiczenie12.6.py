import sqlite3

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

nazwa = "o'connor"

try:
    cursor.execute(f"INSERT INTO uzytkownicy (nazwa) VALUES ('{nazwa}')")
except sqlite3.OperationalError as e:
    print(f"błąd: {e}")

conn.close()