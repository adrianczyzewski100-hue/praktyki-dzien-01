def znajdz_pracownika_po_id(pracownicy, id):
    for pracownik in pracownicy:
        if pracownik["id"] == id:
            return pracownik
    return None


pracownicy = [
    {"id": 1, "imie": "Adam", "stanowisko": "Kierownik"},
    {"id": 2, "imie": "Ewa", "stanowisko": "Magazynier"},
    {"id": 3, "imie": "Ola", "stanowisko": "Informatyk"}
]

# obsługa błędu wpisania tekstu
try:
    id = int(input("Wprowadź ID pracownika: "))
except ValueError:
    print("blad: wpisano tekst zamiast liczby")
    id = None

if id is not None:
    wynik = znajdz_pracownika_po_id(pracownicy, id)
    if wynik:
        print(f"Znaleziono pracownika: {wynik['imie']}, Stanowisko: {wynik['stanowisko']}")
    else:
        print("Nie znaleziono pracownika o podanym ID.")
