class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def clear(self):
        self.expression = ""
        return "0"

    def backspace(self):
        self.expression = self.expression[:-1]
        return self.expression if self.expression else "0"

    def add_to_expression(self, value):
        self.expression += str(value)
        return self.expression

    def calculate(self):
        if not self.expression:
            return "0"
        exp = self.expression.replace("×", "*").replace("÷", "/").replace("−", "-")
        try:
            result = eval(exp)
            self.expression = str(result)
            return self.expression
        except Exception:
            self.expression = ""
            return "Ошибка"