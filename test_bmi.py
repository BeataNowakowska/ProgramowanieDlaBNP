# bmi.py
MIN_WZROST = 0.5   # m
MAX_WZROST = 2.5   # m
MIN_WAGA   = 10.0  # kg
MAX_WAGA   = 400.0 # kg

def _sprawdz_wage_i_wzrost(waga: float, wzrost: float) -> None:
    if not (MIN_WAGA <= waga <= MAX_WAGA):
        raise ValueError(f"Nieprawidłowa waga: {waga} kg (dozwolone {MIN_WAGA}–{MAX_WAGA} kg).")
    if not (MIN_WZROST <= wzrost <= MAX_WZROST):
        raise ValueError(f"Nieprawidłowy wzrost: {wzrost} m (dozwolone {MIN_WZROST}–{MAX_WZROST} m).")

def _sprawdz_wzrost(wzrost: float) -> None:
    if not (MIN_WZROST <= wzrost <= MAX_WZROST):
        raise ValueError(f"Nieprawidłowy wzrost: {wzrost} m (dozwolone {MIN_WZROST}–{MAX_WZROST} m).")

def oblicz_bmi(waga: float, wzrost: float):
    """Zwraca (bmi, kategoria). Waliduje wejście."""
    _sprawdz_wage_i_wzrost(waga, wzrost)
    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        kategoria = "niedowaga"
    elif bmi < 25:
        kategoria = "waga prawidłowa"
    elif bmi < 30:
        kategoria = "nadwaga"
    else:
        kategoria = "otyłość"
    return bmi, kategoria

def zakres_prawidlowej_wagi(wzrost: float):
    """Zwraca (min_kg, max_kg) dla BMI 18.5–24.9. Waliduje wzrost."""
    _sprawdz_wzrost(wzrost)
    min_waga = 18.5 * (wzrost ** 2)
    max_waga = 24.9 * (wzrost ** 2)
    return round(min_waga, 1), round(max_waga, 1)

if __name__ == "__main__":
    try:
        waga = float(input("Podaj swoją wagę (kg): "))
        wzrost = float(input("Podaj swój wzrost (m): "))
        bmi, kategoria = oblicz_bmi(waga, wzrost)
        print(f"\nTwoje BMI: {bmi:.2f} | Kategoria: {kategoria}")
        min_w, max_w = zakres_prawidlowej_wagi(wzrost)
        print(f"Prawidłowa waga dla {wzrost:.2f} m: {min_w}–{max_w} kg")
    except ValueError as e:
        print(f"Błąd: {e}")
