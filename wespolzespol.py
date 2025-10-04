import random
import time
from abc import ABC, abstractmethod


class OsobaIT(ABC):

    def __init__(self, imie):
        self.imie = imie
        self.profesja = ""
        self.tekst = ""

    def daj_glos(self):
        return f"{self.imie}, jak to {self.profesja}, mówi: {self.tekst}"


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


class ScrumMaster(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "Scrum Masterka"
        self.tekst = "Czuję, że powinniśmy zrobić burzę mózgów."


class DevOps(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "DevOpsowiec"
        self.tekst = "W produkcji? To ciekawe..."


class ProductOwner(OsobaIT):

    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "Product Ownerka"
        self.tekst = "Czy możemy to mieć na wczoraj?"


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
    random.shuffle(osoby)  # tasowanie ukryte tutaj
    return osoby


def main():
    ania = Programista("Ania")
    print(ania.daj_glos())


if __name__ == "__main__":
    main()
