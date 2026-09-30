import pytest
from database import Database

@pytest.fixture
def test_db(tmp_path):
    db_file = tmp_path / "test_helpdesk.db"
    return Database(str(db_file))

def test_database_isolation(test_db):
    user = test_db.add_user("test_user", "IT")
    assert user["id"] is not None
    assert user["name"] == "test_user"

    ticket = test_db.add_ticket(user["id"], "testowy problem", "high")
    assert ticket["id"] is not None
    assert ticket["user_name"] == "test_user"
    assert ticket["status"] == "open"

def test_add_ticket_non_existent_user(test_db):
    with pytest.raises(ValueError):
        test_db.add_ticket(999, "opis problemu", "low")

def test_update_status_and_delete(test_db):
    user = test_db.add_user("anna", "hr")
    ticket = test_db.add_ticket(user["id"], "opis problemu", "medium")

    updated = test_db.update_status(ticket["id"], "closed", "2026-09-30 12:00:00")
    assert updated is True

    t = test_db.get_ticket_by_id(ticket["id"])
    assert t["status"] == "closed"

    deleted = test_db.delete_ticket(ticket["id"])
    assert deleted is True
    assert test_db.get_ticket_by_id(ticket["id"]) is None