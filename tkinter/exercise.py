#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox


# Ventana principal
root = tk.Tk()
root.title("Menu() Widget")

def accion_menu():
    messagebox.showinfo("Menú", "Se ha tensao la cosa")


# Definición de la barra menu
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)   # Barra padre de la cual colgarán el resto de barras

menu1 = tk.Menu(barra_menu, tearoff=0) # Tearoff 0 es para evitar la fragmentación de las opciones del menú
barra_menu.add_cascade(label="Menú", menu=menu1)

menu1.add_command(label="Opción 1")
menu1.add_command(label="Opción 2")

menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Extras", menu=menu2)

menu2.add_command(label="Se tensa", command=accion_menu)

root.mainloop()
