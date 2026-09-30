"""
moduł odpowiedzialny za trwałe przechowywanie danych w pliku json.
"""

import json
import os

class Storage:
    """klasa obsługująca odczyt i zapis danych z/do pliku JSON."""

    def __init__(self, filename="tickets.json"):
        self.filename = filename

    def load(self):
        """odczytuje zgłoszenia z pliku json. zwraca pustą listę w przypadku braku pliku lub błędu."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save(self, data):
        """zapisuje listę słowników do pliku json."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)