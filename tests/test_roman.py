import unittest
from calculus_romanus.roman import to_roman, from_roman


class TestRomanNumerals(unittest.TestCase):
    def test_to_roman(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3), "III")
        self.assertEqual(to_roman(4), "IV")
        self.assertEqual(to_roman(5), "V")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(10), "X")
        self.assertEqual(to_roman(40), "XL")
        self.assertEqual(to_roman(50), "L")
        self.assertEqual(to_roman(90), "XC")
        self.assertEqual(to_roman(100), "C")
        self.assertEqual(to_roman(400), "CD")
        self.assertEqual(to_roman(500), "D")
        self.assertEqual(to_roman(900), "CM")
        self.assertEqual(to_roman(1000), "M")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(4000)

    def test_from_roman(self):
        self.assertEqual(from_roman("I"), 1)
        self.assertEqual(from_roman("III"), 3)
        self.assertEqual(from_roman("IV"), 4)
        self.assertEqual(from_roman("V"), 5)
        self.assertEqual(from_roman("IX"), 9)
        self.assertEqual(from_roman("X"), 10)
        self.assertEqual(from_roman("XL"), 40)
        self.assertEqual(from_roman("L"), 50)
        self.assertEqual(from_roman("XC"), 90)
        self.assertEqual(from_roman("C"), 100)
        self.assertEqual(from_roman("CD"), 400)
        self.assertEqual(from_roman("D"), 500)
        self.assertEqual(from_roman("CM"), 900)
        self.assertEqual(from_roman("M"), 1000)
        self.assertEqual(from_roman("MCMXCIV"), 1994)
        self.assertEqual(from_roman("MMMCMXCIX"), 3999)


if __name__ == "__main__":
    unittest.main()
