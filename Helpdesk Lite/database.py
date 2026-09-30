import sqlite3
from datetime import datetime

class Database:

    def __init__(self, db_name="helpdesk.db"):
        self.db_name = db_name
        self._init_db()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def _init_db(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                department TEXT NOT NULL
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'open',
                priority TEXT NOT NULL DEFAULT 'medium',
                created_at TEXT NOT NULL,
                closed_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT
            );
            """)
            conn.commit()

    def add_user(self, name, department):
        query = "INSERT INTO users (name, department) VALUES (?, ?)"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (name, department))
            user_id = cursor.lastrowid
            conn.commit()
        return self.get_user_by_id(user_id)

    def get_user_by_id(self, user_id):
        query = "SELECT id, name, department FROM users WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "name": row[1], "department": row[2]}
            return None

    def get_all_users(self):
        query = "SELECT id, name, department FROM users ORDER BY name ASC"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [{"id": r[0], "name": r[1], "department": r[2]} for r in rows]

    def add_ticket(self, user_id, description, priority):
        if not self.get_user_by_id(user_id):
            raise ValueError(f"użytkownik o ID {user_id} nie istnieje")

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
        INSERT INTO tickets (user_id, description, status, priority, created_at)
        VALUES (?, ?, 'open', ?, ?)
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (user_id, description, priority, created_at))
            ticket_id = cursor.lastrowid
            conn.commit()
        return self.get_ticket_by_id(ticket_id)

    def get_ticket_by_id(self, ticket_id):
        query = """
        SELECT t.id, t.user_id, u.name, u.department, t.description, t.status, t.priority, t.created_at, t.closed_at
        FROM tickets t
        JOIN users u ON t.user_id = u.id
        WHERE t.id = ?
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (ticket_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "user_id": row[1],
                    "user_name": row[2],
                    "department": row[3],
                    "description": row[4],
                    "status": row[5],
                    "priority": row[6],
                    "created_at": row[7],
                    "closed_at": row[8]
                }
            return None

    def update_status(self, ticket_id, new_status, closed_at=None):
        query = "UPDATE tickets SET status = ?, closed_at = ? WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (new_status, closed_at, ticket_id))
            updated = cursor.rowcount > 0
            conn.commit()
            return updated

    def delete_ticket(self, ticket_id):
        query = "DELETE FROM tickets WHERE id = ?"
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (ticket_id,))
            deleted = cursor.rowcount > 0
            conn.commit()
            return deleted

    def get_tickets(self, status=None, priority=None, user_id=None, open_only=False, sort_by=None, reverse=False):
        query = """
        SELECT t.id, t.user_id, u.name, u.department, t.description, t.status, t.priority, t.created_at, t.closed_at
        FROM tickets t
        JOIN users u ON t.user_id = u.id
        """
        conditions = []
        params = []

        if open_only:
            conditions.append("LOWER(t.status) != 'closed'")
        elif status:
            conditions.append("LOWER(t.status) = LOWER(?)")
            params.append(status)

        if priority:
            conditions.append("LOWER(t.priority) = LOWER(?)")
            params.append(priority)

        if user_id is not None:
            conditions.append("t.user_id = ?")
            params.append(user_id)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        if sort_by == "created_at":
            order_dir = "DESC" if reverse else "ASC"
            query += f" ORDER BY t.created_at {order_dir}"
        elif sort_by == "priority":
            order_dir = "DESC" if reverse else "ASC"
            query += f""" ORDER BY CASE LOWER(t.priority)
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
                "user_id": row[1],
                "user_name": row[2],
                "department": row[3],
                "description": row[4],
                "status": row[5],
                "priority": row[6],
                "created_at": row[7],
                "closed_at": row[8]
            })
        return results