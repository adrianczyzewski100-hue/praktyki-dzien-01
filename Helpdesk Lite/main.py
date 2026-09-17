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