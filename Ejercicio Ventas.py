#Ejercicio 05
#Ventas de Productos

import tkinter as tk
from tkinter import messagebox

def calcular_ventas():    
    promedio_final = 0
    for i in range(len(filas)):
        try:
            costo = float(filas[i][1].get())
            precio = float(filas[i][2].get())
            cantidad = float(filas[i][3].get())
            venta  = (precio * cantidad)
            venta_final = venta
            filas[i][4].config(text=f"{venta_final:.2f}")            
        except ValueError:
            messagebox.showerror("Error",f"Ventas Inválidas")    
#La ventana principal
ventana = tk.Tk()
ventana.title("Venta de Productos")

#Nombre del Alumno
tk.Label(ventana, text="Nombre del Cliente").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana,width=40)
entry_nombre.grid(row=0, column=1, columnspan=4, sticky="we")

#Encabezados de la Tabla
encabezados = ["Producto","Costo","Precio","Cantidad","Total"]
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

    #Ventas
    for j in range(1,4):
        entry_cal = tk.Entry(ventana,width=10)
        entry_cal.grid(row=i+2, column=j, padx=5)
        fila.append(entry_cal)
    
    label_venta = tk.Label(ventana,text="0.00", width=10, bg="lightgray")
    label_venta.grid(row=i+2, column=4, padx=5)
    fila.append(label_venta)
    filas.append(fila)
        
    #Promedio
    btn_calcular = tk.Button(ventana,text="Calcular", command=calcular_ventas)
    btn_calcular.grid(row=7,column=0,columnspan=5,pady=10)
ventana.mainloop()

