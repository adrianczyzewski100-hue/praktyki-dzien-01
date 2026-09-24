"""
moduł reprezentujący pojedyncze zgłoszenie (ticket) w systemie helpdesk.
"""

from validators import validate_priority

class Ticket:
    """klasa reprezentująca dane i zachowanie pojedynczego ticketu."""
    def __init__(self, id, user, description, status="open", priority="low"):
        self.id = id
        self.user = user
        self.description = description
        self.status = status
        self.priority = priority

    def close(self):
        """zamyka zgłoszenie, zmieniając jego status na closed."""
        self.status = "closed"

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
            "priority": self.priority
        }

    @staticmethod
    def from_dict(data):
        """tworzy obiekt ticketu na podstawie słownika wczytanego z json."""
        return Ticket(
            id=data["id"],
            user=data["user"],
            description=data["description"],
            status=data["status"],
            priority=data["priority"]
        )

    def __str__(self):
        """zwraca czytelną reprezentację tekstową ticketu."""
        return (f"Ticket {self.id}: "
                f"user={self.user}, "
                f"description={self.description}, "
                f"status={self.status}, "
                f"priority={self.priority}")