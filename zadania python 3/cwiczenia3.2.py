import json

produkty = ["chleb","mleko","jajka"]

with open("produkty.json", "w") as plik:
    json.dump(produkty, plik, indent=4)