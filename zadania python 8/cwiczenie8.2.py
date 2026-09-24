produkty = [
    {"nazwa": "etui", "cena": 45},
    {"nazwa": "ładowarka", "cena": 120},
    {"nazwa": "telefon", "cena": 2500},
    {"nazwa": "słuchawki", "cena": 300}
]

rosnaco = sorted(produkty, key=lambda x: x["cena"])
malejaco = sorted(produkty, key=lambda x: x["cena"], reverse=True)

print(rosnaco)
print(malejaco)