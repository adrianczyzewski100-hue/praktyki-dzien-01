def NajwiekszaLiczba(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))
najwieksza = NajwiekszaLiczba(a, b, c)
print("Największa liczba to:", najwieksza)