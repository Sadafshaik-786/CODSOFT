import tkinter
from tkinter import *

root = Tk()
root.title("Simple Calculator by SADAF")
root.geometry('570x600+100+200')
root.resizable(False, False)
root.configure(bg='#17161b')

equation = ""
result = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation, result
    equation = ""
    result = ""
    label_result.config(text=result)

def calculate():
    global equation, result
    try:
        result = round(eval(equation),10)
    except:
        result = "Error"
        equation = ""
    label_result.config(text=result)

# Screen for display
label_result = Label(root, width=25, height=2, text="", font=("arial", 30), bg="#17161b", fg="#fff")
label_result.pack()

# Buttons
buttons = [
    ("C", 10, 100),
    ("/", 150, 100),
    ("%", 290, 100),
    ("*", 430, 100),
    ("7", 10, 200),
    ("8", 150, 200),
    ("9", 290, 200),
    ("-", 430, 200),
    ("4", 10, 300),
    ("5", 150, 300),
    ("6", 290, 300),
    ("+", 430, 300),
    ("1", 10, 400),
    ("2", 150, 400),
    ("3", 290, 400),
    ("0", 10, 500),
    (".", 290, 500),
    ("=", 430, 400),
]

for (text, x, y) in buttons:
    Button(root, text=text, width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#5A5A5A", command=lambda t=text: show(t)).place(x=x, y=y)

Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#FFA500", command=lambda: calculate()).place(x=430, y=400)
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#ff5555", command=clear).place(x=10, y=100)
Button(root, text="0", width=12, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#5A5A5A",command=lambda t="0": show(t)).place(x=10, y=500)
root.mainloop()