dane = [
    {"name": "telefon", "cena": 2500},
    {"name": "etui", "cena": 45},
    {"name": "słuchawki", "cena": 300}
]

posortowane = sorted(dane, key=lambda x: x["name"])
print(posortowane)