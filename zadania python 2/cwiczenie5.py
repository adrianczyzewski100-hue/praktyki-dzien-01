produkty = {
    "jablko": 5.0,
    "banan": 3.0,
    "grejpfrut": 7.0
}

nazwa = input("Podaj nazwę produktu: ")
if nazwa in produkty:
    cena = produkty[nazwa]
    print(f"Cena {nazwa} wynosi: {cena} zł")
else:
    print("Produkt o podanej nazwie nie istnieje.")