class KalkulatorPol:
  def pole_kola(self, promien):
      return 3.14159 * float(promien) ** 2

  def pole_kwadratu(self, bok):
      return float(bok) ** 2

  def pole_prostokata(self, bok1, bok2):
      return float(bok1) * float(bok2)

  def pole_trojkata(self, podstawa, wysokosc):
      return (float(podstawa) * float(wysokosc)) / 2

  def oblicz(self, figura, *wymiary):
      figura = figura.strip().lower()
      if figura == "koło":
          return self.pole_kola(*wymiary)
      elif figura == "kwadrat":
          return self.pole_kwadratu(*wymiary)
      elif figura == "prostokąt":
          return self.pole_prostokata(*wymiary)
      elif figura == "trójkąt":
          return self.pole_trojkata(*wymiary)
      else:
          raise ValueError("Nieznana figura lub nieprawidłowe parametry.")

def uruchom_interaktywnie():
    kalkulator = KalkulatorPol()
    figura = input("Jakiej figury pole chcesz policzyć? (koło, kwadrat, prostokąt, trójkąt): ").strip().lower()

    try:
        if figura == "koło":
            r = float(input("Podaj promień: "))
            pole = kalkulator.pole_kola(r)
        elif figura == "kwadrat":
            a = float(input("Podaj długość boku: "))
            pole = kalkulator.pole_kwadratu(a)
        elif figura == "prostokąt":
            a = float(input("Podaj długość pierwszego boku: "))
            b = float(input("Podaj długość drugiego boku: "))
            pole = kalkulator.pole_prostokata(a, b)
        elif figura == "trójkąt":
            a = float(input("Podaj długość podstawy: "))
            h = float(input("Podaj wysokość: "))
            pole = kalkulator.pole_trojkata(a, h)
        else:
            print("Nieznana figura.")
            return

        print(f"Pole {figura} wynosi {pole:.2f}")
    except ValueError:
        print("Błąd: podano nieprawidłowe dane.")
