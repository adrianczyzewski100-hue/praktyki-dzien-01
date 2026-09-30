import sqlite3

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

nowa_nazwa = 'piotr nowak'
uzytkownik_id = 1

cursor.execute('UPDATE uzytkownicy SET nazwa = ? WHERE id = ?', (nowa_nazwa, uzytkownik_id))

conn.commit()
conn.close()