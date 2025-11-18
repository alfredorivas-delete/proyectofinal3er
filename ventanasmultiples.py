#Ejemplo 16 Ventanas Multiples

import tkinter as tk
from tkinter import Toplevel

#crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana Hija")
    ventana_hija.geometry("250x150")

    etiqueta = tk.Label(ventana_hija,"Esta es una ventana hija",
                font=("Arial",12))
    etiqueta.pack(pady=10)

    boton_cerrar = tk.Button(ventana_hija,text="Cerrar",
                 command = ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

def abrir_boleta():
    ventana_boleta = Toplevel(ventana_principal)
    ventana_boleta.title("Boleta de Calificaciones")
    ventana_boleta.geometry("250x150")

    #Nombre del Alumno
    tk.Label(ventana_boleta, text="Nombre del Alumno").grid(row=0, column=0, sticky="w")
    entry_nombre = tk.Entry(ventana_boleta,width=40)
    entry_nombre.grid(row=0, column=1, columnspan=4, sticky="we")

    #Encabezados de la Tabla
    encabezados = ["Materia","Unidad1","Unidad2","Unidad3","Promedio"]
    for col, encabezado in enumerate(encabezados):
        tk.Label(ventana_boleta, text=encabezado, font=('Arial',10,'bold')).grid(row=1,column=col,padx=5,pady=5)

        filas = []   
        for i in range(3):
            fila = []
            # aqui va la Materia
            entry_materia = tk.Entry(ventana_boleta)
            entry_materia.grid(row=i+2, column=0, padx=5, pady=5)
            fila.append(entry_materia)

        #Calificaciones
        for j in range(1,4):
            entry_cal = tk.Entry(ventana_boleta,width=10)
            entry_cal.grid(row=i+2, column=j, padx=5)
            fila.append(entry_cal)
    
        label_promedio = tk.Label(ventana_boleta,text="0.00", width=10, bg="lightgray")
        label_promedio.grid(row=i+2, column=4, padx=5)
        fila.append(label_promedio)
        filas.append(fila)
        

boton_abrir = tk.Button(ventana_principal,text="Abrir Ventana", command =  abrir_ventana_hija)
boton_abrir.pack(pady=20)
ventana_principal.mainloop()  