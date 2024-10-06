import tkinter as tk
from tkinter import messagebox


class MiniComputer:
    def __init__(self):
        self.memory = {}

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Error: Division by zero"

    def store(self, name, value):
        self.memory[name] = value
        return f'Stored {value} in memory as {name}.'

    def retrieve(self, name):
        return self.memory.get(name, "Error: Name not found in memory.")

    def clear_memory(self):
        self.memory.clear()
        return "Memory cleared."

    def list_memory(self):
        return self.memory if self.memory else "Memory is empty."


class MiniComputerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Mini Computer")
        self.mini_computer = MiniComputer()

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Input field
        self.input_field = tk.Entry(self.master, width=30)
        self.input_field.pack(pady=10)

        # Display result
        self.result_display = tk.Entry(self.master, textvariable=self.result_var, width=30, state='readonly')
        self.result_display.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        buttons = [
            ("Add", self.add),
            ("Subtract", self.subtract),
            ("Multiply", self.multiply),
            ("Divide", self.divide),
            ("Store", self.store),
            ("Retrieve", self.retrieve),
            ("Clear Memory", self.clear_memory),
            ("List Memory", self.list_memory),
            ("Exit", self.exit_program),
        ]

        for (text, command) in buttons:
            button = tk.Button(button_frame, text=text, command=command)
            button.pack(side=tk.LEFT, padx=5)

    def get_input(self):
        return self.input_field.get()

    def display_result(self, result):
        self.result_var.set(result)

    def add(self):
        inputs = self.get_input().split()
        if len(inputs) == 2:
            result = self.mini_computer.add(float(inputs[0]), float(inputs[1]))
            self.display_result(result)
        else:
            messagebox.showerror("Input Error", "Please provide two numbers.")

    def subtract(self):
        inputs = self.get_input().split()
        if len(inputs) == 2:
            result = self.mini_computer.subtract(float(inputs[0]), float(inputs[1]))
            self.display_result(result)
        else:
            messagebox.showerror("Input Error", "Please provide two numbers.")

    def multiply(self):
        inputs = self.get_input().split()
        if len(inputs) == 2:
            result = self.mini_computer.multiply(float(inputs[0]), float(inputs[1]))
            self.display_result(result)
        else:
            messagebox.showerror("Input Error", "Please provide two numbers.")

    def divide(self):
        inputs = self.get_input().split()
        if len(inputs) == 2:
            result = self.mini_computer.divide(float(inputs[0]), float(inputs[1]))
            self.display_result(result)
        else:
            messagebox.showerror("Input Error", "Please provide two numbers.")

    def store(self):
        inputs = self.get_input().split()
        if len(inputs) == 2:
            result = self.mini_computer.store(inputs[0], float(inputs[1]))
            self.display_result(result)
        else:
            messagebox.showerror("Input Error", "Please provide a name and a value.")

    def retrieve(self):
        name = self.get_input()
        result = self.mini_computer.retrieve(name)
        self.display_result(result)

    def clear_memory(self):
        result = self.mini_computer.clear_memory()
        self.display_result(result)

    def list_memory(self):
        result = self.mini_computer.list_memory()
        self.display_result(result)

    def exit_program(self):
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniComputerGUI(root)
    root.mainloop()
