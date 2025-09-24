from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    def __init__(self, root):
        self.model = CalculatorModel()
        self.view = CalculatorView(root, self)

        self.bind_keys(root)

    def bind_keys(self, root):
        root.bind("<Key>", self.on_key_press)
        root.bind("<Return>", lambda event: self.on_button_click("="))
        root.bind("<BackSpace>", lambda event: self.on_button_click("⌫"))
        root.bind("<Escape>", lambda event: self.on_button_click("AC"))

    def on_key_press(self, event):
        if event.char.isdigit() or event.char in "+-*/.%":
            self.on_button_click(event.char)

    def on_button_click(self, text):
        if text == "AC":
            result = self.model.clear()
        elif text == "⌫":
            result = self.model.backspace()
        elif text == "=":
            result = self.model.calculate()
        elif text == "±":
            if self.model.expression.startswith("-"):
                self.model.expression = self.model.expression[1:]
            else:
                self.model.expression = "-" + self.model.expression
            result = self.model.expression
        else:
            result = self.model.add_to_expression(text)

        self.view.update_display(self.model.expression, result)