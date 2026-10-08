import sys
from helpdesk import Helpdesk
from database import DatabaseError

def print_tickets_table(tickets):
    if not tickets:
        print("\nbrak zgłoszeń do wyświetlenia.\n")
        return

    print("\n" + "=" * 105)
    print(f"{'ID':<4} | {'Użytkownik':<16} | {'Dział':<12} | {'Priorytet':<9} | {'Status':<8} | {'Opis':<25} | {'Data dodania'}")
    print("=" * 105)
    for t in tickets:
        desc = t['description'] if len(t['description']) <= 25 else t['description'][:22] + "..."
        print(f"{t['id']:<4} | {t['user_name']:<16} | {t['department']:<12} | {t['priority']:<9} | {t['status']:<8} | {desc:<25} | {t['created_at']}")
    print("=" * 105 + "\n")

def print_users_table(users):
    if not users:
        print("\nbrak użytkowników w bazie.\n")
        return

    print("\n" + "=" * 45)
    print(f"{'ID':<4} | {'Nazwa użytkownika':<20} | {'Dział':<15}")
    print("=" * 45)
    for u in users:
        print(f"{u['id']:<4} | {u['name']:<20} | {u['department']:<15}")
    print("=" * 45 + "\n")

def handle_add_user(helpdesk):
    name = input("podaj nazwę użytkownika: ").strip()
    dept = input("podaj dział: ").strip()
    if name and dept:
        try:
            u = helpdesk.add_user(name, dept)
            print(f"dodano użytkownika: {u['name']} (ID: {u['id']})")
        except ValueError as ve:
            print(f"ostrzeżenie: {ve}")
        except DatabaseError:
            print("wystąpił błąd bazy danych. szczegóły zostały zapisane w logu.")
    else:
        print("pola nie mogą być puste.")

def handle_add_ticket(helpdesk):
    try:
        users = helpdesk.get_users()
        if not users:
            print("\nbrak użytkowników w bazie. najpierw dodaj użytkownika.")
            return
        print_users_table(users)
        user_id = int(input("podaj ID użytkownika: "))
        desc = input("podaj opis zgłoszenia: ").strip()
        prio = input("podaj priorytet (low/medium/high): ").strip().lower()
        if prio not in ["low", "medium", "high"]:
            prio = "medium"
        if desc:
            t = helpdesk.add_ticket(user_id, desc, prio)
            print(f"utworzono ticket nr {t['id']}")
        else:
            print("opis nie może być pusty.")
    except ValueError as ve:
        print(f"błąd danych: {ve}")
    except DatabaseError:
        print("wystąpił błąd bazy danych. szczegóły zostały zapisane w logu.")

def handle_find_ticket(helpdesk):
    try:
        t_id = int(input("podaj ID ticketu: "))
        t = helpdesk.find_ticket(t_id)
        if t:
            print_tickets_table([t])
        else:
            print("nie znaleziono ticketu.")
    except ValueError:
        print("niepoprawne ID.")
    except DatabaseError:
        print("wystąpił błąd bazy danych. szczegóły zostały zapisane w logu.")

def handle_change_status(helpdesk):
    try:
        t_id = int(input("podaj ID ticketu: "))
        status = input("podaj nowy status (open/closed): ").strip().lower()
        if helpdesk.change_status(t_id, status):
            print("zmieniono status.")
        else:
            print("nie znaleziono ticketu.")
    except ValueError:
        print("niepoprawne ID.")
    except DatabaseError:
        print("wystąpił błąd bazy danych. szczegóły zostały zapisane w logu.")

def handle_delete_ticket(helpdesk):
    try:
        t_id = int(input("podaj ID ticketu do usunięcia: "))
        if helpdesk.delete_ticket(t_id):
            print("usunięto ticket.")
        else:
            print("nie znaleziono ticketu.")
    except ValueError:
        print("niepoprawne ID.")
    except DatabaseError:
        print("wystąpił błąd bazy danych. szczegóły zostały zapisane w logu.")

def main():
    try:
        helpdesk = Helpdesk()
    except DatabaseError:
        print("nie udało się połączyć z bazą danych. sprawdź plik helpdesk.log.")
        sys.exit(1)

    while True:
        print("--- Helpdesk Lite v0.6 ---")
        print("1. dodaj użytkownika")
        print("2. wyświetl użytkowników")
        print("3. dodaj ticket")
        print("4. znajdź ticket po ID")
        print("5. zmień status ticketu")
        print("6. wyświetl wszystkie tickety")
        print("7. wyświetl tylko otwarte tickety")
        print("8. usuń ticket")
        print("0. wyjście")

        choice = input("wybierz opcję: ").strip()

        try:
            if choice == "1":
                handle_add_user(helpdesk)
            elif choice == "2":
                print_users_table(helpdesk.get_users())
            elif choice == "3":
                handle_add_ticket(helpdesk)
            elif choice == "4":
                handle_find_ticket(helpdesk)
            elif choice == "5":
                handle_change_status(helpdesk)
            elif choice == "6":
                print_tickets_table(helpdesk.get_all_tickets())
            elif choice == "7":
                print_tickets_table(helpdesk.get_open_tickets())
            elif choice == "8":
                handle_delete_ticket(helpdesk)
            elif choice == "0":
                print("koniec programu.")
                sys.exit(0)
            else:
                print("nieprawidłowa opcja.\n")
        except DatabaseError:
            print("błąd bazy danych podczas wykonywania operacji. szczegóły w helpdesk.log.")

if __name__ == "__main__":
    main()