#1
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

#2
osoby = [
    {
        "id": 1,
        "imie": "Jan",
        "dzial": "IT"
    },
    {
        "id": 2,
        "imie": "Anna",
        "dzial": "HR"
    }
]
for osoba in osoby:
    print(f"ID: {osoba['id']}, Imię: {osoba['imie']}, Dział: {osoba['dzial']}")

#3
while True:
    print("1")
    print("2")
    print("3.wyjscie")
    wybor = input("Wybierz opcję: ")
    if wybor == "1":
        print("Wybrano opcję 1")
    elif wybor == "2":
        print("Wybrano opcję 2")   
    elif wybor == "3":
        print("Koniec programu")
        break
    else:
        print("nieprawidlowy wybor")

