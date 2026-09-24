"""
moduł logiki biznesowej zarządzający kolekcją ticketów.
"""

from tickets import Ticket
from storage import Storage

# mapa wagi priorytetów używana przy sortowaniu
PRIORITY_ORDER = {
    "high": 1,
    "medium": 2,
    "low": 3
}

class Helpdesk:
    """klasa zarządzająca dodawaniem, usuwaniem, wyszukiwaniem, filtrowaniem i sortowaniem ticketów."""

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
        """zmienia status wskazanego ticketu (oraz ustawia date zamknięcia jeśli status to closed) i zapisuje zmiany."""
        ticket = self.find_ticket(ticket_id)
        if ticket:
            if new_status.lower() == "closed":
                ticket.close()
            else:
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
        """zwraca kopię listy wszystkich ticketów."""
        return list(self.tickets)

    def get_open_tickets(self):
        """zwraca tylko te zgłoszenia, które nie są zamknięte."""
        return [t for t in self.tickets if t.status.lower() != "closed"]

    def filter_tickets(self, status=None, priority=None, open_only=False):
        """filtruje zgłoszenia nie modyfikując oryginalnej listy."""
        result = list(self.tickets)
        if open_only:
            result = [t for t in result if t.status.lower() != "closed"]
        if status:
            result = [t for t in result if t.status.lower() == status.lower()]
        if priority:
            result = [t for t in result if t.priority.lower() == priority.lower()]
        return result

    def sort_tickets(self, tickets_list, by="created_at", reverse=False):
        """sortuje przekazaną listę ticketów według podanego kryterium."""
        result = list(tickets_list)
        if by == "created_at":
            result.sort(key=lambda t: t.created_at, reverse=reverse)
        elif by == "priority":
            result.sort(key=lambda t: PRIORITY_ORDER.get(t.priority.lower(), 99), reverse=reverse)
        return result