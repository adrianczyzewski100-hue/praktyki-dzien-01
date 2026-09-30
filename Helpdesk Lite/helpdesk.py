import csv
from datetime import datetime
from database import Database

class Helpdesk:

    def __init__(self, db_name="helpdesk.db"):
        self.db = Database(db_name)

    def add_user(self, name, department):
        return self.db.add_user(name, department)

    def get_users(self):
        return self.db.get_all_users()

    def add_ticket(self, user_id, description, priority):
        return self.db.add_ticket(user_id, description, priority)

    def find_ticket(self, ticket_id):
        return self.db.get_ticket_by_id(ticket_id)

    def get_all_tickets(self):
        return self.db.get_tickets()

    def get_open_tickets(self):
        return self.db.get_tickets(open_only=True)

    def get_tickets_by_user(self, user_id):
        return self.db.get_tickets(user_id=user_id)

    def change_status(self, ticket_id, new_status):
        closed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if new_status.lower() == "closed" else None
        return self.db.update_status(ticket_id, new_status, closed_at)

    def delete_ticket(self, ticket_id):
        return self.db.delete_ticket(ticket_id)

    def filter_tickets(self, status=None, priority=None, user_id=None, open_only=False, sort_by=None, reverse=False):
        return self.db.get_tickets(status=status, priority=priority, user_id=user_id, open_only=open_only, sort_by=sort_by, reverse=reverse)

    def export_to_csv(self, open_only=False):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        suffix = "otwarte" if open_only else "wszystkie"
        filename = f"raport_ticketow_{suffix}_{timestamp}.csv"

        tickets_to_export = self.get_open_tickets() if open_only else self.get_all_tickets()
        headers = ["ID", "ID Użytkownika", "Użytkownik", "Dział", "Opis", "Status", "Priorytet", "Data utworzenia", "Data zamknięcia"]

        with open(filename, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(headers)

            for t in tickets_to_export:
                writer.writerow([
                    t["id"],
                    t["user_id"],
                    t["user_name"],
                    t["department"],
                    t["description"],
                    t["status"],
                    t["priority"],
                    t["created_at"],
                    t["closed_at"] if t["closed_at"] else ""
                ])

        return filename, len(tickets_to_export)