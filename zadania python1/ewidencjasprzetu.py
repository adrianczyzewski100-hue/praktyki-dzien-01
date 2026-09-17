def pobierz_nastepne_id():
    try:
        with open("sprzet.txt", "r") as plik:
            linie = plik.readlines()
            if not linie:
                return 1
            ostatnia_linia = linie[-1]
            ostatnie_id = int(ostatnia_linia.split(",")[0])
            return ostatnie_id + 1
    except FileNotFoundError:
        return 1

def dodaj_sprzet(nazwa, ilosc):
    id = pobierz_nastepne_id()
    with open("sprzet.txt", "a") as plik:
        plik.write(f"{id},{nazwa},{ilosc}\n")
    print(f"Dodano sprzęt: ID={id}, Nazwa={nazwa}, Ilość={ilosc}")

def wyswietl_sprzet():
    with open("sprzet.txt", "r") as plik:
        for linia in plik:
            id, nazwa, ilosc = linia.strip().split(",")
            print(f"ID: {id}, Nazwa: {nazwa}, Ilość: {ilosc}")
def usun_sprzet(id):
    with open("sprzet.txt", "r") as plik:
        linie = plik.readlines()
    with open("sprzet.txt", "w") as plik:
        for linia in linie:
            if not linia.startswith(f"{id},"):
                plik.write(linia)
def wyszukiwanie_sprzetu(id_szukane=None, nazwa_szukana=None):
    with open("sprzet.txt", "r") as plik:
        znaleziono = False

        for linia in plik:
            id_pliku, nazwa_pliku, ilosc_pliku = linia.strip().split(",")
            if id_szukane is not None and id_pliku == str(id_szukane):
                print(f"Znaleziono po ID: ID={id_pliku}, Nazwa={nazwa_pliku}, Ilość={ilosc_pliku}")
                znaleziono = True
            if nazwa_szukana is not None and nazwa_pliku.lower() == nazwa_szukana.lower():
                print(f"Znaleziono po nazwie: ID={id_pliku}, Nazwa={nazwa_pliku}, Ilość={ilosc_pliku}")
                znaleziono = True
        if not znaleziono:
            print("Nie znaleziono sprzętu.")

def przypisz_pracownika_do_sprzetu(id_pracownika, id_sprzetu):
    with open("sprzet.txt", "r") as plik:
        linie = plik.readlines()
    with open("sprzet.txt", "w") as plik:
        for linia in linie:
            if linia.startswith(f"{id_sprzetu},"):
                plik.write(f"{id_sprzetu},{linia.strip().split(',')[1]},{linia.strip().split(',')[2]},{id_pracownika}\n")
            else:
                plik.write(linia)

dodaj_sprzet("Telefon", 5)
dodaj_sprzet("Laptop", 3)
dodaj_sprzet("Tablet", 2)
usun_sprzet(1)
wyswietl_sprzet()
wyszukiwanie_sprzetu(id_szukane=6, nazwa_szukana=None)
