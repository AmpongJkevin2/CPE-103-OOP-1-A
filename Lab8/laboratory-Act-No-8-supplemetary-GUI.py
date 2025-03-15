import math
import tkinter as tk

# Simple TUI Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Select operation (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input.")

if __name__ == " main ":
    main()

import tkinter as tk
from tkinter import ttk
import math

# --- Setup Main Window ---
root = tk.Tk()
root.title("Modern Dark Calculator")
root.geometry("500x500")
root.configure(bg="#2e2e2e")

# --- Configure Styles ---
style = ttk.Style(root)
style.theme_use("clam")  # Theme that allows customization
style.configure("TFrame", background="#506851")
style.configure("TLabel", background="#2e2e2e", foreground="#ffffff", font=("Helvetica", 10))
style.configure("TButton", background="#424242", foreground="#ffffff", font=("Helvetica", 10))
style.configure("TEntry", fieldbackground="#424242", foreground="#ffffff", font=("Helvetica", 10))

# --- Variables & History ---
result_var = tk.StringVar()
history_list = []

def get_validated(*values):
    """
    Converts provided string values to floats.
    Returns a list of floats if successful; otherwise,
    updates the result with an error message and returns None.
    """
    try:
        return [float(v) for v in values]
    except ValueError:
        result_var.set("Please enter numbers only!!")
        return None

def add_history(operation):
    history_list.append(operation)
    history_box.insert(tk.END, operation)

# --- Calculator Operations ---
def add():
    vals = get_validated(entry1.get(), entry2.get())
    if vals is None:
        return
    a, b = vals
    res = a + b
    result_var.set(res)
    add_history(f'{a} + {b} = {res}')

def subtract():
    vals = get_validated(entry1.get(), entry2.get())
    if vals is None:
        return
    a, b = vals
    res = a - b
    result_var.set(res)
    add_history(f'{a} - {b} = {res}')

def multiply():
    vals = get_validated(entry1.get(), entry2.get())
    if vals is None:
        return
    a, b = vals
    res = a * b
    result_var.set(res)
    add_history(f'{a} x {b} = {res}')

def divide():
    vals = get_validated(entry1.get(), entry2.get())
    if vals is None:
        return
    a, b = vals
    if b == 0:
        result_var.set("Error! Division by zero.")
        return
    res = a / b
    result_var.set(res)
    add_history(f'{a} ÷ {b} = {res}')

def square_root():
    vals = get_validated(entry3.get())
    if vals is None:
        return
    a = vals[0]
    try:
        res = math.sqrt(a)
    except ValueError:
        result_var.set("Invalid input for square root.")
        return
    result_var.set(res)
    add_history(f'sqrt({a}) = {res}')

def power():
    # Expects input in the format: base^exponent (e.g., "2^3")
    parts = entry3.get().split('^')
    if len(parts) != 2:
        result_var.set("Invalid format! Use base^exponent.")
        return
    vals = get_validated(parts[0], parts[1])
    if vals is None:
        return
    base, exponent = vals
    res = math.pow(base, exponent)
    result_var.set(res)
    add_history(f'{base} ^ {exponent} = {res}')

def trigonometric():
    # Expects input in the format: sin(angle), cos(angle) or tan(angle) where angle is in radians.
    s = entry3.get().strip()
    if s.startswith("sin(") and s.endswith(")"):
        inner = s[4:-1]
        vals = get_validated(inner)
        if vals is None:
            return
        angle = vals[0]
        res = math.sin(angle)
        result_var.set(res)
        add_history(f'sin({angle}) = {res}')
    elif s.startswith("cos(") and s.endswith(")"):
        inner = s[4:-1]
        vals = get_validated(inner)
        if vals is None:
            return
        angle = vals[0]
        res = math.cos(angle)
        result_var.set(res)
        add_history(f'cos({angle}) = {res}')
    elif s.startswith("tan(") and s.endswith(")"):
        inner = s[4:-1]
        vals = get_validated(inner)
        if vals is None:
            return
        angle = vals[0]
        res = math.tan(angle)
        result_var.set(res)
        add_history(f'tan({angle}) = {res}')
    else:
        result_var.set("Invalid input format!")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    result_var.set("")

# --- Layout Setup ---

# Main frame with padding
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Input frame for basic arithmetic
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=10)
ttk.Label(input_frame, text="Enter first number:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry1 = ttk.Entry(input_frame, width=15)
entry1.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(input_frame, text="Enter second number:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry2 = ttk.Entry(input_frame, width=15)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Button frame for arithmetic operations
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=10)
ttk.Button(button_frame, text="Add", command=add, width=10).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Subtract", command=subtract, width=10).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="Multiply", command=multiply, width=10).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(button_frame, text="Divide", command=divide, width=10).grid(row=0, column=3, padx=5, pady=5)

# Special Operations frame
special_frame = ttk.Frame(main_frame)
special_frame.pack(fill=tk.X, pady=10)
ttk.Label(special_frame, text="Enter number or expression:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entry3 = ttk.Entry(special_frame, width=25)
entry3.grid(row=0, column=1, padx=5, pady=5)

# Create a subframe for special operation buttons in one row
special_buttons_frame = ttk.Frame(special_frame)
special_buttons_frame.grid(row=1, column=0, columnspan=2, pady=5)
ttk.Button(special_buttons_frame, text="Sqrt", command=square_root, width=10).pack(side=tk.LEFT, padx=5)
ttk.Button(special_buttons_frame, text="Power", command=power, width=10).pack(side=tk.LEFT, padx=5)
ttk.Button(special_buttons_frame, text="Trigonometric", command=trigonometric, width=15).pack(side=tk.LEFT, padx=5)
ttk.Button(special_buttons_frame, text="Clear", command=clear, width=10).pack(side=tk.LEFT, padx=5)

# Result display frame
result_frame = ttk.Frame(main_frame)
result_frame.pack(fill=tk.X, pady=10)
ttk.Label(result_frame, text="Result:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
result_label = ttk.Label(result_frame, textvariable=result_var, font=("Helvetica", 14, "bold"))
result_label.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

# History display frame
history_frame = ttk.Frame(main_frame)
history_frame.pack(fill=tk.BOTH, pady=10, expand=True)
ttk.Label(history_frame, text="History:").pack(anchor=tk.W, padx=5, pady=5)
history_box = tk.Listbox(history_frame, height=8, bg="#424242", fg="#ffffff", font=("Helvetica", 10))
history_box.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)

root.mainloop()
