class Calculator:
    def __init__(self):
        self.log = []

    def calculate(self, operand_1, operand_2, operator):
        result_string = ""
        expression = f"{operand_1} {operator} {operand_2} = "

        if operator == '+':
            result_string = f"{expression} {operand_1 + operand_2}"
        elif operator == '-':
            result_string = f"{expression} {operand_1 - operand_2}"
        elif operator == '*':
            result_string = f"{expression} {operand_1 * operand_2}"
        elif operator == '/':
            result_string = f"{expression} {operand_1 / operand_2}"

        self.log.append(result_string)

    
    def get_log(self):
        return self.log

    def get_last_logged(self):
        if len(self.log) > 1:
            return self.log[ len(self.log) - 1 ]

    def clear_log(self):
        self.log = []

def main():
    calculator = Calculator()
    calculator.calculate(1,2,'+')
    calculator.calculate(2,2,'*')
    calculator.calculate(16,2,'/')
    print(calculator.get_log())
    print(calculator.get_last_logged())

if __name__ == "__main__":
    main()