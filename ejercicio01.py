#Ejercicio 01
#Creado por: NOMBRE ALUMNO
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 1: Sumar")
ventana.geometry("350x230")

entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2.pack(pady=5)

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        suma = num1 + num2
        resultado.config(text=f"Resultado: {suma}")
    except ValueError:
        resultado.config(text="Escriba solo números")

boton_sumar = tk.Button(ventana,text="Sumar",command=sumar)
boton_sumar.pack(pady=5)

resultado = tk.Label(ventana,text="Resultado: ")
resultado.pack(pady=10)
ventana.mainloop()

