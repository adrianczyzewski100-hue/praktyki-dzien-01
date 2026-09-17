def dodaj(a, b):
    return a + b
def odejmij(a, b):
    return a - b
def pomnoz(a, b):
    return a * b
def podziel(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b
a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
case = input("Wybierz operację (1-dodaj, 2-odejmij, 3-pomnoz, 4-podziel): ")
if case == "1":
    print("Wynik:", dodaj(a, b))
elif case == "2":
    print("Wynik:", odejmij(a, b))
elif case == "3":
    print("Wynik:", pomnoz(a, b))
elif case == "4":
    try:
        print("Wynik:", podziel(a, b))
    except ValueError as e:
        print(e)
