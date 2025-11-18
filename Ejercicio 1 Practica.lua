#Ejercicio 1

import tkinter as tk
from tkinter import Toplevel

ventana = tk.Tk()
ventana.title("Ejercicio 1")

def abrir_ventana():
    ventana_productos = Toplevel(ventana)
    etiquetanombre = tk.Label(text="Producto:")
    etiquetanombre.pack(pady=5)
    nombre = tk.Entry()
    nombre.pack()

    etiquetacant = tk.Label(text="Cantidad:")
    etiquetacant.pack(pady=5)
    cantidad = tk.Entry()
    cantidad.pack()

    etiquetaprecio = tk.Label(text="Precio")
    etiquetaprecio.pack(pady=5)
    precio = tk.Entry()
    precio.pack()

botonmostrar = tk.Button(ventana,text="Mostrar Ventana", command = abrir_ventana)
botonmostrar.pack()
ventana.mainloop()




