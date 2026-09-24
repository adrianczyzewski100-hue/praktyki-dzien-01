"""
moduł logiki biznesowej zarządzający kolekcją ticketów.
"""

from tickets import Ticket
from storage import Storage

class Helpdesk:
    """klasa zarządzająca dodawaniem, usuwaniem, wyszukiwaniem i filtrowaniem ticketów."""
    def __init__(self):
        self.storage = Storage()
        # wczytanie surowych danych z pliku i konwersja na obiekty klasy Ticket
        raw_data = self.storage.load()
        self.tickets = [Ticket.from_dict(item) for item in raw_data]
        # automatyczne wyznaczenie kolejnego dostępnego id
        self.next_id = max((t.id for t in self.tickets), default=0) + 1

    def _save(self):
        """pomocnicza metoda prywatna zapisująca aktualny stan ticketów do pliku."""
        self.storage.save([t.to_dict() for t in self.tickets])

    def add_ticket(self, user, description, priority):
        """tworzy nowy ticket, dodaje go do listy i zapisuje zmiany."""
        ticket = Ticket(self.next_id, user, description, status="open", priority=priority)
        self.tickets.append(ticket)
        self.next_id += 1
        self._save()
        return ticket

    def find_ticket(self, ticket_id):
        """wyszukuje ticket po jego id. zwraca obiekt Ticket lub None."""
        return next((t for t in self.tickets if t.id == ticket_id), None)

    def change_status(self, ticket_id, new_status):
        """zmienia status wskazanego ticketu i zapisuje zmiany."""
        ticket = self.find_ticket(ticket_id)
        if ticket:
            ticket.status = new_status
            self._save()
            return True
        return False

    def delete_ticket(self, ticket_id):
        """usuwa ticket o podanym id i zapisuje stan bazy."""
        ticket = self.find_ticket(ticket_id)
        if ticket:
            self.tickets = [t for t in self.tickets if t.id != ticket_id]
            self._save()
            return True
        return False

    def get_all_tickets(self):
        """zwraca listę wszystkich ticketów."""
        return self.tickets
#
    def filter_tickets(self, status=None, priority=None):
        """filtruje tickety według podanego statusu lub priorytetu."""
        result = self.tickets
        if status:
            result = [t for t in result if t.status.lower() == status.lower()]
        if priority:
            result = [t for t in result if t.priority.lower() == priority.lower()]
        return result