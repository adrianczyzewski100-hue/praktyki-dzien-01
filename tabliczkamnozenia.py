def TabliczkaMnozenia(n,wynik):
    for i in range(1,11):
        wynik = n * i
        print(f"{n} x {i} = {wynik}")
wynik = 0
n=int(input("Podaj liczbę, dla której chcesz zobaczyć tabliczkę mnożenia: "))
TabliczkaMnozenia(n,wynik)