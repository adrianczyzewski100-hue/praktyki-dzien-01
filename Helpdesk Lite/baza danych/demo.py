import sqlite3

def run_demo():
    conn = sqlite3.connect("helpdesk.db")
    cursor = conn.cursor()

    cursor.executescript("""
    DROP TABLE IF EXISTS tickets;

    CREATE TABLE tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'open',
        priority TEXT NOT NULL DEFAULT 'medium',
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        closed_at TEXT
    );

    INSERT INTO tickets (user, description, priority) VALUES ('anna_kowalska', 'Brak dostępu do poczty e-mail', 'high');
    INSERT INTO tickets (user, description, priority) VALUES ('piotr_nowak', 'Problem z drukarką w biurze', 'low');
    INSERT INTO tickets (user, description, priority) VALUES ('pavel_novak', 'Myszka komputerowa nie działa', 'low');
    INSERT INTO tickets (user, description, status, priority, closed_at) VALUES ('jan_zielinski', 'Zapomniane hasło', 'closed', 'medium', '2026-09-30 10:00:00');
    """)
    conn.commit()

    print("--- OTWARTY RAPORT (SELECT z WHERE i ORDER BY) ---")
    cursor.execute("""
        SELECT id, user, description, status, priority, created_at
        FROM tickets
        WHERE status = 'open'
        ORDER BY created_at DESC
    """)
    for row in cursor.fetchall():
        print(row)

    print("\n--- ZMIANA STATUSU (UPDATE) ---")
    cursor.execute("UPDATE tickets SET status = 'closed', closed_at = CURRENT_TIMESTAMP WHERE id = 1")
    conn.commit()

    print("\n--- USUNIĘCIE TICKETU (DELETE) ---")
    cursor.execute("DELETE FROM tickets WHERE id = 3")
    conn.commit()

    print("\n--- STAN BAZY PO ZMIANACH ---")
    cursor.execute("SELECT * FROM tickets")
    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    run_demo()