#Proyecto final 
#Submodulo
#Autores: Rivas Lerma Alfredo Nicolas y Orono Hernandez Diego

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# FUNCIONES
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("POS Sneaker's Club")
ventana.geometry("500x650")
ventana.resizable(True, True)
ventana.configure(bg="white")

# CANVAS efecto goteado
canvas = tk.Canvas(ventana, highlightthickness=0, bg="white")
canvas.place(relwidth=1, relheight=1)

# Bloque rojo superior
canvas.create_rectangle(0, 0, 500, 260, fill="#f30b0b", outline="")

# GOTEO MÁS MARCADO (chorreado fuerte)
goteos = [
    (-80, 190, 120, 360),
    (100, 210, 260, 420),
    (240, 160, 450, 340),
    (350, 200, 700, 420),
    (20, 240, 140, 470),
    (180, 250, 300, 520),
]

for x1, y1, x2, y2 in goteos:
    canvas.create_oval(x1, y1, x2, y2, fill="#f30b0b", outline="")

# GOTAS pequeñas sueltas
gotas = [
    (90, 360, 120, 410),
    (150, 420, 180, 460),
    (310, 350, 340, 390),
    (260, 480, 290, 520),
]

for x1, y1, x2, y2 in gotas:
    canvas.create_oval(x1, y1, x2, y2, fill="#f30b0b", outline="")

# LOGO
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "ventas2025.png"))
    imagen = imagen.resize((200, 200))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo, bg="#f30b0b")
    lbl_logo.place(relx=0.5, y=160, anchor="center")
except:
    lbl_sin_logo = tk.Label(ventana, text="(Aquí va el logo)", font=("Arial", 14), bg="#f30b0b", fg="white")
    lbl_sin_logo.place(relx=0.5, y=160, anchor="center")

# ====== ESTILO DE BOTONES (Borde negro grueso + mismo tamaño) ======

estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Rojo.TButton",
    font=("Arial", 12),
    foreground="red",
    background="white",
    bordercolor="black",   # borde negro
    borderwidth=3,         # borde grueso
    padding=10
)

estilo.map(
    "Rojo.TButton",
    background=[("active", "#ffe5e5")],
    bordercolor=[("active", "black")],
    foreground=[("active", "red")]
)

# Frame para controlar tamaño fijo
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.place(relx=0.5, y=360, anchor="n")

ANCHO_BOTON = 25  # <-- todos iguales

btn_reg_prod = ttk.Button(frame_botones, text="Registro de Productos",
                          style="Rojo.TButton", width=ANCHO_BOTON,
                          command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(frame_botones, text="Registro de Ventas",
                            style="Rojo.TButton", width=ANCHO_BOTON,
                            command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(frame_botones, text="Reportes",
                          style="Rojo.TButton", width=ANCHO_BOTON,
                          command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(frame_botones, text="Acerca de",
                        style="Rojo.TButton", width=ANCHO_BOTON,
                        command=abrir_acerca_de)
btn_acerca.pack(pady=10)

ventana.mainloop()