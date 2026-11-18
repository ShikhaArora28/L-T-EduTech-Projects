"""Simple Calculator: our first complete Tkinter app (Unit V, Day 1)."""
import tkinter as tk
from tkinter import messagebox


def calc(op):
    """Read both boxes, do the maths for op, and show the result."""
    try:
        a = float(first.get())
        b = float(second.get())
    except ValueError:
        messagebox.showerror("Oops", "Please type numbers only")
        return

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    elif op == "*":
        answer = a * b
    elif b == 0:
        messagebox.showerror("Oops", "Cannot divide by zero")
        return
    else:
        answer = a / b

    result.config(text=f"Result: {answer:g}")


root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="First number").grid(row=0, column=0, padx=8, pady=6)
first = tk.Entry(root, width=15)
first.grid(row=0, column=1, columnspan=3, padx=8)

tk.Label(root, text="Second number").grid(row=1, column=0, padx=8, pady=6)
second = tk.Entry(root, width=15)
second.grid(row=1, column=1, columnspan=3, padx=8)

plus = tk.Button(root, text="+", width=5, command=lambda: calc("+"))
plus.grid(row=2, column=0, pady=8)
minus = tk.Button(root, text="-", width=5, command=lambda: calc("-"))
minus.grid(row=2, column=1)
times = tk.Button(root, text="×", width=5, command=lambda: calc("*"))
times.grid(row=2, column=2)
divide = tk.Button(root, text="÷", width=5, command=lambda: calc("/"))
divide.grid(row=2, column=3)

result = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"))
result.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()