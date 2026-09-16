import datetime
def IleLat(rok_urodzenia):
    dzisiaj = datetime.date.today()
    wiek = dzisiaj.year- rok_urodzenia
    return wiek
def CzyPelnoletni(rok_urodzenia):
    dzisiaj = datetime.date.today()
    wiek = dzisiaj.year- rok_urodzenia
    if wiek >= 18:
        return True
    else:
        return False
rok_urodzenia = input("Podaj rok urodzenia: ")
print("Masz", IleLat(int(rok_urodzenia)), "lat.")
if CzyPelnoletni(int(rok_urodzenia)):
    print("Jesteś pełnoletni.")
else:
    print("Nie jesteś pełnoletni.")