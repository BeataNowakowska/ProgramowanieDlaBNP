import random
import time
from abc import ABC, abstractmethod


class OsobaIT(ABC):

    def __init__(self, imie):
        self.imie = imie
        self.profesja = ""
        self.tekst = ""

    def daj_glos(self):
        return self.imie + " mówi: " + self.tekst

    def zgoda(self):
        return self.imie + ": Tak"


class Programista(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "programistka"
        self.tekst = "U mnie działa, pewnie masz coś źle ustawione."


class Tester(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "tester"
        self.tekst = "O, znowu coś zepsuliście."

    def zgoda(self):
        return self.imie + ": No może być"


class ScrumMaster(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "Scrum Masterka"
        self.tekst = "Czuję, że powinniśmy zrobić burzę mózgów."

    def zgoda(self):
        return self.imie + ": Ależ oczywiście"


class DevOps(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "DevOpsowiec"
        self.tekst = "W produkcji? To ciekawe..."

    def zgoda(self):
        return self.imie + ": OK"


class ProductOwner(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "Product Ownerka"
        self.tekst = "Czy możemy to mieć na wczoraj?"

    def zgoda(self):
        return self.imie + ": Wyrażam zgodę"


class UXDesigner(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "UX designer"
        self.tekst = "To trzeba zrobić bardziej intuicyjnie."


def stworz_osoby():
    osoby = [
        Programista("Ania"),
        Tester("Bartek"),
        ScrumMaster("Celina"),
        DevOps("Darek"),
        ProductOwner("Ewa"),
        UXDesigner("Filip"),
    ]

    return osoby


def wszycy_się_zgadzają():
    osoby = stworz_osoby()
    print("Czy zgadzamy się co do celu Sprintu?")
    print()

    for i in osoby:
        print(i.zgoda())


def main():
    ania = Programista("Ania")
    print(ania.daj_glos())
    bartek = ProductOwner("Barter")
    print(bartek.daj_glos())

    wszycy_się_zgadzają()


if __name__ == "__main__":
    main()
