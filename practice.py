import tkinter as tk
from tkinter import ttk
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PASSWORD GENERATOR by SADAF")

        self.letters = ['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        self.symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','.']

        self.len_var = tk.StringVar()
        self.n_symbols_var = tk.StringVar()
        self.n_numbers_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Configure style for labels and buttons
        style = ttk.Style()
        style.configure('TLabel', foreground='white', background='#17161b', font=("Helvetica", 12))
        style.configure('TButton', foreground='white', background='#007bff', font=("Helvetica", 12))

        # Title Label
        ttk.Label(self.root, text="WELCOME TO PASSWORD GENERATOR", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # Length Entry
        ttk.Label(self.root, text="Length of the Password:", style='TLabel').grid(row=1, column=0, padx=5, pady=5)
        self.len_entry = ttk.Entry(self.root, textvariable=self.len_var)
        self.len_entry.grid(row=1, column=1, padx=5, pady=5)

        # Complexity Label
        ttk.Label(self.root, text="SET THE COMPLEXITY:", style='TLabel').grid(row=2, column=0, columnspan=2, pady=5)

        # Number of Symbols Entry
        ttk.Label(self.root, text="Number of Symbols in your password:", style='TLabel').grid(row=3, column=0, padx=5, pady=5)
        self.n_symbols_entry = ttk.Entry(self.root, textvariable=self.n_symbols_var)
        self.n_symbols_entry.grid(row=3, column=1, padx=5, pady=5)

        # Number of Numbers Entry
        ttk.Label(self.root, text="Number of Numbers in your password:", style='TLabel').grid(row=4, column=0, padx=5, pady=5)
        self.n_numbers_entry = ttk.Entry(self.root, textvariable=self.n_numbers_var)
        self.n_numbers_entry.grid(row=4, column=1, padx=5, pady=5)

        # Generate Button
        ttk.Button(self.root, text="Generate Password", command=self.generate_password, style='TButton').grid(row=5, column=0, columnspan=2, pady=10)

        # Password Display Label
        ttk.Label(self.root, text="Generated Password:", style='TLabel').grid(row=6, column=0, padx=5, pady=5)
        self.password_label = ttk.Label(self.root, textvariable=self.password_var, font=("Courier", 12), style='TLabel')
        self.password_label.grid(row=6, column=1, padx=5, pady=5)

        # Password Message Label
        self.password_message_var = tk.StringVar()
        self.password_message_label = ttk.Label(self.root, textvariable=self.password_message_var, font=("Helvetica", 10), wraplength=300, style='TLabel')
        self.password_message_label.grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = int(self.len_var.get())
        n_symbols = int(self.n_symbols_var.get())
        n_numbers = int(self.n_numbers_var.get())

        n_letters = length - (n_symbols + n_numbers)
        password_list = []

        for _ in range(n_letters):
            char = random.choice(self.letters)
            password_list.append(char)

        for _ in range(n_symbols):
            char = random.choice(self.symbols)
            password_list.append(char)

        for _ in range(n_numbers):
            char = random.choice(self.numbers)
            password_list.append(char)

        random.shuffle(password_list)
        password = ''.join(password_list)
        self.password_var.set(password)

        self.password_message_var.set(f"Successfully generated a password with {n_letters} letters, {n_numbers} numbers, {n_symbols} symbols.")

def main():
    root = tk.Tk()
    root.title("PASSWORD GENERATOR by SADAF")
    root.geometry('490x400+100+200')
    root.resizable(False, False)
    root.configure(bg='#17161b')
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
