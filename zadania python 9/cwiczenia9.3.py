import csv
with open("report.csv", "r", encoding="utf-8") as plik:
    czytnik = csv.DictReader(plik, delimiter=";")
    aktywne = [wiersz for wiersz in czytnik if wiersz.get("active") == "1"]

for wiersz in aktywne:
    print(wiersz)