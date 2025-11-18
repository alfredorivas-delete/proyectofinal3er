#Evaluacion 2 B

import tkinter as tk
from tkinter import Toplevel

def abrir_ventana_nombre():
    ventana_hija = Toplevel(ventana_principal)
    etiqueta = tk.Label(ventana_hija, text="Nombre")
    etiqueta.pack(padx=20)
    nombre = tk.Entry(ventana_hija)
    nombre.pack(pady=5)

    etiqueta2 = tk.Label(ventana_hija, text="Apellido")
    etiqueta2.pack(padx=20)
    apellido = tk.Entry(ventana_hija)
    apellido.pack(pady=5)

def abrir_ventana_usuario():
    ventana_hija = Toplevel(ventana_principal)
    etiqueta = tk.Label(ventana_hija, text="Usuario")
    etiqueta.pack(padx=20)
    usuario = tk.Entry(ventana_hija)
    usuario.pack(pady=5)

    etiqueta2 = tk.Label(ventana_hija, text="Password")
    etiqueta2.pack(padx=20)
    password = tk.Entry(ventana_hija)
    password.pack(pady=5)

#crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

boton_nombre = tk.Button(ventana_principal,text="Nombre", command =  abrir_ventana_nombre)
boton_nombre.pack(pady=20)

boton_grupo = tk.Button(ventana_principal,text="Usuario", command =  abrir_ventana_usuario)
boton_grupo.pack(pady=20)

ventana_principal.mainloop()  