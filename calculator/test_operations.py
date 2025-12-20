import unittest
from operations import *


class TestOperations(unittest.TestCase):
    """Тесты для математических функций в operations.py"""

    def test_basic_arithmetic(self):
        # Проверка базового сложения, вычитания, умножения
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(multiply(10, 5), 50)

    def test_power_and_root(self):
        # Возведение в степень
        self.assertEqual(power(2, 3), 8)
        # Квадратный корень
        self.assertEqual(square_root(16), 4)
        # Корень из отрицательного числа
        self.assertRaises(ValueError, square_root, -1)

    def test_trigonometry_and_rounding(self):
        # Округление вниз и вверх
        self.assertEqual(floor_func(3.9), 3)
        self.assertEqual(ceil_func(3.1), 4)
        # Тригонометрия (проверка примерных значений)
        self.assertAlmostEqual(sin_func(0), 0)
        self.assertAlmostEqual(cos_func(0), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
