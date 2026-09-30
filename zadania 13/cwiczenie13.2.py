import sqlite3

conn = sqlite3.connect("baza.db")
cursor = conn.cursor()

cursor.execute("""
SELECT users.name, orders.product
FROM users
JOIN orders ON users.id = orders.user_id
""")

wyniki = cursor.fetchall()
for row in wyniki:
    print(f"uzytkownik: {row[0]}, zamowienie: {row[1]}")

conn.close()