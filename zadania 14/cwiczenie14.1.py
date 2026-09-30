import pytest

def validate_priority(priority):
    if not isinstance(priority, int) or not (1 <= priority <= 5):
        raise ValueError("priorytet musi być liczbą całkowitą od 1 do 5")
    return True

@pytest.mark.parametrize("valid_priority", [1, 2, 3, 4, 5])
def test_validate_priority_valid_values(valid_priority):
    assert validate_priority(valid_priority) is True

@pytest.mark.parametrize("invalid_priority", [0, 6, -1, "1", 2.5, None])
def test_validate_priority_invalid_values(invalid_priority):
    with pytest.raises(ValueError):
        validate_priority(invalid_priority)