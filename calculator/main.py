import tkinter as tk
from calculator_ui import CalculatorUI
# запуск программы
def main():
    root = tk.Tk()
    app = CalculatorUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()