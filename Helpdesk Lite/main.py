from tickets import add_ticket, find_ticket, change_status, delete_ticket, show_tickets

def main():
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
            print(ticket if ticket else "Nie znaleziono ticketu.")

        elif choice == "3":
            try:
                id = int(input("Podaj ID ticketu: "))
            except ValueError:
                print("Błąd: wpisano tekst zamiast liczby.")
                continue

            new_status = input("Podaj nowy status: ")
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
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
