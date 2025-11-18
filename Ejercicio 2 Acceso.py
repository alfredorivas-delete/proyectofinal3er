#Ejercicio 2
# Creado por NOMBRE

import tkinter as tk
from tkinter import messagebox
from tkinter import font

#Aqui se crean las funciones
def verificar_password():
    password = entrada_password.get()
    if password == "admin123":
        messagebox.showinfo("Resultado","Acceso OK")
    else:
        messagebox.showwarning("Resultado","Incorrecto")

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificador de Contraseña")
ventana.geometry("300x150")
ventana.configure(bg="#f0f4f8")

#Fuente personalizada
fuente_titulo = font.Font(family="Helvetica", size=14,
                          weight="bold")
fuente_normal = font.Font(family="Helvetica", size = 10)

#Marco Centrado
marco = tk.Frame(ventana, bg="#ffffff", bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")

etiqueta = tk.Label(marco, text="Ingrese la Clave",
                    font = fuente_titulo, bg="#ffffff")
etiqueta.pack(padx=20, pady=(15,5))

entrada_password = tk.Entry(marco, show="*",
                            font=fuente_normal,width=25,
                            bd=2, relief="solid")
entrada_password.pack(pady=5, padx=20)

boton_verificar = tk.Button(marco, 
                text="Verificar",
                command=verificar_password,
                bg="#4CAF50",fg="white", 
                font=fuente_normal,
                padx=10, pady=5, 
                activebackground="#45a049",
                relief="flat")

boton_verificar.pack(pady=(10,15))

#Ejecuta la ventana
ventana.mainloop()
