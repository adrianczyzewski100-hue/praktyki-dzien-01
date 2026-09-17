imiona = ["Adam", "Ewa", "Ola"]

with open("imiona.txt", "w") as plik:
    for imie in imiona:                     #zapisanie imion do pliku tekstowego, każde imię w nowej linii
        plik.write(imie + "\n")

with open("imiona.txt", "r") as plik:
    zawartosc = plik.read()                 #odczytanie zawartości pliku tekstowego
    print(zawartosc)