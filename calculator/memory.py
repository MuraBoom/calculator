# работа с памятью калькулятора
class Memory:
    def __init__(self):
        self.value = 0
    
    def memory_add(self, num):
        # M+ - добавить в память
        self.value += num
    
    def memory_subtract(self, num):
        # M- - вычесть из памяти
        self.value -= num
    
    def memory_store(self, num):
        # MS - запомнить число
        self.value = num
    
    def memory_recall(self):
        # MR - вспомнить
        return self.value
    
    def memory_clear(self):
        # MC - очистить память
        self.value = 0
    
    def get_display(self):
        # показать значение памяти
        return f"M={self.value}"

