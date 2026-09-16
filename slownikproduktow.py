produkty = {
    "Chleb": 4.50,
    "Mleko": 3.20,
    "Masło": 7.80,
    "Jajka": 9.99,
    "Ser": 12.50
}

produkt = input("Podaj nazwę produktu: ")
if produkt in produkty:
    cena = produkty[produkt]
    print(f"Cena {produkt} wynosi: {cena} zł")
else:
    print("Nie znaleziono produktu w słowniku.")