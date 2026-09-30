"""
moduł logiki biznesowej zarządzający zgłoszeniami przez klasę Database.
"""

import csv
from datetime import datetime
from tickets import Ticket
from database import Database

class Helpdesk:
    """klasa zarządzająca zgłoszeniami przy użyciu repozytorium bazy danych."""

    def __init__(self, db_name="helpdesk.db"):
        self.db = Database(db_name)

    def add_ticket(self, user, description, priority):
        """tworzy i zapisuje nowy ticket w bazie danych."""
        ticket_data = self.db.add_ticket(user, description, priority)
        return Ticket.from_dict(ticket_data)

    def find_ticket(self, ticket_id):
        """pobiera pojedynczy ticket bezpośrednio z bazy danych po id."""
        ticket_data = self.db.get_ticket_by_id(ticket_id)
        return Ticket.from_dict(ticket_data) if ticket_data else None

    def change_status(self, ticket_id, new_status):
        """zmienia status ticketu w bazie danych i ustawia datę zamknięcia jeśli status to closed."""
        closed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if new_status.lower() == "closed" else None
        return self.db.update_status(ticket_id, new_status, closed_at)

    def delete_ticket(self, ticket_id):
        """usuwa ticket z bazy danych po id."""
        return self.db.delete_ticket(ticket_id)

    def get_all_tickets(self):
        """pobiera wszystkie zgłoszenia z bazy danych."""
        rows = self.db.get_tickets()
        return [Ticket.from_dict(data) for data in rows]

    def get_open_tickets(self):
        """pobiera tylko otwarte zgłoszenia z bazy danych."""
        rows = self.db.get_tickets(open_only=True)
        return [Ticket.from_dict(data) for data in rows]

    def filter_tickets(self, status=None, priority=None, open_only=False):
        """filtruje zgłoszenia zapytaniem SQL."""
        rows = self.db.get_tickets(status=status, priority=priority, open_only=open_only)
        return [Ticket.from_dict(data) for data in rows]

    def sort_tickets(self, tickets_list, by="created_at", reverse=False):
        """sortuje przekazaną listę obiektów Ticket według wybranego pola."""
        result = list(tickets_list)
        if by == "created_at":
            result.sort(key=lambda t: t.created_at, reverse=reverse)
        elif by == "priority":
            priority_order = {"high": 1, "medium": 2, "low": 3}
            result.sort(key=lambda t: priority_order.get(t.priority.lower(), 99), reverse=reverse)
        return result

    def export_to_csv(self, open_only=False):
        """generuje raport w formacie csv czytelnym dla programu excel."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        suffix = "otwarte" if open_only else "wszystkie"
        filename = f"raport_ticketow_{suffix}_{timestamp}.csv"

        tickets_to_export = self.get_open_tickets() if open_only else self.get_all_tickets()
        headers = ["ID", "Użytkownik", "Opis", "Status", "Priorytet", "Data utworzenia", "Data zamknięcia"]

        with open(filename, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(headers)

            for t in tickets_to_export:
                writer.writerow([
                    t.id,
                    t.user,
                    t.description,
                    t.status,
                    t.priority,
                    t.created_at,
                    t.closed_at if t.closed_at else ""
                ])

        return filename, len(tickets_to_export)