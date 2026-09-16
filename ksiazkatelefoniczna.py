ksiazkaTelefoniczna = {
    "Jan Kowalski": "123-456-789",
    "Anna Nowak": "987-654-321",
}

def DodajKontakt(imie, numer):
    imie = input("Podaj imię kontaktu do dodania: ")
    numer = input("Podaj numer telefonu kontaktu: ")
    ksiazkaTelefoniczna[imie] = numer
    print(f"Dodano kontakt: {imie} - {numer}")
def WyszukajKontakt(imie):
    imie = input("Podaj imię kontaktu do wyszukania: ")
    if imie in ksiazkaTelefoniczna:
        numer = ksiazkaTelefoniczna[imie]
        print(f"Numer telefonu kontaktu {imie} to: {numer}")
    else:
        print(f"Nie znaleziono kontaktu o imieniu: {imie}")
def WyswietlWszystkieKontakty():
    print("Lista kontaktów w książce telefonicznej:")
    for imie, numer in ksiazkaTelefoniczna.items():
        print(f"{imie}: {numer}")

DodajKontakt("", "")
WyszukajKontakt("")
WyswietlWszystkieKontakty()