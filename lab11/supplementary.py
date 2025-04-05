import tkinter as tk
import math
from tkinter import messagebox

# --- Simple Elegant Theme Colors ---
BG_COLOR = "#F5F5F5"        # Off-white background (Whitesmoke)
WIDGET_BG = "#E0E0E0"       # Light gray for widgets (subtle contrast)
WIDGET_FG = "#333333"       # Dark gray text for readability
ACTIVE_BG = "#BDBDBD"       # Slightly darker gray for hover/press
ACTIVE_FG = "#111111"       # Slightly darker text on hover/press
ACCENT_BG = "#78909C"       # Muted Blue-Gray for operators/special buttons
ACCENT_FG = "#FFFFFF"       # White text on accent buttons
ACCENT_ACTIVE_BG = "#546E7A" # Darker Blue-Gray for accent hover/press
ENTRY_CURSOR = "#333333"    # Cursor color matches text
MENU_BG = WIDGET_BG
MENU_FG = WIDGET_FG
MENU_ACTIVE_BG = ACTIVE_BG
MENU_ACTIVE_FG = ACTIVE_FG
ERROR_BG = "#E57373"       # Muted Red for errors
ERROR_FG = "#FFFFFF"       # White text on error background

expression = ""

def set_display(text, is_error=False):
    global expression
    equation.set(text)
    if is_error:
        display_entry.config(bg=ERROR_BG, fg=ERROR_FG)
        expression = ""
    else:
        # Use WIDGET_BG for normal display background
        display_entry.config(bg=WIDGET_BG, fg=WIDGET_FG)
        if not text.startswith("Error"):
            expression = text

def press(num):
    if display_entry.cget('bg') == ERROR_BG:
        set_display(str(num))
    else:
        set_display(expression + str(num))

def equalpress():
    try:
        if not expression: return
        # WARNING: eval is a security risk. Use with caution.
        safe_expression = expression.replace('sin(','math.sin(math.radians(').replace('cos(','math.cos(math.radians(').replace('exp(','math.exp(')
        total = str(eval(safe_expression))
        set_display(total)
    except ZeroDivisionError:
        set_display("Error: Div by 0", is_error=True)
        messagebox.showerror("Calculation Error", "Cannot divide by zero.", parent=window) # Specify parent
    except Exception as e:
        set_display("Error", is_error=True)
        messagebox.showerror("Calculation Error", f"Invalid Input or Expression:\n{e}", parent=window) # Specify parent

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
        messagebox.showerror("Math Error", f"Please enter a valid number for {func_name}.", parent=window)
    except Exception as e:
        set_display("Error", is_error=True)
        messagebox.showerror("Math Error", f"Error during {func_name} calculation:\n{e}", parent=window)

# --- Main Window Setup ---
window = tk.Tk()
window.title("Elegant Calculator")
window.geometry("360x500") # Slightly adjusted size might look better
window.config(bg=BG_COLOR)
window.minsize(300, 450) # Optional: Set minimum size

# --- Grid Configuration ---
# 4 columns needed for standard layout + 1 for potential extra ops if added later
for i in range(4): window.columnconfigure(i, weight=1)
# Row weights - Adjust as needed, maybe give display more space?
window.rowconfigure(0, weight=2) # Display row
for i in range(1, 8): window.rowconfigure(i, weight=1) # Button rows

# --- Display Entry ---
equation = tk.StringVar()
display_entry = tk.Entry(window, textvariable=equation, font=('Segoe UI', 24), # Try Segoe UI or Arial
                         borderwidth=0, relief="flat", justify='right', # Flat look
                         bg=WIDGET_BG, fg=WIDGET_FG, insertbackground=ENTRY_CURSOR)
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(15, 10), sticky="nsew")
set_display("")

# --- Menu Bar ---
menubar = tk.Menu(window, bg=BG_COLOR, relief='flat', borderwidth=0) # Match window bg
filemenu = tk.Menu(menubar, tearoff=0, bg=MENU_BG, fg=MENU_FG,
                   activebackground=MENU_ACTIVE_BG, activeforeground=MENU_ACTIVE_FG,
                   relief='flat', borderwidth=0)
filemenu.add_command(label="Clear", command=clear)
# filemenu.add_separator(background=BG_COLOR) # Separator might look odd with flat style
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Options", menu=filemenu, underline=0)
window.config(menu=menubar)

# --- Button Styling Dictionaries ---
base_button_opts = {
    'font': ('Segoe UI', 14), # Consistent font
    'relief': 'flat',         # Use flat design
    'borderwidth': 0,         # No border for flat
    'activeforeground': ACTIVE_FG,
    'activebackground': ACTIVE_BG,
    'padx': 5, 'pady': 10      # Adjust padding for visual spacing
}

# Normal number/dot buttons
num_button_opts = base_button_opts.copy()
num_button_opts['bg'] = WIDGET_BG
num_button_opts['fg'] = WIDGET_FG

# Operator/Function/Clear/Equals buttons (Accent Color)
accent_button_opts = base_button_opts.copy()
accent_button_opts['bg'] = ACCENT_BG
accent_button_opts['fg'] = ACCENT_FG
accent_button_opts['activebackground'] = ACCENT_ACTIVE_BG

# --- Button Layout Definition (4 columns layout) ---
# (text, row, col, columnspan, command_type, command_arg, style_opts)
button_layout = [
    ('sin', 1, 0, 1, 'func', 'sin', accent_button_opts), # Row 1
    ('cos', 1, 1, 1, 'func', 'cos', accent_button_opts),
    ('exp', 1, 2, 1, 'func', 'exp', accent_button_opts),
    ('C',   1, 3, 1, 'clear', clear, accent_button_opts),

    ('7',   2, 0, 1, 'press', '7', num_button_opts),    # Row 2
    ('8',   2, 1, 1, 'press', '8', num_button_opts),
    ('9',   2, 2, 1, 'press', '9', num_button_opts),
    ('/',   2, 3, 1, 'press', '/', accent_button_opts),

    ('4',   3, 0, 1, 'press', '4', num_button_opts),    # Row 3
    ('5',   3, 1, 1, 'press', '5', num_button_opts),
    ('6',   3, 2, 1, 'press', '6', num_button_opts),
    ('*',   3, 3, 1, 'press', '*', accent_button_opts),

    ('1',   4, 0, 1, 'press', '1', num_button_opts),    # Row 4
    ('2',   4, 1, 1, 'press', '2', num_button_opts),
    ('3',   4, 2, 1, 'press', '3', num_button_opts),
    ('-',   4, 3, 1, 'press', '-', accent_button_opts),

    ('0',   5, 0, 2, 'press', '0', num_button_opts),    # Row 5 (0 spans 2 cols)
    ('.',   5, 2, 1, 'press', '.', num_button_opts),
    ('+',   5, 3, 1, 'press', '+', accent_button_opts),

    ('=',   6, 0, 4, 'equal', equalpress, accent_button_opts) # Row 6 (= spans 4 cols)
]

grid_sticky = "nsew"
grid_padx = 3 # Slightly reduced padding between buttons
grid_pady = 3

# --- Create Buttons in a Loop ---
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
        # Create button with its specific style options
        btn = tk.Button(window, text=text, command=command, **style)
        # Apply grid layout separately
        btn.grid(row=r, column=c, columnspan=cspan,
                 padx=grid_padx, pady=grid_pady, sticky=grid_sticky)

# Add some padding at the bottom of the window
window.rowconfigure(7, weight=1) # Add an empty row for padding

# --- Start Tkinter event loop ---
window.mainloop()