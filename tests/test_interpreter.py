import unittest
from unittest.mock import patch
from io import StringIO
from calculus_romanus.interpreter import run_calculus_romanus


class TestInterpreter(unittest.TestCase):
    def assert_calculus_romanus(self, code, expected_output):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            run_calculus_romanus(code)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_addition(self):
        self.assert_calculus_romanus("Scribo V addit III", "VIII")

    def test_subtraction(self):
        self.assert_calculus_romanus("Scribo X minuit IV", "VI")

    def test_multiplication(self):
        self.assert_calculus_romanus("Scribo II multiplicat III", "VI")

    def test_assignment(self):
        code = """
        x est V
        y est X
        Scribo x addit y
        """
        self.assert_calculus_romanus(code, "XV")

    def test_precedence(self):
        # NOTE: The interpreter evaluates expressions from left to right without standard operator precedence.
        # This test confirms the current behavior: (X + V) * II = XXX
        self.assert_calculus_romanus("Scribo X addit V multiplicat II", "XXX")

    def test_non_positive_numbers(self):
        with self.assertRaises(ValueError):
            run_calculus_romanus("Scribo V minuit V")  # 5 - 5 = 0
        with self.assertRaises(ValueError):
            run_calculus_romanus("Scribo V minuit X")  # 5 - 10 = -5
        with self.assertRaises(ValueError):
            run_calculus_romanus("x est V minuit X")  # x = -5


if __name__ == "__main__":
    unittest.main()
