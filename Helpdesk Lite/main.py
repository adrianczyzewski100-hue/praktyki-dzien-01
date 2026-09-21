import json
import os

tickets = []
next_id = 1

#zapisywanie i czytywanie pliku

def load_tickets_from_file():
    global next_id

    if not os.path.exists("tickets.json"):
        print("Plik tickets.json nie istnieje — zaczynam od pustej listy.")
        return

    try:
        with open("tickets.json", "r") as file:
            data = json.load(file)

            tickets.clear()
            tickets.extend(data)

            if tickets:
                next_id = max(ticket["id"] for ticket in tickets) + 1
            else:
                next_id = 1

            print("Tickety wczytane poprawnie.")

    except json.JSONDecodeError:
        print("Błąd: plik JSON jest uszkodzony. Zaczynam od pustej listy.")


def save_tickets_to_file():
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)
    print("Tickety zapisane do pliku.")

#operacje na ticketach

def add_ticket():
    global next_id

    user = input("Podaj nazwę użytkownika: ").strip()
    if user == "":
        print("Błąd: nazwa użytkownika nie może być pusta.")
        return

    problem = input("Podaj opis problemu: ").strip()
    if problem == "":
        print("Błąd: opis problemu nie może być pusty.")
        return

    status = input("Podaj status ticketu: ").strip()
    priority = input("Podaj priorytet (low/medium/high): ").strip().lower()

    if priority not in ["low", "medium", "high"]:
        print("Błąd: priorytet musi być low/medium/high.")
        return

    ticket = {
        "id": next_id,
        "user": user,
        "problem": problem,
        "status": status,
        "priority": priority
    }

    tickets.append(ticket)
    next_id += 1

    save_tickets_to_file()
    print(f"Ticket {ticket['id']} został dodany.")


def find_ticket(id):
    for ticket in tickets:
        if ticket["id"] == id:
            return ticket
    return None


def change_status(id, new_status):
    ticket = find_ticket(id)
    if ticket:
        ticket["status"] = new_status
        save_tickets_to_file()
        print(f"Status ticketu {id} został zmieniony na {new_status}.")
    else:
        print(f"Nie znaleziono ticketu o ID {id}.")


def delete_ticket(id):
    global tickets
    ticket = find_ticket(id)
    if ticket:
        tickets = [t for t in tickets if t["id"] != id]
        save_tickets_to_file()
        print(f"Ticket {id} został usunięty.")
    else:
        print(f"Nie znaleziono ticketu o ID {id}.")


def show_tickets():
    if len(tickets) == 0:
        print("Brak ticketów do wyświetlenia.")
    else:
        for ticket in tickets:
            print(f"ID: {ticket['id']}, "
                  f"Użytkownik: {ticket['user']}, "
                  f"Problem: {ticket['problem']}, "
                  f"Status: {ticket['status']}, "
                  f"Priorytet: {ticket['priority']}")

            #menu

def menu():
    load_tickets_from_file()

    while True:
        print("\nMenu:")
        print("1. Dodaj ticket")
        print("2. Znajdź ticket po ID")
        print("3. Zmień status ticketu")
        print("4. Wyświetl wszystkie tickety")
        print("5. Usuń ticket")
        print("6. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_ticket()

        elif choice == "2":
            try:
                id = int(input("Podaj ID ticketu: "))
            except ValueError:
                print("Błąd: wpisano tekst zamiast liczby.")
                continue

            ticket = find_ticket(id)
            if ticket:
                print(ticket)
            else:
                print(f"Nie znaleziono ticketu o ID {id}.")

        elif choice == "3":
            try:
                id = int(input("Podaj ID ticketu: "))
            except ValueError:
                print("Błąd: wpisano tekst zamiast liczby.")
                continue

            new_status = input("Podaj nowy status ticketu: ")
            change_status(id, new_status)

        elif choice == "4":
            show_tickets()

        elif choice == "5":
            try:
                id = int(input("Podaj ID ticketu do usunięcia: "))
            except ValueError:
                print("Błąd: wpisano tekst zamiast liczby.")
                continue

            delete_ticket(id)

        elif choice == "6":
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


menu()
