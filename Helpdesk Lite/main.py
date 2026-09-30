import sys
from helpdesk import Helpdesk

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

def select_user_prompt(helpdesk):
    users = helpdesk.get_users()
    if not users:
        print("\nbrak użytkowników w bazie. najpierw dodaj użytkownika.")
        name = input("podaj nazwę nowego użytkownika: ").strip()
        dept = input("podaj dział: ").strip()
        if not name or not dept:
            print("anulowano.")
            return None
        user = helpdesk.add_user(name, dept)
        return user["id"]

    print_users_table(users)
    try:
        user_id = int(input("podaj ID użytkownika: "))
        if any(u["id"] == user_id for u in users):
            return user_id
        print("nie znaleziono użytkownika o takim ID.")
    except ValueError:
        print("niepoprawne ID.")
    return None

def handle_add_user(helpdesk):
    name = input("podaj nazwę użytkownika: ").strip()
    dept = input("podaj dział: ").strip()
    if name and dept:
        try:
            u = helpdesk.add_user(name, dept)
            print(f"dodano użytkownika: {u['name']} (ID: {u['id']})")
        except Exception as e:
            print(f"błąd podczas dodawania użytkownika: {e}")
    else:
        print("pola nie mogą być puste.")

def handle_add_ticket(helpdesk):
    user_id = select_user_prompt(helpdesk)
    if not user_id:
        return
    desc = input("podaj opis zgłoszenia: ").strip()
    prio = input("podaj priorytet (low/medium/high): ").strip().lower()
    if prio not in ["low", "medium", "high"]:
        prio = "medium"
    if desc:
        t = helpdesk.add_ticket(user_id, desc, prio)
        print(f"utworzono ticket nr {t['id']}")
    else:
        print("opis nie może być pusty.")

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

def handle_tickets_by_user(helpdesk):
    users = helpdesk.get_users()
    print_users_table(users)
    try:
        u_id = int(input("podaj ID użytkownika: "))
        tickets = helpdesk.get_tickets_by_user(u_id)
        print_tickets_table(tickets)
    except ValueError:
        print("niepoprawne ID.")

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

def handle_delete_ticket(helpdesk):
    try:
        t_id = int(input("podaj ID ticketu do usunięcia: "))
        if helpdesk.delete_ticket(t_id):
            print("usunięto ticket.")
        else:
            print("nie znaleziono ticketu.")
    except ValueError:
        print("niepoprawne ID.")

def handle_export(helpdesk):
    mode = input("eksportować tylko otwarte? (t/n): ").strip().lower()
    open_only = mode == 't'
    filename, count = helpdesk.export_to_csv(open_only=open_only)
    print(f"wyeksportowano {count} zgłoszeń do pliku {filename}")

def main():
    helpdesk = Helpdesk()

    while True:
        print("--- Helpdesk Lite v0.6 ---")
        print("1. dodaj użytkownika")
        print("2. wyświetl użytkowników")
        print("3. dodaj ticket")
        print("4. znajdź ticket po ID")
        print("5. wyświetl tickety wybranego użytkownika")
        print("6. zmień status ticketu")
        print("7. wyświetl wszystkie tickety")
        print("8. wyświetl tylko otwarte tickety")
        print("9. usuń ticket")
        print("10. eksportuj raport do CSV")
        print("0. wyjście")

        choice = input("wybierz opcję: ").strip()

        if choice == "1":
            handle_add_user(helpdesk)
        elif choice == "2":
            print_users_table(helpdesk.get_users())
        elif choice == "3":
            handle_add_ticket(helpdesk)
        elif choice == "4":
            handle_find_ticket(helpdesk)
        elif choice == "5":
            handle_tickets_by_user(helpdesk)
        elif choice == "6":
            handle_change_status(helpdesk)
        elif choice == "7":
            print_tickets_table(helpdesk.get_all_tickets())
        elif choice == "8":
            print_tickets_table(helpdesk.get_open_tickets())
        elif choice == "9":
            handle_delete_ticket(helpdesk)
        elif choice == "10":
            handle_export(helpdesk)
        elif choice == "0":
            print("koniec programu.")
            sys.exit(0)
        else:
            print("nieprawidłowa opcja.\n")

if __name__ == "__main__":
    main()