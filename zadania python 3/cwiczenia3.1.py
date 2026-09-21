import json
with open("dane_pracownika.json", "w") as plik:
    dane_pracownika = {
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "wiek": 30,
        "stanowisko": "Programista"
    }
    json.dump(dane_pracownika, plik, indent=4)
with open("dane_pracownika.json", "r") as plik:
    dane = json.load(plik)
    print(dane)