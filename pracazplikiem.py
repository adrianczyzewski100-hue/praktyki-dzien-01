def dodaj_pracownika(imie):
    with open("pracownicy.txt", "a") as plik:
        plik.write(f"{imie}\n")
    print(f"dodano pracownika:{imie}")

def odczytaj_pracownikow():
    with open("pracownicy.txt", "r") as plik:
        pracownicy = plik.readlines()
    return [pracownik.strip() for pracownik in pracownicy]

def PoliczPracownikow():
    pracownicy = odczytaj_pracownikow()
    return len(pracownicy)

dodaj_pracownika("bbb")
print("Liczba pracowników:", PoliczPracownikow())
print("Lista pracowników:", odczytaj_pracownikow())