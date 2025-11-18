#Evaluación 1
import tkinter as tk
from tkinter import Toplevel

def abrir_ventana_nombre():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Nombre")
    ventana_hija.geometry("250x150")
    
    etiqueta = tk.Label(ventana_hija,text="NOMBRE")
    etiqueta.pack(pady=10)

    boton_cerrar = tk.Button(ventana_hija,text="Cerrar", command = ventana_hija.destroy)
    boton_cerrar.pack(pady=10)
    
def abrir_ventana_carrera():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Carrera")
    ventana_hija.geometry("250x150")

    etiqueta = tk.Label(ventana_hija,text="CARRERA DEL ALUMNO", font=("Arial",12))
    etiqueta.pack(pady=10)

    boton_cerrar = tk.Button(ventana_hija,text="Cerrar", command = ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

def abrir_ventana_grupo():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Grupo")
    ventana_hija.geometry("250x150")

    etiqueta = tk.Label(ventana_hija,text="3A PROGRAMACION", font=("Arial",12))
    etiqueta.pack(pady=10)

    boton_cerrar = tk.Button(ventana_hija,text="Cerrar", command = ventana_hija.destroy)
    boton_cerrar.pack(pady=10)
    return

#crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

boton_nombre = tk.Button(ventana_principal,text="Nombre", command =  abrir_ventana_nombre)
boton_nombre.pack(pady=20)

boton_carrera = tk.Button(ventana_principal,text="Carrera", command =  abrir_ventana_carrera)
boton_carrera.pack(pady=20)

boton_grupo = tk.Button(ventana_principal,text="Grupo", command =  abrir_ventana_grupo)
boton_grupo.pack(pady=20)

ventana_principal.mainloop()  