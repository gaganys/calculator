import customtkinter as ctk
from controller import CalculatorController

if __name__ == "__main__":
    root = ctk.CTk()
    app = CalculatorController(root)
    root.mainloop()