def dodaj(a, b):
    return a + b
def odejmij(a, b):
    return a - b
def mnoz(a, b):
    return a * b
def dziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"
def kalkulator(a, b, operacja):
    if operacja == "dodawanie":
        return dodaj(a, b)
    elif operacja == "odejmowanie":
        return odejmij(a, b)
    elif operacja == "mnożenie":
        return mnoz(a, b)
    elif operacja == "dzielenie":
        return dziel(a, b)
    else:
        return "Nieznana operacja!"

print(kalkulator(10, 5, "dodawanie"))  # Wynik: 15
print(kalkulator(10, 5, "odejmowanie"))  # Wynik: 5
print(kalkulator(10, 5, "mnożenie"))  # Wynik: 50
print(kalkulator(10, 5, "dzielenie"))  # Wynik: 2.0