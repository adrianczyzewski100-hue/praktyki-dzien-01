def CzyParzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

liczba = int(input("Podaj liczbę: "))
if CzyParzysta(liczba):
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")
