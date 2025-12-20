from operations import *
from memory import Memory


class CalculatorLogic:
    def __init__(self):
        self.current = "0"
        self.previous = None
        self.operation = None
        self.memory = Memory()
        self.reset_next = False  # Флаг, если True, то следующий ввод очищает предыдущее число.
        # True после нажатия на операцию. в иных случаях False.

    def press_number(self, num):
        # Если на экране 0 или вводится следующее число,
        # то перезаписываем число на экране цифрой, которую нажал пользователь
        if self.reset_next or self.current == "0":
            self.current = num
            self.reset_next = False
        else:
            self.current += num

    def press_dot(self):
        if "." not in self.current:
            self.current += "."

    def set_operation(self, op):
        # Условие, необходимое для цепочки операторов. Пример: 5+3+1 = 9
        if self.operation and not self.reset_next:
            self.calculate()
        self.previous = float(self.current)
        self.operation = op
        self.reset_next = True

    def calculate(self):
        if self.operation is None or self.previous is None:
            return

        current_num = float(self.current)
        result = None

        try:
            if self.operation == "+":
                result = add(self.previous, current_num)
            elif self.operation == "-":
                result = subtract(self.previous, current_num)
            elif self.operation == "*":
                result = multiply(self.previous, current_num)
            elif self.operation == "/":
                result = divide(self.previous, current_num)
            elif self.operation == "%":
                result = remainder(self.previous, current_num)
            elif self.operation == "^":
                result = power(self.previous, current_num)

            # убираем лишние нули
            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = str(round(result, 10)).rstrip('0').rstrip('.')

        except ValueError as e:
            self.current = str(e)
        except:
            self.current = "Неизвестная ошибка"

        self.operation = None
        self.reset_next = True

    def unary_operation(self, op):
        num = float(self.current)
        result = None

        try:
            if op == "√":
                result = square_root(num)
            elif op == "sin":
                result = sin_func(num)
            elif op == "cos":
                result = cos_func(num)
            elif op == "floor":
                result = floor_func(num)
            elif op == "ceil":
                result = ceil_func(num)

            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = str(round(result, 10)).rstrip('0').rstrip('.')
        except ValueError as e:
            self.current = str(e)
        except:
            self.current = "Неизвестная ошибка"

        self.reset_next = True

    def clear_all(self):
        self.current = "0"
        self.previous = None
        self.operation = None

    def delete(self):
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"

    def get_display(self):
        return self.current
