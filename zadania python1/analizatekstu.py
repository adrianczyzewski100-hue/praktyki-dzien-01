def IleZnakow(tekst):
    liczba_znakow = len(tekst)
    return liczba_znakow
def IleSlow(tekst):
    slowa = tekst.split()
    liczba_slow = len(slowa)
    return liczba_slow
def IleLiter(tekst):
    liczba_liter = sum(1 for znak in tekst if znak.isalpha())
    return liczba_liter
def WielkieLitery(tekst):
    duze = tekst.upper()
    return duze
tekst = input("Podaj tekst: ")
print("Liczba znaków w tekście:", IleZnakow(tekst))
print("Liczba słów w tekście:", IleSlow(tekst)) 
print("Liczba liter w tekście:", IleLiter(tekst))
print("Tekst zapisany wielkimi literami:", WielkieLitery(tekst))