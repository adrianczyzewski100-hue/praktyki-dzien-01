class osoba:
    def __init__(self,imie , wiek):
        self.imie=imie  
        self.wiek=wiek

    def zmien_wiek(self, nowy_wiek):
        self.wiek=nowy_wiek

    def przedstaw_sie(self):
        print(f"nazywak sie {self.imie} i mam {self.wiek} lat")

osoba1 = osoba("Jan", 20)
osoba1.przedstaw_sie()
osoba1.zmien_wiek(30)
osoba1.przedstaw_sie()