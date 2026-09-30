Helpdesk Lite v0.5
system do zarzadzania zgloszeniami w konsoli

wymagania
- python 3.8 lub nowszy
- brak zewsnetrznych bibliotek

instalacja i uruchomienie
1. pobierz lub sklonuj repozytorium
2. uruchom aplikacje:
   python main.py

funkcje
- dodawanie nowych ticketow
- wyszukiwanie zgloszen po id
- zmiana statusu zgloszenia
- filtrowanie oraz sortowanie zgloszen
- usuwanie zgloszen
- eksport zgloszen do pliku CSV z kodowaniem utf-8-sig pod program excel

struktura plikow
- main.py - interfejs konsolowy
- helpdesk.py - logika biznesowa i eksport danych
- ticket.py - model zgloszenia
- storage.py - zapis i odczyt z pliku json
- validators.py - walidacja dancyh wejsciowych