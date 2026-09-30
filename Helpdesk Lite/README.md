# Helpdesk Lite v0.5 (SQLite Edition)

system do zarządzania zgłoszeniami w konsoli z obsługą bazy danych SQLite3.

## wymagania

- python 3.8 lub nowszy
- wbudowany moduł sqlite3 (standard w pythonie)

## instalacja i uruchomienie

1. pobierz lub sklonuj repozytorium

2. uruchom aplikację:
   python main.py

## funkcje

- przechowywanie danych w bazie SQLite (`helpdesk.db`)
- dodawanie nowych ticketów (`INSERT`)
- szybkie wyszukiwanie pojedynczych zgłoszeń po ID (`SELECT ... WHERE id = ?`)
- zmiana statusu zgłoszenia (`UPDATE`)
- filtrowanie i sortowanie bezpośrednio w bazie SQL
- usuwanie zgłoszeń (`DELETE`)
- eksport zgłoszeń do pliku CSV z kodowaniem UTF-8-SIG pod program Excel

## struktura plików

- `main.py` - interfejs konsolowy
- `helpdesk.py` - logika biznesowa
- `database.py` - obsługa połączenia i zapytań SQL do bazy danych
- `ticket.py` - model zgłoszenia
- `validators.py` - walidacja danych wejściowych