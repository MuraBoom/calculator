import unittest
from memory import Memory


class TestMemory(unittest.TestCase):
    """Тесты для класса Memory в memory.py"""

    def setUp(self):
        # Создаем новый объект памяти перед каждым тестом
        self.mem = Memory()

    def test_memory_store_recall(self):
        # Проверка MS (сохранить) и MR (вспомнить)
        self.mem.memory_store(52)
        self.assertEqual(self.mem.memory_recall(), 52)  # функция assertEqual проверяет равенство двух
        # передаваемых в неё аргументов

    def test_memory_add_subtract(self):
        # Проверка M+
        self.mem.memory_store(10)
        self.mem.memory_add(5)
        self.assertEqual(self.mem.memory_recall(), 15)
        # Проверка M-
        self.mem.memory_subtract(3)
        self.assertEqual(self.mem.memory_recall(), 12)

    def test_memory_clear(self):
        # Проверка MC (очистка)
        self.mem.memory_store(100)
        self.mem.memory_clear()
        self.assertEqual(self.mem.memory_recall(), 0)

    def test_memory_display(self):
        # Проверка строкового представления для UI
        self.mem.memory_store(5)
        self.assertEqual(self.mem.get_display(), "M=5")


if __name__ == '__main__':
    unittest.main(verbosity=2)
