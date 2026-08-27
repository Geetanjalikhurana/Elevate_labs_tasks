"""
Unit tests for calculator.py
"""

import unittest
from calculator import add, subtract, multiply, divide, power, modulus

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-5, -5), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 2), 4.5)
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(4, 0.5), 2.0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)

    def test_modulus_by_zero(self):
        with self.assertRaises(ValueError):
            modulus(10, 0)

if __name__ == '__main__':
    unittest.main()
