import json
import os

#1
def save_to_json(lista, filename="lista.json"):
    with open (filename, "w") as file:
        json.dump(lista, file, indent=4)


#2
def load_from_json(filename="lista.json"):
    if not os.path.exists(filename):
        print("plik nie istnieje")
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("plik json jest uszkodzony")
        return[]

#3
#kompletnosc danych
#poprawnosc techniczna
#zgodnosc biznesowa