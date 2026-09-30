import csv

with open("report.csv", "r", encoding="utf-8") as plik:
    czytnik = csv.DictReader(plik, delimiter=";")
    polola_naglowka = czytnik.fieldnames
    wszystkie = list(czytnik)

with open("raport_wszystkie.csv", "w", encoding="utf-8", newline="") as plik:
    writer = csv.DictWriter(plik, fieldnames=polola_naglowka, delimiter=";")
    writer.writeheader()
    writer.writerows(wszystkie)

aktywne = [wiersz for wiersz in wszystkie if wiersz.get("active") == "1"]

with open("raport_aktywne.csv", "w", encoding="utf-8", newline="") as plik:
    writer = csv.DictWriter(plik, fieldnames=polola_naglowka, delimiter=";")
    writer.writeheader()
    writer.writerows(aktywne)

print("raporty zostały wygenerowane pomyślnie")