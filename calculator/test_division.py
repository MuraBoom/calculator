import unittest
from operations import divide
class TestDivisionOperation(unittest.TestCase):

    def test_01_normal_division(self):
        #тест нормального деления 10 / 2 = 5
        result = divide(10, 2)
        self.assertEqual(result, 5,
                         "Ошибка: 10 / 2 должно быть 5")
        print("10 / 2 = 5 - работает корректно")

    def test_02_float_division(self):
        #тест деления с плавающей точкой 5 / 2 = 2.5
        result = divide(5, 2)
        self.assertEqual(result, 2.5,
                         "Ошибка: 5 / 2 должно быть 2.5")
        print("5 / 2 = 2.5 - работает корректно")

    def test_03_division_by_zero(self):
        #тест деления на ноль должно вернуть сообщение об ошибке
        result = divide(10, 0)
        expected = "ошибка: деление на ноль"
        self.assertEqual(result, expected,
                         f"Ошибка: должно быть '{expected}', а получили '{result}'")
        print(f"10 / 0 = '{result}' - работает корректно")

    def test_04_negative_division(self):
        #тест деления отрицательных чисел -10 / 2 = -5
        result = divide(-10, 2)
        self.assertEqual(result, -5,
                         "Ошибка: -10 / 2 должно быть -5")
        print("-10 / 2 = -5 - работает корректно")

    def test_05_zero_divided_by_number(self):
        #тест деления нуля на число 0 / 5 = 0
        result = divide(0, 5)
        self.assertEqual(result, 0,
                         "Ошибка: 0 / 5 должно быть 0")
        print("0 / 5 = 0 - работает корректно")


if __name__ == '__main__':
    #создаем набор тестов(Test Suite)
    #находит все методы начинающиеся с 'test_' в классе TestDivisionOperation и добавляет их в набор
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDivisionOperation)

    #запускаем тесты с подробным выводом
    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)

