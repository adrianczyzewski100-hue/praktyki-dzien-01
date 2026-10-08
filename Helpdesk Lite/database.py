import sqlite3
from datetime import datetime
from logger_config import setup_logger

logger = setup_logger()

class DatabaseError(Exception):
    pass

class Database:

    def __init__(self, db_name="helpdesk.db"):
        self.db_name = db_name
        self._init_db()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def _init_db(self):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("PRAGMA table_info(tickets);")
                columns = [column[1] for column in cursor.fetchall()]

                if columns and "user_id" not in columns:
                    logger.warning("wykryto starą strukturę bazy danych. usuwanie starej tabeli tickets.")
                    cursor.execute("DROP TABLE tickets;")

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
                logger.info("baza danych została pomyślnie zainicjalizowana.")
        except sqlite3.Error as e:
            logger.error(f"błąd podczas inicjalizacji bazy danych: {e}", exc_info=True)
            raise DatabaseError("nie udało się zainicjalizować bazy danych.")

    def add_user(self, name, department):
        query = "INSERT INTO users (name, department) VALUES (?, ?)"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (name, department))
                user_id = cursor.lastrowid
                conn.commit()
            logger.info(f"dodano nowego użytkownika: {name} (ID: {user_id})")
            return self.get_user_by_id(user_id)
        except sqlite3.IntegrityError:
            logger.warning(f"odrzucono próbę dodania istniejącego użytkownika: {name}")
            raise ValueError(f"użytkownik o nazwie {name} już istnieje.")
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy dodawaniu użytkownika {name}: {e}", exc_info=True)
            raise DatabaseError("nie udało się dodać użytkownika.")

    def get_user_by_id(self, user_id):
        query = "SELECT id, name, department FROM users WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (user_id,))
                row = cursor.fetchone()
                if row:
                    return {"id": row[0], "name": row[1], "department": row[2]}
                logger.warning(f"nie znaleziono użytkownika o ID: {user_id}")
                return None
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy pobieraniu użytkownika ID {user_id}: {e}", exc_info=True)
            raise DatabaseError("nie udało się pobrać danych użytkownika.")

    def get_all_users(self):
        query = "SELECT id, name, department FROM users ORDER BY name ASC"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                return [{"id": r[0], "name": r[1], "department": r[2]} for r in rows]
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy pobieraniu listy użytkowników: {e}", exc_info=True)
            raise DatabaseError("nie udało się pobrać listy użytkowników.")

    def add_ticket(self, user_id, description, priority):
        if not self.get_user_by_id(user_id):
            logger.warning(f"odrzucono dodanie ticketu: brak użytkownika o ID {user_id}")
            raise ValueError(f"użytkownik o ID {user_id} nie istnieje")

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = """
        INSERT INTO tickets (user_id, description, status, priority, created_at)
        VALUES (?, ?, 'open', ?, ?)
        """
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (user_id, description, priority, created_at))
                ticket_id = cursor.lastrowid
                conn.commit()
            logger.info(f"utworzono nowy ticket nr {ticket_id} dla użytkownika ID {user_id}")
            return self.get_ticket_by_id(ticket_id)
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy dodawaniu ticketu dla użytkownika {user_id}: {e}", exc_info=True)
            raise DatabaseError("nie udało się utworzyć zgłoszenia.")

    def get_ticket_by_id(self, ticket_id):
        query = """
        SELECT t.id, t.user_id, u.name, u.department, t.description, t.status, t.priority, t.created_at, t.closed_at
        FROM tickets t
        JOIN users u ON t.user_id = u.id
        WHERE t.id = ?
        """
        try:
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
                logger.warning(f"nie znaleziono ticketu o ID {ticket_id}")
                return None
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy szukaniu ticketu ID {ticket_id}: {e}", exc_info=True)
            raise DatabaseError("nie udało się pobrać danych zgłoszenia.")

    def update_status(self, ticket_id, new_status, closed_at=None):
        query = "UPDATE tickets SET status = ?, closed_at = ? WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (new_status, closed_at, ticket_id))
                updated = cursor.rowcount > 0
                conn.commit()
                if updated:
                    logger.info(f"zmieniono status ticketu nr {ticket_id} na {new_status}")
                else:
                    logger.warning(f"nie zmieniono statusu: nie znaleziono ticketu nr {ticket_id}")
                return updated
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy zmianie statusu ticketu nr {ticket_id}: {e}", exc_info=True)
            raise DatabaseError("nie udało się zaktualizować statusu.")

    def delete_ticket(self, ticket_id):
        query = "DELETE FROM tickets WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, (ticket_id,))
                deleted = cursor.rowcount > 0
                conn.commit()
                if deleted:
                    logger.info(f"usunięto ticket nr {ticket_id}")
                else:
                    logger.warning(f"nie usunięto ticketu: brak nr {ticket_id}")
                return deleted
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy usuwaniu ticketu nr {ticket_id}: {e}", exc_info=True)
            raise DatabaseError("nie udało się usunąć zgłoszenia.")

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

        try:
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
        except sqlite3.Error as e:
            logger.error(f"błąd bazy przy pobieraniu listy ticketów: {e}", exc_info=True)
            raise DatabaseError("nie udało się pobrać zgłoszeń z bazy.")