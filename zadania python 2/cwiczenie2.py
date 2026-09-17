import random
liczba_zgadywana = random.randint(1, 100)
liczba_prob = 0
liczba= int(input("Zgadnij liczbę od 1 do 100: "))
while liczba != liczba_zgadywana:
    liczba_prob += 1
    if liczba < liczba_zgadywana:
        print("Za mało!")
    else:
        print("Za dużo!")
    liczba = int(input("Spróbuj ponownie: "))
print(f"Gratulacje! Zgadłeś liczbę w {liczba_prob} próbach.")