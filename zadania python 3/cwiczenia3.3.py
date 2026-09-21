def validate_priority(value):
    allowed = ["low", "medium", "high"]
    if value not in allowed:
        raise ValueError(f"niepoprawny priorytet: {value}. Dozwolone wartości to: low, medium, high")
    return value