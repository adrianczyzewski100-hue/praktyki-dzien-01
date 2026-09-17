lista_ocen = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]
srednia = sum(lista_ocen) / len(lista_ocen)
print(f"Średnia ocen: {srednia}")
najmniejsza_ocena = min(lista_ocen)
najwieksza_ocena = max(lista_ocen)
print(f"Najmniejsza ocena: {najmniejsza_ocena}")
print(f"Największa ocena: {najwieksza_ocena}")
liczba_pozytywnych = 0
for ocena in lista_ocen:
    if ocena >= 3:
        liczba_pozytywnych += 1
print(f"Liczba pozytywnych ocen: {liczba_pozytywnych}")