import pytest

def get_user_by_id(user_id):
    database = {1: "Anna", 2: "Jan"}
    if not isinstance(user_id, int) or user_id <=0:
        raise ValueError("nieprawidlowe id")
    return database.get(user_id)

def test_get_user_by_id_succes():
    user_id = 1
    expected_name = "Anna"

    result = get_user_by_id(user_id)

    assert result == expected_name