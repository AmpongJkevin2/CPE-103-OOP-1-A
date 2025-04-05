import tkinter as tk
import math
from tkinter import messagebox

BG_COLOR = "#2E2E2E"
FG_COLOR = "#CCCCCC"
WIDGET_BG = "#404040"
WIDGET_FG = "#FFFFFF"
ACTIVE_BG = "#555555"
ACTIVE_FG = "#FFFFFF"
ENTRY_CURSOR = "#FFFFFF"
MENU_ACTIVE_BG = "#555555"
MENU_ACTIVE_FG = "#FFFFFF"
ERROR_BG = "#5B0000"

expression = ""

def set_display(text, is_error=False):
    global expression
    equation.set(text)
    bg_color = ERROR_BG if is_error else WIDGET_BG
    display_entry.config(bg=bg_color, fg=WIDGET_FG)
    if is_error:
        expression = ""
    elif not text.startswith("Error"):
        expression = text

def press(num):
    if display_entry.cget('bg') == ERROR_BG:
        set_display(str(num))
    else:
        set_display(expression + str(num))

def equalpress():
    try:
        if not expression: return
        # WARNING: eval is a security risk if input is not controlled.
        # Basic replacement for direct function calls - not a robust parser.
        safe_expression = expression.replace('sin(','math.sin(math.radians(').replace('cos(','math.cos(math.radians(').replace('exp(','math.exp(')
        total = str(eval(safe_expression))
        set_display(total)
    except ZeroDivisionError:
        set_display("Error: Div by 0", is_error=True)
        messagebox.showerror("Calculation Error", "Cannot divide by zero.")
    except Exception as e:
        set_display("Error", is_error=True)
        messagebox.showerror("Calculation Error", f"Invalid Input or Expression:\n{e}")

def clear():
    set_display("")

def calculate_math_func(func_name):
    try:
        if not expression: return
        value = float(expression)
        result = 0
        if func_name == 'sin':
            result = math.sin(math.radians(value))
        elif func_name == 'cos':
            result = math.cos(math.radians(value))
        elif func_name == 'exp':
            result = math.exp(value)
        set_display(str(result))
    except ValueError:
        set_display("Error: Invalid Input", is_error=True)
        messagebox.showerror("Math Error", f"Please enter a valid number for {func_name}.")
    except Exception as e:
        set_display("Error", is_error=True)
        messagebox.showerror("Math Error", f"Error during {func_name} calculation:\n{e}")

window = tk.Tk()
window.title("Simple Dark Calculator")
window.geometry("400x550")
window.config(bg=BG_COLOR)

for i in range(5): window.columnconfigure(i, weight=1)
for i in range(8): window.rowconfigure(i, weight=1)

equation = tk.StringVar()
display_entry = tk.Entry(window, textvariable=equation, font=('Arial', 24),
                         borderwidth=2, relief="sunken", justify='right',
                         bg=WIDGET_BG, fg=WIDGET_FG, insertbackground=ENTRY_CURSOR)
display_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
set_display("")

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0, bg=WIDGET_BG, fg=FG_COLOR,
                   activebackground=MENU_ACTIVE_BG, activeforeground=MENU_ACTIVE_FG)
filemenu.add_command(label="Clear", command=clear)
filemenu.add_separator(background=BG_COLOR)
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Options", menu=filemenu)
window.config(menu=menubar)

# Style options (excluding grid-specific 'sticky')
button_opts = {
    'font': ('Arial', 14), 'padx': 5, 'pady': 5,
    'bg': WIDGET_BG, 'fg': WIDGET_FG, 'activebackground': ACTIVE_BG,
    'activeforeground': ACTIVE_FG, 'relief': 'raised', 'borderwidth': 1
}
op_func_opts = button_opts.copy()
# op_func_opts['bg'] = "#505050" # Example variation
clear_opts = button_opts.copy()
clear_opts['bg'] = "#8B0000"; clear_opts['activebackground'] = "#A52A2A"
eq_opts = button_opts.copy()
eq_opts['bg'] = "#006400"; eq_opts['activebackground'] = "#008000"

button_layout = [
    ('sin', 1, 0, 1, 'func', 'sin', op_func_opts),
    ('cos', 1, 1, 1, 'func', 'cos', op_func_opts),
    ('exp', 1, 2, 1, 'func', 'exp', op_func_opts),
    ('C',   2, 0, 5, 'clear', clear, clear_opts),
    ('7',   3, 0, 1, 'press', '7', button_opts),
    ('8',   3, 1, 1, 'press', '8', button_opts),
    ('9',   3, 2, 1, 'press', '9', button_opts),
    ('/',   3, 3, 1, 'press', '/', op_func_opts),
    ('4',   4, 0, 1, 'press', '4', button_opts),
    ('5',   4, 1, 1, 'press', '5', button_opts),
    ('6',   4, 2, 1, 'press', '6', button_opts),
    ('*',   4, 3, 1, 'press', '*', op_func_opts),
    ('1',   5, 0, 1, 'press', '1', button_opts),
    ('2',   5, 1, 1, 'press', '2', button_opts),
    ('3',   5, 2, 1, 'press', '3', button_opts),
    ('-',   5, 3, 1, 'press', '-', op_func_opts),
    ('0',   6, 0, 2, 'press', '0', button_opts),
    ('.',   6, 2, 1, 'press', '.', button_opts),
    ('+',   6, 3, 1, 'press', '+', op_func_opts),
    ('=',   7, 0, 5, 'equal', equalpress, eq_opts)
]

# Grid sticky setting used for all buttons
grid_sticky = "nsew"

for config in button_layout:
    text, r, c, cspan, cmd_type, cmd_arg, style = config

    command = None
    if cmd_type == 'press':
        command = lambda arg=cmd_arg: press(arg)
    elif cmd_type == 'func':
        command = lambda arg=cmd_arg: calculate_math_func(arg)
    elif cmd_type in ['clear', 'equal']:
        command = cmd_arg

    if command:
        # Pass only valid Button options using **style
        btn = tk.Button(window, text=text, command=command, **style)
        # Apply grid options separately
        btn.grid(row=r, column=c, columnspan=cspan, padx=5, pady=5, sticky=grid_sticky)

window.mainloop()