import sqlite3

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

uzytkownik_id = 1

cursor.execute('DELETE FROM uzytkownicy WHERE id = ?', (uzytkownik_id,))

conn.commit()
conn.close()