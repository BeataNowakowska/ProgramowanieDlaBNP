class Zwierze:

  def reakcja_na_wolanie(self):
    print("Zwierzę patrzy obojętnie...")


class Kot(Zwierze):

  def reakcja_na_wolanie(self):
    print("Kot: *ignoruje właściciela z pogardą*")


class Pies(Zwierze):

  def reakcja_na_wolanie(self):
    print("Pies: biegnie, szczeka i macha ogonem!")


class Chomik(Zwierze):

  def reakcja_na_wolanie(self):
    print("Chomik Krysia: chowa się w trociny i udaje, że jej nie ma 🐹")


# Przykład użycia
zwierzeta = [Kot(), Pies(), Chomik()]

print("Zwierzaki chodźcie !!!")
print("")
for z in zwierzeta:
  z.reakcja_na_wolanie()
