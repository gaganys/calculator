import customtkinter as ctk

class CalculatorView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Калькулятор")
        self.root.geometry("420x560")
        self.root.resizable(False, False)

        ctk.set_appearance_mode("light")

        self.expression_var = ctk.StringVar(value="")
        self.result_var = ctk.StringVar(value="0")

        self.display_frame = ctk.CTkFrame(self.root)
        self.display_frame.pack(pady=15, padx=15, fill="x")

        self.expression_label = ctk.CTkLabel(self.display_frame, textvariable=self.expression_var, font=("Arial", 16), anchor="e")
        self.expression_label.pack(fill="x")

        self.result_label = ctk.CTkLabel(self.display_frame, textvariable=self.result_var, font=("Arial", 32, "bold"), anchor="e")
        self.result_label.pack(fill="x")

        self.create_buttons()

    def create_buttons(self):
        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=5, padx=5, fill="both", expand=True)

        buttons = [
            ("AC", "⌫", "±", "÷"),
            ("7", "8", "9", "×"),
            ("4", "5", "6", "−"),
            ("1", "2", "3", "+"),
            ("0", "00", ".", "=")
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                button = ctk.CTkButton(
                    button_frame, text=btn_text, font=("Arial", 20),
                    width=60, height=60, corner_radius=15,
                    fg_color="#ECF0F1", hover_color="#BDC3C7", text_color="#000",
                    command=lambda text=btn_text: self.controller.on_button_click(text)
                )
                button.grid(row=i, column=j, padx=8, pady=8, sticky="nsew")

        for j in range(4):
            button_frame.columnconfigure(j, weight=1)
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)

    def update_display(self, expression, result):
        self.expression_var.set(expression)
        self.result_var.set(result)