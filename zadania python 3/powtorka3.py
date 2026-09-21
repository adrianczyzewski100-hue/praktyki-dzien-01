#1
def dodawanie(a, b):
    return a + b
#2
try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = dodawanie(a, b)
    print(f"Wynik dodawania: {wynik}")
except ValueError:
    print("Wprowadzono nieprawidłową wartość. Proszę podać liczby całkowite.")

#3
with open("sprzet.txt", "r") as plik:
    liczba_linii = sum(1 for _ in plik)
print(f"Liczba linii w pliku: {liczba_linii}")

#4
# funkcje stosujemy aby uniknac powtarzania kodu i zwiekszyc czytelnosc programu