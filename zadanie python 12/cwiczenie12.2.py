import sqlite3

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

uzytkownik_id = 1
cursor.execute('SELECT * FROM uzytkownicy WHERE id = ?', (uzytkownik_id,))
uzytkownik = cursor.fetchone()

print(uzytkownik)

conn.close()