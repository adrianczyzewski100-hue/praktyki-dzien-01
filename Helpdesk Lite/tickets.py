from storage import load_tickets, save_tickets
from validators import validate_user, validate_description, validate_priority

class Ticket:
    def __init__(self, id, user, description, status, priority):
        self.id = id
        self.user = user
        self.description = description
        self.status = status
        self.priority = priority

    def close(self):
        self.status = "closed"

    def change_priority(self, new_priority):
        if validate_priority(new_priority):
            self.priority = new_priority
        else:
            print("Błąd: priorytet musi być low/medium/high.")

    def __str__(self):
        return (f"Ticket {self.id}: "
                f"user={self.user}, "
                f"description={self.description}, "
                f"status={self.status}, "
                f"priority={self.priority}")


# --- Lista ticketów wczytana z pliku ---
tickets = [Ticket(**t) for t in load_tickets()]
next_id = max((t.id for t in tickets), default=0) + 1


def add_ticket():
    global next_id

    user = input("Podaj nazwę użytkownika: ").strip()
    if not validate_user(user):
        print("Błąd: nazwa użytkownika nie może być pusta.")
        return

    description = input("Podaj opis problemu: ").strip()
    if not validate_description(description):
        print("Błąd: opis problemu nie może być pusty.")
        return

    status = input("Podaj status ticketu: ").strip()
    priority = input("Podaj priorytet (low/medium/high): ").strip().lower()

    if not validate_priority(priority):
        print("Błąd: priorytet musi być low/medium/high.")
        return

    ticket = Ticket(next_id, user, description, status, priority)
    tickets.append(ticket)
    next_id += 1

    save_tickets([t.__dict__ for t in tickets])
    print(f"Ticket {ticket.id} został dodany.")


def find_ticket(id):
    return next((t for t in tickets if t.id == id), None)


def change_status(id, new_status):
    ticket = find_ticket(id)
    if ticket:
        ticket.status = new_status
        save_tickets([t.__dict__ for t in tickets])
        print(f"Status ticketu {id} został zmieniony.")
    else:
        print("Nie znaleziono ticketu.")


def delete_ticket(id):
    global tickets
    ticket = find_ticket(id)
    if ticket:
        tickets = [t for t in tickets if t.id != id]
        save_tickets([t.__dict__ for t in tickets])
        print(f"Ticket {id} został usunięty.")
    else:
        print("Nie znaleziono ticketu.")


def show_tickets():
    if not tickets:
        print("Brak ticketów.")
        return

    for t in tickets:
        print(t)
