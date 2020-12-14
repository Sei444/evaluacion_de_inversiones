import tkinter as tk
from tkinter import ttk


año = 2020

inv = tk.Tk()
inv.title("Mi ventana")
inv.minsize(500, 250)



tk.Label(inv,text="").grid(row=0,column=0)
tk.Label(inv,text="").grid(row=1,column=1)  

entries = [] 
for i in range(2015, año + 1):
    a = i - 2015
    a = a + 3
    (tk.Label(inv, text="Selecione la tasa de inflación porcentual para el año ")
        .grid(row=a,column=1)
        )
    tk.Label(inv, text = i).grid(row=a, column=2)
    txt = tk.Entry(inv, width=7)
    txt.grid(column=3, row=a)
    entries.append(txt)


def get_entries(entries):
    for entry in entries:
        print(entry.get())

but = ttk.Button(inv,
                 text="Guardar tasas de interés ",
                 command=lambda: get_entries(entries)
                 )
but.grid(column=4, row=a + 1)

inv.mainloop() 