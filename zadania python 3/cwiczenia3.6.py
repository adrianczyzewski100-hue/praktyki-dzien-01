import json
def load_json(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        print("plik nie istnieje")
        return []
    except json.JSONDecodeError:
        print("plik json jest uszkodzony")
        return[]

with open("dane.json", "w") as f:
    f.write ("{niepoprawny json")

dane = load_json("dane.json")
print("wczytane dane:", dane)
        