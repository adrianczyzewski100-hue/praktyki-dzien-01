<<<<<<< HEAD
tickets = []
next_id = 1   # globalny licznik ID


def add_ticket():
    global next_id

    id = next_id
    next_id += 1

    user = input("Podaj nazwę użytkownika: ")
    problem = input("Podaj opis problemu: ")
    status = input("Podaj status ticketu: ")

    ticket = {
        "id": id,
        "user": user,
        "problem": problem,
        "status": status
    }

    tickets.append(ticket)
    print(f"Ticket {id} został dodany.")


def find_ticket(id):
    for ticket in tickets:
        if ticket["id"] == id:
            return ticket
    return None


def change_status(id, new_status):
    ticket = find_ticket(id)
    if ticket:
        ticket["status"] = new_status
        print(f"Status ticketu {id} został zmieniony na {new_status}.")
    else:
        print(f"Nie znaleziono ticketu o ID {id}.")


def show_tickets():
    if len(tickets) == 0:
        print("Brak ticketów do wyświetlenia.")
    else:
        for ticket in tickets:
            print(f"ID: {ticket['id']}, Użytkownik: {ticket['user']}, Problem: {ticket['problem']}, Status: {ticket['status']}")


def save_tickets_to_file():
    with open("tickets.txt", "w") as file:
        for ticket in tickets:
            file.write(f"{ticket['id']},{ticket['user']},{ticket['problem']},{ticket['status']}\n")
    print("Tickety zapisane do pliku.")


def load_tickets_from_file():
    global next_id
    try:
        with open("tickets.txt", "r") as file:
            tickets.clear()
            max_id = 0

            for line in file:
                id, user, problem, status = line.strip().split(",")
                id = int(id)

                ticket = {
                    "id": id,
                    "user": user,
                    "problem": problem,
                    "status": status
                }
                tickets.append(ticket)

                if id > max_id:
                    max_id = id

            next_id = max_id + 1
            print("Tickety wczytane poprawnie.")

    except FileNotFoundError:
        print("Plik tickets.txt nie istnieje — zaczynam od pustej listy.")


def menu():
    while True:
        print("\nMenu:")
        print("1. Dodaj ticket")
        print("2. Znajdź ticket po ID")
        print("3. Zmień status ticketu")
        print("4. Wyświetl wszystkie tickety")
        print("5. Zapisz tickety do pliku")
        print("6. Wczytaj tickety z pliku")
        print("7. Wyjście")

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
                print(f"ID: {ticket['id']}, Użytkownik: {ticket['user']}, Problem: {ticket['problem']}, Status: {ticket['status']}")
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
            save_tickets_to_file()

        elif choice == "6":
            load_tickets_from_file()

        elif choice == "7":
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


menu()
=======
tickets = []
def dodaj_ticket(id,user,problem,status):
    #zwiekszanie id z kazdym dodaniem ticketu
    id = len(tickets) + 1

    user = input("Podaj nazwę użytkownika: ")

    problem = input("Podaj opis problemu: ")

    status = input("Podaj status ticketu: ")

    ticket = {
        "id": id,
        "user": user,
        "problem": problem,
        "status": status
    }

    tickets.append(ticket)
    print(f"Ticket {id} został dodany.")

def wyswietl_tickets():
    if len(tickets) == 0:
        print("Brak ticketów do wyświetlenia.")
    else:
        for ticket in tickets:
            print(f"ID: {ticket['id']}, Użytkownik: {ticket['user']}, Problem: {ticket['problem']}, Status: {ticket['status']}")

            
dodaj_ticket(None, None, None, None)
dodaj_ticket(None, None, None, None)
dodaj_ticket(None, None, None, None)
wyswietl_tickets()
>>>>>>> e646a3e87b80409923b3a0889b8e054ab2c7274f
