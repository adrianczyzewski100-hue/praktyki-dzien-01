import json

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Plik {filename} nie został znaleziony.")
        return []
    except json.JSONDecodeError:
        print(f"Plik {filename} zawiera niepoprawny format JSON.")
        return []

produkty = load_data("produkty2.json")
print("wczytane dane:", produkty)