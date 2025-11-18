#Ejercicio 1

import tkinter as tk
from tkinter import Toplevel

ventana = tk.Tk()
ventana.title("Ejercicio 1")

def abrir_ventana():
    ventana_productos = Toplevel(ventana)
    etiquetanombre = tk.Label(ventana_productos,text="Producto:")
    etiquetanombre.pack(pady=5)
    nombre = tk.Entry(ventana_productos)
    nombre.pack()

    etiquetacant = tk.Label(ventana_productos, text="Cantidad:")
    etiquetacant.pack(pady=5)
    cantidad = tk.Entry(ventana_productos)
    cantidad.pack()

    etiquetaprecio = tk.Label(ventana_productos, text="Precio")
    etiquetaprecio.pack(pady=5)
    precio = tk.Entry(ventana_productos)
    precio.pack()

botonmostrar = tk.Button(ventana,text="Mostrar Ventana", command = abrir_ventana)
botonmostrar.pack()
ventana.mainloop()




