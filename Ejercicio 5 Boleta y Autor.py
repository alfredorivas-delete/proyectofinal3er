#Ejercicio 5

import tkinter as tk
from tkinter import Toplevel

#crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ejercicio 5")
ventana_principal.geometry("300x200")

def ventana_autor():
    ventana_autor = Toplevel(ventana_principal)
    ventana_autor.title("Autor del Proyecto")
    ventana_autor.geometry("250x150")

    etiqueta = tk.Label(ventana_autor,text="Creado por: NOMBREALUMNO", font=("Arial",12))
    etiqueta.pack(pady=10)

    boton_cerrar = tk.Button(ventana_autor,text="Cerrar", command = ventana_autor.destroy)
    boton_cerrar.pack(pady=10)

def ventana_boleta():
    #La ventana principal
    ventana_boleta = Toplevel(ventana_principal)
    ventana_boleta.title("Boleta de Calificaciones")

    #Nombre del Alumno
    tk.Label(ventana_boleta, text="Nombre del Alumno").grid(row=0, column=0, sticky="w")
    entry_nombre = tk.Entry(ventana_boleta,width=40)
    entry_nombre.grid(row=0, column=1, columnspan=4, sticky="we")

    #Encabezados de la Tabla
    encabezados = ["Materia","Unidad1","Unidad2","Unidad3","Promedio"]
    for col, encabezado in enumerate(encabezados):
        tk.Label(ventana_boleta, text=encabezado, 
             font=('Arial',10,'bold')).grid(row=1,column=col,padx=5,pady=5)

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
        
boton_abrir = tk.Button(ventana_principal,text="Autor", command =  ventana_autor)
boton_abrir.pack(pady=20)

boton_boleta = tk.Button(ventana_principal,text="Boleta", command =  ventana_boleta)
boton_boleta.pack(pady=20)

ventana_principal.mainloop()  




