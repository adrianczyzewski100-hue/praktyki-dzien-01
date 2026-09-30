import sqlite3

def init_database():
    conn = sqlite3.connect("helpdesk.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'open',
        priority TEXT NOT NULL DEFAULT 'medium',
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        closed_at TEXT
    );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    print("baza helpdesk.db oraz tabela tickets zostaly utworzone")