import pytest
from validators import validate_priority, validate_status, validate_text

def test_validate_priority_correct():
    assert validate_priority("low") == "low"
    assert validate_priority("MEDIUM") == "medium"
    assert validate_priority("high") == "high"

def test_validate_priority_incorrect():
    with pytest.raises(ValueError):
        validate_priority("urgent")

    with pytest.raises(ValueError):
        validate_priority("")

def test_validate_status_correct():
    assert validate_status("open") == "open"
    assert validate_status("CLOSED") == "closed"

def test_validate_status_incorrect():
    with pytest.raises(ValueError):
        validate_status("in_progress")

def test_validate_text_correct():
    assert validate_text(" nowa wiadomość ") == "nowa wiadomość"

def test_validate_text_empty():
    with pytest.raises(ValueError):
        validate_text("   ")