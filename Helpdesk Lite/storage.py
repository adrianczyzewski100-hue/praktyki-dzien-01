"""
moduł odpowiedzialny za operacje wejścia/wyjścia na plikach json.
"""

import json
import os
from config import TICKETS_FILE

class Storage:
    """klasa obsługująca odczyt i zapis danych z/do pliku json."""
    def __init__(self, filename=TICKETS_FILE):
        self.filename = filename

    def load(self):
        """wczytuje listę słowników z pliku json. zwraca pustą listę w przypadku błędu."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # w przypadku uszkodzonego pliku json zwracamy pustą listę
            return []

    def save(self, data):
        """zapisuje przekazaną strukturę danych do pliku json."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)