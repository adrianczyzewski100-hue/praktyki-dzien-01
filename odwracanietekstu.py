def OdwrocTekst(tekst):
    return tekst[::-1]
def czyPalindrom(tekst):
    odwrocony_tekst = OdwrocTekst(tekst)
    if tekst == odwrocony_tekst:
        return True
    else:
        return False
tekst = input("Podaj tekst do odwrócenia: ")
odwrocony_tekst = OdwrocTekst(tekst)
print("Odwrócony tekst:", odwrocony_tekst)
if czyPalindrom(tekst):
    print("Tekst jest palindromem.")
else:
    print("Tekst nie jest palindromem.")
