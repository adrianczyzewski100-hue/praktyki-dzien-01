"""
moduł reprezentujący pojedyncze zgłoszenie (ticket) w systemie helpdesk.
"""

from datetime import datetime
from validators import validate_priority

class Ticket:
    """klasa reprezentująca dane i zachowanie pojedynczego ticketu."""

    def __init__(self, id, user, description, status="open", priority="low", created_at=None, closed_at=None):
        # unikalny identyfikator ticketu
        self.id = id
        # nazwa użytkownika zgłaszającego problem
        self.user = user
        # opis zgłoszenia
        self.description = description
        # status ticketu (np. open, closed)
        self.status = status
        # priorytet zgłoszenia (low, medium, high)
        self.priority = priority
        # data utworzenia ticketu (jeśli brak, pobierana jest aktualna data)
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # data zamknięcia ticketu (ustawiana przy wywołaniu close())
        self.closed_at = closed_at

    def close(self):
        """zamyka zgłoszenie, zmieniając jego status na closed i zapisując datę zamknięcia."""
        self.status = "closed"
        self.closed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def change_priority(self, new_priority):
        """zmienia priorytet zgłoszenia po wcześniejszej walidacji."""
        if validate_priority(new_priority):
            self.priority = new_priority
            return True
        return False

    def to_dict(self):
        """konwertuje obiekt ticketu na słownik gotowy do zapisu w json."""
        return {
            "id": self.id,
            "user": self.user,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "created_at": self.created_at,
            "closed_at": self.closed_at
        }

    @staticmethod
    def from_dict(data):
        """tworzy obiekt ticketu na podstawie słownika wczytanego z json."""
        return Ticket(
            id=data["id"],
            user=data["user"],
            description=data["description"],
            status=data["status"],
            priority=data["priority"],
            created_at=data.get("created_at"),
            closed_at=data.get("closed_at")
        )

    def __str__(self):
        """zwraca czytelną reprezentację tekstową ticketu."""
        closed_info = f", closed_at={self.closed_at}" if self.closed_at else ""
        return (f"Ticket {self.id}: "
                f"user={self.user}, "
                f"description={self.description}, "
                f"status={self.status}, "
                f"priority={self.priority}, "
                f"created_at={self.created_at}"
                f"{closed_info}")