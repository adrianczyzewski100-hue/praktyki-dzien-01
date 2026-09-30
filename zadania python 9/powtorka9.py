lista = [1,2,3,4,5,6,7]
filtr = [x for x in lista if x % 2 == 0]
print(filtr)

ludzie = [
    {"imie": "anna", "wiek": 30},
    {"imie": "jan", "wiek": 25},
    {"imie": "ewa", "wiek": 35}
]
posortowane = sorted(ludzie, key=lambda x: x["wiek"])

print(posortowane)

from datetime import datetime
teraz = datetime.now()
teskstiso = teraz.isoformat()
print(teskstiso)