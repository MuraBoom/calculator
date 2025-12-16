
import tkinter as tk
from calculator_logic import CalculatorLogic

# интерфейс калькулятора
class CalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x550")
        self.root.configure(bg="#E6E6FA")  # светло-лиловый фон
        
        # логика калькулятора
        self.calc = CalculatorLogic()
        
        # создаем все элементы
        self.create_widgets()
        
        # настройка сетки
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
    
    def create_widgets(self):
        # отображение памяти
        self.memory_label = tk.Label(self.root, text="M=0", bg="#D8BFD8", font=("Arial", 10))
        self.memory_label.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        
        # основное поле ввода
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(self.root, textvariable=self.display_var, 
                               font=("Arial", 24), justify="right", bd=0, bg="#FFFFFF")
        self.display.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        self.display.config(state="readonly")
        
        # кнопки памяти (лиловые)
        memory_buttons = [
            ("MC", 2, 0, self.mc_click, "#9370DB"),
            ("MR", 2, 1, self.mr_click, "#9370DB"),
            ("M+", 2, 2, self.mplus_click, "#9370DB"),
            ("M-", 2, 3, self.mminus_click, "#9370DB"),
            ("MS", 2, 4, self.ms_click, "#9370DB")
        ]
        
        for text, row, col, cmd, color in memory_buttons:
            btn = tk.Button(self.root, text=text, command=cmd, bg=color, fg="white",
                           font=("Arial", 12), relief="flat")
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        # цифры и операции
        buttons = [
            ("C", 3, 0, self.clear_click, "#BA55D3"),
            ("⌫", 3, 1, self.delete_click, "#BA55D3"),
            ("%", 3, 2, lambda: self.op_click("%"), "#DA70D6"),
            ("/", 3, 3, lambda: self.op_click("/"), "#DA70D6"),
            ("√", 3, 4, lambda: self.unary_click("√"), "#EE82EE"),
            
            ("7", 4, 0, lambda: self.num_click("7"), "#E6E6FA"),
            ("8", 4, 1, lambda: self.num_click("8"), "#E6E6FA"),
            ("9", 4, 2, lambda: self.num_click("9"), "#E6E6FA"),
            ("*", 4, 3, lambda: self.op_click("*"), "#DA70D6"),
            ("sin", 4, 4, lambda: self.unary_click("sin"), "#EE82EE"),
            
            ("4", 5, 0, lambda: self.num_click("4"), "#E6E6FA"),
            ("5", 5, 1, lambda: self.num_click("5"), "#E6E6FA"),
            ("6", 5, 2, lambda: self.num_click("6"), "#E6E6FA"),
            ("-", 5, 3, lambda: self.op_click("-"), "#DA70D6"),
            ("cos", 5, 4, lambda: self.unary_click("cos"), "#EE82EE"),
            
            ("1", 6, 0, lambda: self.num_click("1"), "#E6E6FA"),
            ("2", 6, 1, lambda: self.num_click("2"), "#E6E6FA"),
            ("3", 6, 2, lambda: self.num_click("3"), "#E6E6FA"),
            ("+", 6, 3, lambda: self.op_click("+"), "#DA70D6"),
            ("floor", 6, 4, lambda: self.unary_click("floor"), "#EE82EE"),
            
            ("0", 7, 0, lambda: self.num_click("0"), "#E6E6FA"),
            (".", 7, 1, self.dot_click, "#E6E6FA"),
            ("=", 7, 2, self.equal_click, "#8A2BE2"),
            ("^", 7, 3, lambda: self.op_click("^"), "#DA70D6"),
            ("ceil", 7, 4, lambda: self.unary_click("ceil"), "#EE82EE")
        ]
        
        for text, row, col, cmd, color in buttons:
            btn = tk.Button(self.root, text=text, command=cmd, bg=color, 
                           font=("Arial", 12), relief="flat")
            if color == "#E6E6FA":
                btn.config(fg="black")  # цифры черным
            else:
                btn.config(fg="white")  # остальное белым
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    
    def update_display(self):
        # обновляем поле ввода
        self.display_var.set(self.calc.get_display())
        # обновляем память
        self.memory_label.config(text=self.calc.memory.get_display())
    
    # обработчики кнопок
    def num_click(self, num):
        self.calc.press_number(num)
        self.update_display()
    
    def dot_click(self):
        self.calc.press_dot()
        self.update_display()
    
    def op_click(self, op):
        self.calc.set_operation(op)
        self.update_display()
    
    def equal_click(self):
        self.calc.calculate()
        self.update_display()
    
    def unary_click(self, op):
        self.calc.unary_operation(op)
        self.update_display()
    
    def clear_click(self):
        self.calc.clear()
        self.update_display()
    
    def delete_click(self):
        self.calc.delete()
        self.update_display()
    
    # кнопки памяти
    def mc_click(self):
        self.calc.memory.memory_clear()
        self.update_display()
    
    def mr_click(self):
        value = self.calc.memory.memory_recall()
        self.calc.current = str(value)
        self.update_display()
    
    def mplus_click(self):
        try:
            num = float(self.calc.current)
            self.calc.memory.memory_add(num)
            self.update_display()
        except:
            pass
    
    def mminus_click(self):
        try:
            num = float(self.calc.current)
            self.calc.memory.memory_subtract(num)
            self.update_display()
        except:
            pass
    
    def ms_click(self):
        try:
            num = float(self.calc.current)
            self.calc.memory.memory_store(num)
            self.update_display()
        except:
            pass
