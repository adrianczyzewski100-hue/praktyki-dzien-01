import csv

with open("produkty.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["ID", "Produkt", "ilosc"])
    writer.writerow([1, "Jablko", 10])
    writer.writerow([2, "Banan", 5])
    writer.writerow([3, "gruszka", 20])

