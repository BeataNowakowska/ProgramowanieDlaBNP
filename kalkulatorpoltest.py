import unittest
from kalkulatorpol import KalkulatorPol


class TestKalkulatorPol(unittest.TestCase):

    def setUp(self):
        self.kalk = KalkulatorPol()

    def test_pole_kwadratu(self):
        self.assertEqual(self.kalk.pole_kwadratu(3), 9)


if __name__ == '__main__':
    unittest.main()
