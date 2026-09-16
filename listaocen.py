oceny = [5, 4, 3, 6, 2, 5, 4, 3, 6, 1]
def obliczSrednia(oceny):
    if len(oceny) == 0:
        return 0
    suma = sum(oceny)
    srednia = suma / len(oceny)
    return srednia
def znajdzNajwyzszaOcene(oceny):
    if len(oceny) == 0:
        return None
    najwyzsza = max(oceny)
    return najwyzsza
def znajdzNajnizszaOcene(oceny):
    if len(oceny) == 0:
        return None
    najnizsza = min(oceny)
    return najnizsza
def LiczbaOcenPozytywnych(oceny):
    liczba_pozytywnych = sum(1 for ocena in oceny if ocena >= 3)
    return liczba_pozytywnych
print("Oceny:", oceny)
print("Średnia ocen:", obliczSrednia(oceny))
print("Najwyższa ocena:", znajdzNajwyzszaOcene(oceny))
print("Najniższa ocena:", znajdzNajnizszaOcene(oceny))
print("Liczba ocen pozytywnych:", LiczbaOcenPozytywnych(oceny))