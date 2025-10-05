import unittest
from test_bmi import oblicz_bmi, zakres_prawidlowej_wagi

class TestBMI(unittest.TestCase):

    def test_oblicz_bmi_ok(self):
        bmi_val, kat = oblicz_bmi(70, 1.75)
        self.assertAlmostEqual(bmi_val, 22.9, places=1)
        self.assertEqual(kat, "waga prawidłowa")

    def test_zakres_prawidlowej_wagi_ok(self):
        min_w, max_w = zakres_prawidlowej_wagi(1.75)
        self.assertEqual(min_w, 56.7)
        self.assertEqual(max_w, 76.3)


if __name__ == "__main__":
    unittest.main()
