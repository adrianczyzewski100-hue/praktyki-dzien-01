import json
import os
from config import TICKETS_FILE

def load_tickets():
    if not os.path.exists(TICKETS_FILE):
        return []

    try:
        with open(TICKETS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Błąd: plik JSON jest uszkodzony. Zaczynam od pustej listy.")
        return []

def save_tickets(tickets_dict_list):
    with open(TICKETS_FILE, "w") as file:
        json.dump(tickets_dict_list, file, indent=4)
