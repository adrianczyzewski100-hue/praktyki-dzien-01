def SumaLiczb(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
n = int(input("Podaj liczbę: "))
wynik = SumaLiczb(n)
print("Suma liczb od 1 do", n, "wynosi:", wynik)