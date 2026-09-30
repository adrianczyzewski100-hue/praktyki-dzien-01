import csv

with open("produkty.csv", "r", encoding="utf-8") as plik:
    czytnik = csv.reader(plik)
    wiersze = list(czytnik)
    liczba_wierszy = len(wiersze)

print(liczba_wierszy)