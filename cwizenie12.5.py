import sqlite3

conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

szukany_fragment = 'jan'
cursor.execute('SELECT * FROM uzytkownicy WHERE nazwa LIKE ?', (f'%{szukany_fragment}%',))
wyniki = cursor.fetchall()

print(wyniki)

conn.close()