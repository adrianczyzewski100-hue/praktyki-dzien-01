from datetime import datetime
import pytest

class Ticket:
    def __init__(self, title):
        self.title = title
        self.status = "open"
        self.closed_at = None

    def close(self):
        if self.status == "closed":
            raise ValueError("ticket jest już zamknięty")
        self.status = "closed"
        self.closed_at = datetime.now()

def test_ticket_close_success():
    ticket = Ticket("problem z logowaniem")
    
    ticket.close()
    
    assert ticket.status == "closed"
    assert ticket.closed_at is not None

def test_ticket_close_already_closed():
    ticket = Ticket("problem z logowaniem")
    ticket.close()
    
    with pytest.raises(ValueError):
        ticket.close()