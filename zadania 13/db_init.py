import sqlite3

conn = sqlite3.connect("baza.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
""")

users_data = [
    ("adrian",),
    ("jan",),
    ("anna",)
]

cursor.executemany("INSERT INTO users (name) VALUES (?)", users_data)

orders_data = [
    (1, "laptop"),
    (1, "myszka"),
    (2, "klawiatura")
]

cursor.executemany("INSERT INTO orders (user_id, product) VALUES (?, ?)", orders_data)

conn.commit()
conn.close()