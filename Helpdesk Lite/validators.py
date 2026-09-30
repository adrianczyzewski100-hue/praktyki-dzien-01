"""
moduł zawierający funkcje walidujące dane wejściowe.
"""

def validate_user(user):
    """sprawdza, czy nazwa użytkownika nie jest pusta."""
    return bool(user and user.strip())

def validate_description(description):
    """sprawdza, czy opis problemu nie jest pusty."""
    return bool(description and description.strip())

def validate_priority(priority):
    """sprawdza, czy priorytet należy do dozwolonych wartości."""
    return priority in ["low", "medium", "high"]