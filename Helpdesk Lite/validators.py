def validate_priority(priority):
    allowed = ["low", "medium", "high"]
    if not priority or priority.lower() not in allowed:
        raise ValueError(f"nieprawidłowy priorytet: {priority}")
    return priority.lower()

def validate_status(status):
    allowed = ["open", "closed"]
    if not status or status.lower() not in allowed:
        raise ValueError(f"nieprawidłowy status: {status}")
    return status.lower()

def validate_text(text):
    if not text or not text.strip():
        raise ValueError("pole nie może być puste")
    return text.strip()