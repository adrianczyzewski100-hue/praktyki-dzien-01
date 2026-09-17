import random
import string
def generuj_haslo(dlugosc):
    znaki = string.ascii_letters + string.digits
    haslo = ''.join(random.choice(znaki) for _ in range(dlugosc))
    return haslo

dlugosc = int(input("Podaj długość hasła: "))
print("Wygenerowane hasło:", generuj_haslo(dlugosc))