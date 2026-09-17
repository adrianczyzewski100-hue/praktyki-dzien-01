def kalkulator(a, b, operacja):
    if operacja == "dodawanie":
        return a + b
    elif operacja == "odejmowanie":
        return a - b
    elif operacja == "mnożenie":
        return a * b
    elif operacja == "dzielenie":
        if b != 0:
            return a / b
        else:
            return "Nie można dzielić przez zero!"
    else:
        return "Nieznana operacja!"
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
operacja = input("Podaj operację (dodawanie, odejmowanie, mnożenie, dzielenie): ")
wynik = kalkulator(a, b, operacja)
print(f"Wynik: {wynik}")