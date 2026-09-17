import random
def losuj_liczbe():
    return random.randint(1, 100)
def zgadnij_liczbe():
    proby = 0
    while True:
        proby += 1
        strzal = int(input("Zgadnij liczbę od 1 do 100: "))
        if strzal < liczba:
            print("Za mało!")
        elif strzal > liczba:
            print("Za dużo!")
        else:
            print(f"Gratulacje! Zgadłeś liczbę {liczba} w {proby} próbach.")
            break
liczba = losuj_liczbe()
zgadnij_liczbe()