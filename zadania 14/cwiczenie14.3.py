import pytest

tickets_db = {
    1: {"title": "problem z logowaniem"},
    2: {"title": "błąd w płatnościach"}
}

def get_ticket(ticket_id):
    if not isinstance(ticket_id, int) or ticket_id <= 0:
        raise ValueError("id musi być dodatnią liczbą całkowitą")
    if ticket_id not in tickets_db:
        raise KeyError("ticket o podanym id nie istnieje")
    return tickets_db[ticket_id]

@pytest.mark.parametrize("invalid_id", [0, -1, "123", 1.5, None, []])
def test_get_ticket_invalid_id_format(invalid_id):
    with pytest.raises(ValueError):
        get_ticket(invalid_id)

def test_get_ticket_non_existent_id():
    with pytest.raises(KeyError):
        get_ticket(999)