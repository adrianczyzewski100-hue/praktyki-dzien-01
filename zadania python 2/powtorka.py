imie = input("Podaj swoje imię: ")
wiek = int(input("Podaj swój wiek: "))

print(f"imie: {imie}, wiek: {wiek}")

liczba = int(input("Podaj liczbę: "))
if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba < 0:
    print("Liczba jest ujemna")
else:
    print("Liczba jest równa zero")

for i in range(2,20,2):
    print(i)