class Product:
    def __init__(self, produkt, cena):
        self.produkt = produkt
        self.cena = cena

    def display(self):
        print(f"Produkt: {self.produkt}, cena: {self.cena} zł")

class User:
    def __init__(self,imie, dzial):
        self.imie = imie
        self.dzial = dzial

    def display(self):
            print(f"imie: {self.imie}, dzial: {self.dzial} ")

    def change_department(self, nowy_dzial):
        self.dzial = nowy_dzial
        print(f"dzial {self.imie} zostal zmieniony na: {nowy_dzial}")

    def __str__(self):
        return f"uzytkownik: {self.imie}, dzial: {self.dzial}"

p1 = Product("laptop",1500)
p2 = Product("drukarka",700)
u = User("Jan", "IT")

u.display()
p1.display()
p2.display()

u.change_department("HQ")

u.display()
print(u)

#klasa --- zbior obiektow atrybutow i metod
#obiekt --- np. w klasie user obiektem jest uzytkownik
#metoda --- funkcja