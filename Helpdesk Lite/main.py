"""
główny moduł aplikacji obsługujący interfejs użytkownika w konsoli.
"""

from helpdesk import Helpdesk
from validators import validate_user, validate_description, validate_priority

def get_ticket_id(message):
    """pobiera od użytkownika liczbę całkowitą (id). obsługuje błąd konwersji."""
    try:
        return int(input(message))
    except ValueError:
        print("Błąd: wpisano tekst zamiast liczby.")
        return None

def display_menu():
    """wyświetla opcje menu głównego."""
    print("\nMenu:")
    print("1. Dodaj ticket")
    print("2. Znajdź ticket po ID")
    print("3. Zmień status ticketu")
    print("4. Wyświetl wszystkie tickety")
    print("5. Usuń ticket")
    print("6. Filtruj tickety")
    print("7. Wyjście")

def handle_add(helpdesk):
    """obsługuje interaktywny proces dodawania nowego ticketu."""
    user = input("Podaj nazwę użytkownika: ").strip()
    if not validate_user(user):
        print("Błąd: nazwa użytkownika nie może być pusta.")
        return

    description = input("Podaj opis problemu: ").strip()
    if not validate_description(description):
        print("Błąd: opis problemu nie może być pusty.")
        return

    priority = input("Podaj priorytet (low/medium/high): ").strip().lower()
    if not validate_priority(priority):
        print("Błąd: priorytet musi być low/medium/high.")
        return

    ticket = helpdesk.add_ticket(user, description, priority)
    print(f"Ticket {ticket.id} został dodany.")

def handle_find(helpdesk):
    """obsługuje wyszukiwanie ticketu po id."""
    ticket_id = get_ticket_id("Podaj ID ticketu: ")
    if ticket_id is not None:
        ticket = helpdesk.find_ticket(ticket_id)
        print(ticket if ticket else "Nie znaleziono ticketu.")

def handle_change_status(helpdesk):
    """obsługuje zmianę statusu zgłoszenia."""
    ticket_id = get_ticket_id("Podaj ID ticketu: ")
    if ticket_id is not None:
        new_status = input("Podaj nowy status: ")
        if helpdesk.change_status(ticket_id, new_status):
            print(f"Status ticketu {ticket_id} został zmieniony.")
        else:
            print("Nie znaleziono ticketu.")

def handle_show_all(helpdesk):
    """wyświetla wszystkie zgłoszenia z bazy."""
    tickets = helpdesk.get_all_tickets()
    if not tickets:
        print("Brak ticketów.")
        return
    for t in tickets:
        print(t)

def handle_delete(helpdesk):
    """obsługuje usuwanie zgłoszenia z bazy."""
    ticket_id = get_ticket_id("Podaj ID ticketu do usunięcia: ")
    if ticket_id is not None:
        if helpdesk.delete_ticket(ticket_id):
            print(f"Ticket {ticket_id} został usunięty.")
        else:
            print("Nie znaleziono ticketu.")

def handle_filter(helpdesk):
    """obsługuje filtrowanie zgłoszeń według statusu i/lub priorytetu."""
    status = input("Podaj status do filtrowania (lub enter aby pominąć): ").strip()
    priority = input("Podaj priorytet do filtrowania (low/medium/high lub enter): ").strip()

    filtered = helpdesk.filter_tickets(
        status=status if status else None,
        priority=priority if priority else None
    )
    if not filtered:
        print("Brak ticketów spełniających kryteria.")
        return
    for t in filtered:
        print(t)

def main():
    """główna pętla sterująca aplikacją."""
    helpdesk = Helpdesk()
    # mapa akcji przypisująca wybór z menu do odpowiednich funkcji
    actions = {
        "1": lambda: handle_add(helpdesk),
        "2": lambda: handle_find(helpdesk),
        "3": lambda: handle_change_status(helpdesk),
        "4": lambda: handle_show_all(helpdesk),
        "5": lambda: handle_delete(helpdesk),
        "6": lambda: handle_filter(helpdesk),
    }

    while True:
        display_menu()
        choice = input("Wybierz opcję: ")

        if choice == "7":
            print("Koniec programu.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()