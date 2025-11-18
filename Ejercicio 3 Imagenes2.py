import tkinter as tk
import os

from tkinter import ttk
from PIL import Image, ImageTk

# Ruta base del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Diccionario de figuras con rutas de imagen
# Diccionario con rutas completas
figuras = {
    "Cuadrado": os.path.join(BASE_DIR, "cuadro.png"),
    "Rectángulo": os.path.join(BASE_DIR, "rectangulo.png"),
    "Círculo": os.path.join(BASE_DIR, "circulo.png"),
    "Triángulo": os.path.join(BASE_DIR, "triangulo.png")
}

def mostrar_imagen(event):
    # Obtener selección
    if not lista_figuras.curselection():
        return
    seleccion = lista_figuras.get(lista_figuras.curselection())
    ruta = figuras.get(seleccion)

    # Borrar imagen anterior (si existe)
    etiqueta_imagen.config(image="")
    etiqueta_imagen.image = None
    
    # Cargar y redimensionar imagen
    imagen = Image.open(ruta)
    imagen = imagen.resize((200, 200))
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un canvas temporal para animación
    canvas = tk.Canvas(ventana, width=200, height=200, bg="white", highlightthickness=0)
    canvas.place(relx=0.5, rely=1.2, anchor="center")  # comienza abajo
       
    # Crear la imagen en el canvas
    imagen_id = canvas.create_image(100, 200, image=imagen_tk)
    canvas.imagen_ref = imagen_tk  # evitar que se borre la referencia

    # Animación: de abajo hacia arriba
    def animar(y_actual):
        if y_actual > 100:  # posición final
            canvas.move(imagen_id, 0, -5)
            ventana.after(15, lambda: animar(y_actual - 5))
        else:
            # Cuando termina la animación, mostrarla fija en la etiqueta
            etiqueta_imagen.config(image=imagen_tk)
            etiqueta_imagen.image = imagen_tk
            canvas.destroy()  # quitar el canvas animado

    animar(300)  # posición inicial (correcta indentación)


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Visualizador de Figuras")
ventana.geometry("400x400")

# Título
titulo = tk.Label(ventana, text="Selecciona una figura:", font=("Arial", 14))
titulo.pack(pady=10)

# Listbox de figuras
lista_figuras = tk.Listbox(ventana, font=("Arial", 12), height=4)
for figura in figuras.keys():
   lista_figuras.insert(tk.END, figura)
   lista_figuras.pack()

# Imagen mostrada
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=20)

# Evento al seleccionar
lista_figuras.bind("<<ListboxSelect>>", mostrar_imagen)

# Ejecutar
ventana.mainloop()