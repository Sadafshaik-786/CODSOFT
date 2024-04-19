import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

contact = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contact[name] = (phone, email, address)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_fields()

def search_contact():
    search_name = search_entry.get()
    if search_name in contact:
        phone, email, address = contact[search_name]
        result_label.config(text="Phone: {}\nEmail: {}\nAddress: {}".format(phone, email, address))
    else:
        result_label.config(text="Name not found in contact book")

def display_contact():
    if not contact:
        result_label.config(text="Empty contact book")
    else:
        result_label.config(text="")
        for name, details in contact.items():
            phone, email, address = details
            result_label.config(text=result_label.cget("text") + "\nName: {}\nPhone: {}\nEmail: {}\nAddress: {}\n".format(name, phone, email, address))

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def edit_contact():
    edit_name = edit_entry.get()
    if edit_name in contact:
        phone, email, address = contact[edit_name]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.insert(0, edit_name)
        phone_entry.insert(0, phone)
        email_entry.insert(0, email)
        address_entry.insert(0, address)
    else:
        messagebox.showerror("Error", "Name not found in contact book")

# Create main window
root = tk.Tk()
root.title("Contact Book by SADAF")
root.geometry("500x550")
root.configure(background="#AC94F4")

# Labels
name_label = ttk.Label(root, text="Name:", background="#D4FAFA", foreground="black")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
phone_label = ttk.Label(root, text="Phone:", background="#D4FAFA", foreground="black")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
email_label = ttk.Label(root, text="Email:", background="#D4FAFA", foreground="black")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
address_label = ttk.Label(root, text="Address:", background="#D4FAFA", foreground="black")
address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
search_label = ttk.Label(root, text="Search Name:", background="#F6DAE4", foreground="black")
search_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
edit_label = ttk.Label(root, text="Edit Name:", background="#F6DAE4", foreground="black")
edit_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")

result_label = ttk.Label(root, text="", wraplength=350, justify="left",font="arial 10 bold", background="#fffec8", foreground="black")
result_label.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Entry Fields
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
phone_entry = ttk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
email_entry = ttk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
address_entry = ttk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
search_entry = ttk.Entry(root)
search_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
edit_entry = ttk.Entry(root)
edit_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")

# Buttons
add_button = ttk.Button(root, text="Add Contact", command=add_contact, style="TButton")
add_button.grid(row=4, column=0, padx=10, pady=5, sticky="w")
search_button = ttk.Button(root, text="Search Contact", command=search_contact, style="TButton")
search_button.grid(row=7, column=1, padx=10, pady=5, sticky="w")
display_button = ttk.Button(root, text="Display Contacts", command=display_contact, style="TButton")
display_button.grid(row=4, column=2, padx=10, pady=5, sticky="w")
clear_button = ttk.Button(root, text="Clear Fields", command=clear_fields, style="TButton")
clear_button.grid(row=4, column=1, padx=10, pady=5, sticky="w")
edit_button = ttk.Button(root, text="Edit Contact", command=edit_contact, style="TButton")
edit_button.grid(row=9, column=1, padx=10, pady=5, sticky="w")

style = ttk.Style()
style.configure("TButton", background="#4CAF50", foreground="white")

root.mainloop()
