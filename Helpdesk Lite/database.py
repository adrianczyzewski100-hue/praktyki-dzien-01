"""
moduł obsługi bazy danych sqlite dla aplikacji helpdesk lite.
"""

import sqlite3
from datetime import datetime

class Database:
    """klasa reprezentująca repozytorium bazy danych sqlite."""

    def __init__(self, db_name="helpdesk.db"):
        self.db_name = db_name
        self._init_db()

    def _get_connection(self):
        """pomocnicza metoda zwracająca połączenie do bazy danych."""
        return sqlite3.connect(self.db_name)

    def _init_db(self):
        """tworzy tabelę tickets w bazie danych, jeśli jeszcze nie istnieje."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'open',
                priority TEXT NOT NULL DEFAULT 'medium',
                created_at TEXT NOT NULL,
                closed_at TEXT
            );
            """)
            conn.commit()

    def add_ticket(self, user, description, priority):
        """dodaje nowy rekord do bazy danych przy użyciu zapytania INSERT."""
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
        INSERT INTO tickets (user, description, status, priority, created_at)
        VALUES (?, ?, 'open', ?, ?)
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (user, description, priority, created_at))
            ticket_id = cursor.lastrowid
            conn.commit()
        return self.get_ticket_by_id(ticket_id)

    def get_ticket_by_id(self, ticket_id):
        """wyszukuje pojedyncze zgłoszenie po id przy użyciu zapytania SELECT z WHERE."""
        query = "SELECT id, user, description, status, priority, created_at, closed_at FROM tickets WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (ticket_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "user": row[1],
                    "description": row[2],
                    "status": row[3],
                    "priority": row[4],
                    "created_at": row[5],
                    "closed_at": row[6]
                }
            return None

    def update_status(self, ticket_id, new_status, closed_at=None):
        """zmienia status zgłoszenia przy użyciu zapytania UPDATE."""
        query = "UPDATE tickets SET status = ?, closed_at = ? WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (new_status, closed_at, ticket_id))
            updated = cursor.rowcount > 0
            conn.commit()
            return updated

    def delete_ticket(self, ticket_id):
        """usuwa zgłoszenie z bazy danych przy użyciu zapytania DELETE."""
        query = "DELETE FROM tickets WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (ticket_id,))
            deleted = cursor.rowcount > 0
            conn.commit()
            return deleted

    def get_tickets(self, status=None, priority=None, open_only=False, sort_by=None, reverse=False):
        """pobiera przefiltrowane i posortowane zgłoszenia bezpośrednio z bazy danych."""
        query = "SELECT id, user, description, status, priority, created_at, closed_at FROM tickets"
        conditions = []
        params = []

        if open_only:
            conditions.append("LOWER(status) != 'closed'")
        elif status:
            conditions.append("LOWER(status) = LOWER(?)")
            params.append(status)

        if priority:
            conditions.append("LOWER(priority) = LOWER(?)")
            params.append(priority)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        if sort_by == "created_at":
            order_dir = "DESC" if reverse else "ASC"
            query += f" ORDER BY created_at {order_dir}"
        elif sort_by == "priority":
            order_dir = "DESC" if reverse else "ASC"
            query += f""" ORDER BY CASE LOWER(priority)
                WHEN 'high' THEN 1
                WHEN 'medium' THEN 2
                WHEN 'low' THEN 3
                ELSE 4 END {order_dir}"""

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()

        results = []
        for row in rows:
                results.append({
                    "id": row[0],
                    "user": row[1],
                    "description": row[2],
                    "status": row[3],
                    "priority": row[4],
                    "created_at": row[5],
                    "closed_at": row[6]
                })
        return results