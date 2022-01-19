import tkinter as tk
from typing import Text
from calculatorclass import *

class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.calculator = Calculator()

        self.label_operand_1 = tk.Label(self.root, text = "Operand 1 ")
        self.label_operand_1.grid(row = 1, column = 1)
        self.entry_operand_1 = tk.Entry(self.root)
        self.entry_operand_1.grid(row = 1, column = 2)

        self.label_operator = tk.Label(self.root, text = "Operator (+-*/)")
        self.label_operator.grid(row = 2, column = 1)
        self.entry_operator = tk.Entry(self.root, width=1)
        self.entry_operator.grid(row = 2, column = 2)

        self.label_operand_2 = tk.Label(self.root, text = "Operand 2 ")
        self.label_operand_2.grid(row = 3, column = 1)
        self.entry_operand_2 = tk.Entry(self.root)
        self.entry_operand_2.grid(row = 3, column = 2)

        self.result_label = tk.Label(self.root, text = "Result ")
        self.result_label.grid(row = 4, column = 1)
        self.result_label2 = tk.Label(self.root, text = "")
        self.result_label2.grid(row = 4, column = 2)

        self.button_calculate = tk.Button(text="Calculate", 
                                          command=self.show_result)
        self.button_calculate.grid(row = 5, column=1)

        self.button_clear_log = tk.Button(text="Clear log", 
                                          command=self.clear_log)
        self.button_clear_log.grid(row = 5, column=2)

        self.button_exit = tk.Button(text="Exit", command=self.exit)
        self.button_exit.grid(row = 5, column=3)

        self.log_label = tk.Label(self.root, text="Log:")
        self.log_label.grid(row = 6, column=1)
        self.log_label2 = tk.Label(self.root, text="")
        self.log_label2.grid(row = 7, column=1)

        self.root.mainloop()

    def show_result(self):
        operand_1 = float( self.entry_operand_1.get() )
        operand_2 = float( self.entry_operand_2.get() )
        operator = self.entry_operator.get()
        self.calculator.calculate(operand_1, operand_2, operator)
        log = self.calculator.get_log()
        last_logged_element = log[-1]
        last_logged_element = last_logged_element.split("=")
        result = last_logged_element[-1]
        self.result_label2.configure(text = (f"{result}") )
        log_string = ""

        for expression in log:
            log_string += str(expression) + "\n" 
        self.log_label.configure(text=f"{log_string}")
    
    def clear_log(self):
        self.calculator.clear_log()
        self.log_label.configure(text="")

    def exit(self):
        self.root.destroy()

Window()