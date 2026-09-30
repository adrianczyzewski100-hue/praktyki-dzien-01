import pytest
from tickets import Ticket

def test_ticket_creation_defaults():
    t = Ticket(id=1, user_id=1, description="test problem")
    assert t.status == "open"
    assert t.priority == "medium"

def test_ticket_valid_status_and_priority():
    t = Ticket(id=2, user_id=1, description="test", status="closed", priority="high")
    assert t.status == "closed"
    assert t.priority == "high"

def test_ticket_invalid_priority():
    with pytest.raises(ValueError):
        Ticket(id=3, user_id=1, description="test", priority="critical")

def test_ticket_from_dict():
    data = {
        "id": 10,
        "user_id": 2,
        "user_name": "jan_kowalski",
        "department": "IT",
        "description": "brak internetu",
        "status": "open",
        "priority": "high",
        "created_at": "2026-09-30 10:00:00"
    }
    t = Ticket.from_dict(data)
    assert t.id == 10
    assert t.user_name == "jan_kowalski"
    assert t.priority == "high"