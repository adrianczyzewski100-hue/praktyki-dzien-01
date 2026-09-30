import sqlite3

conn = sqlite3.connect("baza.db")
cursor = conn.cursor()

cursor.execute("""
SELECT DISTINCT users.name
FROM users
JOIN orders ON users.id = orders.user_id
""")

wyniki = cursor.fetchall()
for user in wyniki:
    print(f"uzytkownik z zamowieniem: {user[0]}")

conn.close()