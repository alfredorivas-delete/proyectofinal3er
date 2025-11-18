import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

#Ejercicio 03
#Creado por NOMBRE 

#La sig linea obtiene donde están los archivos del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
figuras = {
    "Cuadrado": os.path.join(BASE_DIR,"cuadro.png"),
    "Rectángulo": os.path.join(BASE_DIR,"rectangulo.png"),
    "Círculo": os.path.join(BASE_DIR,"circulo.png"),
    "Tríangulo": os.path.join(BASE_DIR,"triangulo.png")
}

def mostrar_imagen(event):
    seleccion = lista_figuras.get(lista_figuras.curselection())
    ruta = figuras.get(seleccion)
    imagen = Image.open(ruta)
    imagen = imagen.resize((200,200))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.config(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    canvas.coords(id_label, -200, 150)
    deslizar_izq_dcha()

def deslizar_izq_dcha():
    x, y = canvas.coords(id_label)

    if x < 200:  # detener en el centro
        canvas.move(id_label, 10, 0)  # mover 10 píxeles por frame
        ventana.after(20, deslizar_izq_dcha)  # velocidad de animación
    else:
        # detener justo en el centro
        canvas.coords(id_label, 200, y)

ventana = tk.Tk()
ventana.title("Ejercicio 03: Imagenes")
ventana.geometry("400x400")

titulo = tk.Label(ventana,text="Selecciona una Figura", font=("Arial",14))
titulo.pack(pady=10)

lista_figuras = tk.Listbox(ventana, font=("Arial",12), height=4)
for figura in figuras.keys():
    lista_figuras.insert(tk.END,figura)
    lista_figuras.pack()

canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack()

etiqueta_imagen = tk.Label(canvas,bg="white",bd=0)
id_label = canvas.create_window(-200, 150, window=etiqueta_imagen) 


#La siguiente linea ejecuta la funcion al elegir
#una figura en la lista desplegable
lista_figuras.bind("<<ListboxSelect>>",mostrar_imagen)

ventana.mainloop()




    



