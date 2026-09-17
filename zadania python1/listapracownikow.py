pracownicy = ["Adam", "Beata", "Cezary", "Daria", "Eryk"]
imie = ""
def DodajPracownika(imie):
    imie = input("Podaj imię pracownika do dodania: ")
    pracownicy.append(imie)
def UsunPracownika(imie):
    imie = input("Podaj imię pracownika do usunięcia: ")
    if imie in pracownicy:
        pracownicy.remove(imie)
    else:
        print("Nie znaleziono pracownika o imieniu:", imie)
def WyswietlPracownikow():
    print("Lista pracowników:")
    for pracownik in pracownicy:
        print(pracownik)
def Czyjestnaliscie(imie):
    imie = input("Podaj imię pracownika do sprawdzenia: ")
    if imie in pracownicy:
        print("Pracownik o imieniu", imie, "jest na liście.")
    else:
        print("Pracownik o imieniu", imie, "nie jest na liście.")

DodajPracownika(imie)
UsunPracownika(imie)
WyswietlPracownikow()
Czyjestnaliscie(imie)