from storage import load_tickets, save_tickets
from validators import validate_user, validate_problem, validate_priority

tickets = load_tickets()
next_id = max((t["id"] for t in tickets), default=0) + 1

def add_ticket():
    global next_id

    user = input("Podaj nazwę użytkownika: ").strip()
    if not validate_user(user):
        print("Błąd: nazwa użytkownika nie może być pusta.")
        return

    problem = input("Podaj opis problemu: ").strip()
    if not validate_problem(problem):
        print("Błąd: opis problemu nie może być pusty.")
        return

    status = input("Podaj status ticketu: ").strip()
    priority = input("Podaj priorytet (low/medium/high): ").strip().lower()

    if not validate_priority(priority):
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
    save_tickets(tickets)

    print(f"Ticket {ticket['id']} został dodany.")

def find_ticket(id):
    return next((t for t in tickets if t["id"] == id), None)

def change_status(id, new_status):
    ticket = find_ticket(id)
    if ticket:
        ticket["status"] = new_status
        save_tickets(tickets)
        print(f"Status ticketu {id} został zmieniony.")
    else:
        print("Nie znaleziono ticketu.")

def delete_ticket(id):
    global tickets
    ticket = find_ticket(id)
    if ticket:
        tickets = [t for t in tickets if t["id"] != id]
        save_tickets(tickets)
        print(f"Ticket {id} został usunięty.")
    else:
        print("Nie znaleziono ticketu.")

def show_tickets():
    if not tickets:
        print("Brak ticketów.")
        return

    for t in tickets:
        print(f"ID: {t['id']}, Użytkownik: {t['user']}, Problem: {t['problem']}, "
              f"Status: {t['status']}, Priorytet: {t['priority']}")
