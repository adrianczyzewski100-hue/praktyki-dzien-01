"""
moduł reprezentujący model pojedynczego zgłoszenia (ticketu).
"""

from datetime import datetime

class Ticket:
    """klasa opisująca strukturę i zachowanie pojedynczego zgłoszenia."""

    def __init__(self, id, user, description, status="open", priority="medium", created_at=None, closed_at=None):
        self.id = id
        self.user = user
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.closed_at = closed_at

    def close(self):
        """zamyka zgłoszenie i ustawia datę zamknięcia."""
        self.status = "closed"
        self.closed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """konwertuje obiekt ticketu na słownik gotowy do zapisu json."""
        return {
            "id": self.id,
            "user": self.user,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "created_at": self.created_at,
            "closed_at": self.closed_at
        }

    @classmethod
    def from_dict(cls, data):
        """tworzy obiekt Ticket na podstawie słownika."""
        return cls(
            id=data["id"],
            user=data["user"],
            description=data["description"],
            status=data.get("status", "open"),
            priority=data.get("priority", "medium"),
            created_at=data.get("created_at"),
            closed_at=data.get("closed_at")
        )

    def __str__(self):
        closed_info = f" | zamknięto: {self.closed_at}" if self.closed_at else ""
        return f"[{self.id}] {self.user} | {self.description} | status: {self.status} | priorytet: {self.priority} | utworzono: {self.created_at}{closed_info}"