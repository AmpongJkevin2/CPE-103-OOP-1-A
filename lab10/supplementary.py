import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
window.configure(background="light gray")


ttk.Label(window, text="Choose your birth month",
          background='black', foreground="wheat",
          font=("Times New Roman", 20, 'bold')).pack(pady=20)

container1 = ttk.Frame(window)
# label text for title

# Set label
ttk.Label(container1, text="Select the day of your birth :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=0, padx=5)

ttk.Label(container1, text="Select the month of your birth :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=1, padx=5)

ttk.Label(container1, text="Select the year of your birth :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=2, padx=5)
# Create Combobox
day_val = tk.StringVar()
mont_val = tk.StringVar()
year_val = tk.StringVar()

day = ttk.Combobox(container1, width=27, textvariable=day_val)
month = ttk.Combobox(container1, width=27, textvariable=mont_val)
year = ttk.Combobox(container1, width=27, textvariable=year_val)

# Adding combobox drop down list

day['values'] = [[i] for i in range(1,32)]

month['values'] = (' January',
                     ' February',
                     ' March',
                     ' April',
                     ' May',
                     ' June',
                     ' July',
                     ' August',
                     'September',
                     'October',
                     'November',
                     'December')

year['values'] = [[i] for i in range(1990, 2026)]

day.grid(column=1, row=0)
month.grid(column=1, row=1, pady=25)
year.grid(column=1, row=2)
day.current()
month.current()
year.current()
container1.pack()


def get_info():
    if day_val.get() and mont_val.get() and year_val.get():
        showinfo(
            title = "Selection",
            message = f'You selected {mont_val.get()} {day_val.get()}, {year_val.get()}')
    else:
        showinfo(
            title="Warning",
            message=f'Please fill all the field.')


ttk.Button(window, text='View', command=get_info).pack(side = 'right', padx=50)


window.mainloop()