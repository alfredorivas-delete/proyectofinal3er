#Ejercicio 04
#Boleta de Calificaciones

import tkinter as tk
from tkinter import messagebox

def calcular_promedios():    
    promedio_final = 0
    for i in range(len(filas)):
        try:
            cal1 = float(filas[i][1].get())
            cal2 = float(filas[i][2].get())
            cal3 = float(filas[i][3].get())
            promedio = (cal1 + cal2 + cal3) / 3
            promedio_final = promedio_final + promedio
            filas[i][4].config(text=f"{promedio:.2f}")            
        except ValueError:
            messagebox.showerror("Error",f"Calificaciones Inválidas")
    promedio_final = promedio_final / 3
    messagebox.showinfo("Promedio",f"El promedio final es de: {promedio_final}")
#La ventana principal
ventana = tk.Tk()
ventana.title("Boleta de Calificaciones")

#Nombre del Alumno
tk.Label(ventana, text="Nombre del Alumno").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana,width=40)
entry_nombre.grid(row=0, column=1, columnspan=4, sticky="we")

#Encabezados de la Tabla
encabezados = ["Materia","Unidad1","Unidad2","Unidad3","Promedio"]
for col, encabezado in enumerate(encabezados):
    tk.Label(ventana, text=encabezado, 
             font=('Arial',10,'bold')).grid(row=1,column=col,padx=5,pady=5)

filas = []   
for i in range(3):
    fila = []
    # aqui va la Materia
    entry_materia = tk.Entry(ventana)
    entry_materia.grid(row=i+2, column=0, padx=5, pady=5)
    fila.append(entry_materia)

    #Calificaciones
    for j in range(1,4):
        entry_cal = tk.Entry(ventana,width=10)
        entry_cal.grid(row=i+2, column=j, padx=5)
        fila.append(entry_cal)
    
    label_promedio = tk.Label(ventana,text="0.00", width=10, bg="lightgray")
    label_promedio.grid(row=i+2, column=4, padx=5)
    fila.append(label_promedio)
    filas.append(fila)
        
    #Promedio
    btn_calcular = tk.Button(ventana,text="Calcular", command=calcular_promedios)
    btn_calcular.grid(row=7,column=0,columnspan=5,pady=10)
ventana.mainloop()

