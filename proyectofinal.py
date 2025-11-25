#Proyecto final 
#Submodulo
#Autores: Rivas Lerma Alfredo Nicolas y Orono Hernandez Diego

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# FUNCIONES
def abrir_registro_productos():
   reg = tk.Toplevel()
   reg.title("Registro de Productos")
   reg.geometry("400x400")
   reg.resizable(False, False)

   # --- Etiquetas y Campos de Texto ---
   lbl_id = tk.Label(reg, text="ID del Producto:", font=("Arial", 12))
   lbl_id.pack(pady=5)
   txt_id = tk.Entry(reg, font=("Arial", 12))
   txt_id.pack(pady=5)
   lbl_desc = tk.Label(reg, text="Descripción:", font=("Arial", 12))
   lbl_desc.pack(pady=5)
   txt_desc = tk.Entry(reg, font=("Arial", 12))
   txt_desc.pack(pady=5)
   lbl_precio = tk.Label(reg, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(reg, font=("Arial", 12))
   txt_precio.pack(pady=5)
   lbl_categoria = tk.Label(reg, text="Categoría:", font=("Arial", 12))
   lbl_categoria.pack(pady=5)
   txt_categoria = tk.Entry(reg, font=("Arial", 12))
   txt_categoria.pack(pady=5)

   # --- Función para guardar ---
   def guardar_producto():
      id_prod = txt_id.get().strip()
      descripcion = txt_desc.get().strip()
      precio = txt_precio.get().strip()
      categoria = txt_categoria.get().strip()
      # Validaciones
      if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
         messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")
         return
      # Validar precio como número
      try:
         float(precio)
      except:
         messagebox.showerror("Error", "El precio debe ser un número.")
         return

      # Guardar en archivo de texto
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivo = os.path.join(BASE_DIR,"productos.txt")
      with open(archivo, "a", encoding="utf-8") as archivo:
         archivo.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")
         messagebox.showinfo("Guardado", "Producto registrado correctamente.")
         # Limpiar campos
         txt_id.delete(0, tk.END)
         txt_desc.delete(0, tk.END)
         txt_precio.delete(0, tk.END)
         txt_categoria.delete(0, tk.END)
   # --- Botón Guardar ---
   btn_guardar = tk.Button(reg, text="Guardar Producto", command=guardar_producto)
   btn_guardar.pack(pady=20)
   

from datetime import datetime

def mostrar_ticket(producto, precio, cantidad, total):
  ticket = tk.Toplevel()
  ticket.title("Ticket de Venta")
  ticket.geometry("300x350")
  ticket.resizable(False, False)

  # Fecha y hora
  fecha_hora = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

  # Texto del ticket
  texto = (
  " *** PUNTO DE VENTA ***\n"
  "--------------------------------------\n"
  f"Fecha: {fecha_hora}\n"
  "--------------------------------------\n"
  f"Producto: {producto}\n"
  f"Precio: ${precio}\n"
  f"Cantidad: {cantidad}\n"
  "--------------------------------------\n"
  f"TOTAL: ${total}\n"
  "--------------------------------------\n"
  " ¡GRACIAS POR SU COMPRA!\n"
  )

  lbl_ticket = tk.Label(ticket, text=texto, justify="left", font=("Consolas", 11))
  lbl_ticket.pack(pady=15)

  btn_cerrar = ttk.Button(ticket, text="Cerrar", command=ticket.destroy)
  btn_cerrar.pack(pady=10)
   
def abrir_registro_ventas():
   ven = tk.Toplevel()
   ven.title("Registro de Ventas")
   ven.geometry("420x430")
   ven.resizable(False, False)
   # ------------------------------------
   # Cargar productos desde productos.txt
   # ------------------------------------
   
   productos = {} #Este es un Array arreglo para que cuente valores
   try:
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivof = os.path.join(BASE_DIR,"productos.txt")
      with open(archivof, "r", encoding="utf-8") as archivo:
         for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 4:
               idp, desc, precio, cat = partes
               productos[desc] = float(precio)
   except FileNotFoundError:
      messagebox.showerror("Error", "No se encontró el archivo productos.txt")
      ven.destroy()
      return

   # Lista de nombres de productos
   lista_productos = list(productos.keys())
   # ------------------------------------
   # CONTROLES VISUALES
   # ------------------------------------
   lbl_prod = tk.Label(ven, text="Producto:", font=("Arial", 12))
   lbl_prod.pack(pady=5)
   cb_producto = ttk.Combobox(ven, values=lista_productos, font=("Arial", 12), state="readonly")
   cb_producto.pack(pady=5)
   lbl_precio = tk.Label(ven, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_precio.pack(pady=5)
   lbl_cantidad = tk.Label(ven, text="Cantidad:", font=("Arial", 12))
   lbl_cantidad.pack(pady=5)
   cantidad_var = tk.StringVar(ven)
   ven.cantidad_var = cantidad_var   # importante: mantiene la referencia
   txt_cantidad = tk.Entry(ven, font=("Arial", 12), textvariable=cantidad_var)
   txt_cantidad.pack(pady=5)  
   cantidad_var.trace_add("write", lambda *args: calcular_total())
   lbl_total = tk.Label(ven, text="Total:", font=("Arial", 12))
   lbl_total.pack(pady=5)
   txt_total = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_total.pack(pady=5)
   # ------------------------------------
   # FUNCIONES
   # ------------------------------------
   def actualizar_precio(event):      
      prod = cb_producto.get()
      if prod in productos:
         txt_precio.config(state="normal")
         txt_precio.delete(0, tk.END)
         txt_precio.insert(0, productos[prod])
         txt_precio.config(state="readonly")
         calcular_total()
   def calcular_total(*args):      
      try:
         cant = int(txt_cantidad.get())
         precio = float(txt_precio.get())
         total = cant * precio
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.insert(0, total)
         txt_total.config(state="readonly")
      except:
         # Si no hay número válido, limpiar el total
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.config(state="readonly")
   def registrar_venta():
      prod = cb_producto.get()
      precio = txt_precio.get()
      cant = txt_cantidad.get()
      total = txt_total.get()
      if prod == "" or precio == "" or cant == "" or total == "":
         messagebox.showwarning("Campos Vacíos", "Todos los campos deben estar completos.")
         return
      # Guardar venta
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivov = os.path.join(BASE_DIR,"ventas")
      with open(archivov, "a", encoding="utf-8") as archivo:
         archivo.write(f"{prod}|{precio}|{cant}|{total}\n")
         messagebox.showinfo("Venta Registrada", "La venta se registró correctamente.")
         mostrar_ticket(prod, precio, cant, total) 
      # Limpiar campos
      cb_producto.set("")
      txt_precio.config(state="normal"); txt_precio.delete(0, tk.END); txt_precio.config(state="readonly")
      txt_cantidad.delete(0, tk.END)
      txt_total.config(state="normal"); txt_total.delete(0, tk.END); txt_total.config(state="readonly")
   # ------------------------------------
   # EVENTOS Y BOTÓN
   # ------------------------------------
   cb_producto.bind("<<ComboboxSelected>>", actualizar_precio)
   btn_guardar = ttk.Button(ven, text="Registrar Venta", command=registrar_venta)
   btn_guardar.pack(pady=25)

def abrir_reportes():
  ventana = tk.Toplevel()
  ventana.title("Reporte de Ventas")
  ventana.geometry("700x400")
  ventana.configure(bg="#f2f2f2")

  titulo = tk.Label(ventana, text="Reporte de Ventas Realizadas",
  font=("Arial", 16, "bold"), bg="#f2f2f2")
  titulo.pack(pady=10)

  # Frame para el GRID
  frame_tabla = tk.Frame(ventana)
  frame_tabla.pack(pady=10)

  # Columnas del archivo ventas.txt
  columnas = ("producto", "precio", "cantidad", "total")

  tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=15)

  # Encabezados
  tabla.heading("producto", text="Producto")
  tabla.heading("precio", text="Precio")
  tabla.heading("cantidad", text="Cantidad")
  tabla.heading("total", text="Total")

  # Tamaño de columnas
  tabla.column("producto", width=250, anchor="center")
  tabla.column("precio", width=100, anchor="center")
  tabla.column("cantidad", width=100, anchor="center")
  tabla.column("total", width=120, anchor="center")

  tabla.pack()

  # --- Leer archivo ventas.txt ---
  try:
    with open("ventas.txt", "r", encoding="utf-8") as archivo:
     for linea in archivo:
      if linea.strip():
        datos = linea.strip().split("|")
        if len(datos) == 4:
          tabla.insert("", tk.END, values=datos)
  except FileNotFoundError:
    messagebox.showerror("Error", "El archivo ventas.txt no existe.")
    ventana.destroy()
    return
    mostrar_reporte_ventas()
# Ejecución individual para pruebas:
if __name__ == "__main__":
 root = tk.Tk()
 root.withdraw()
 
def abrir_acerca_de():
    acerca = tk.Toplevel()
    acerca.title("Acerca de")
    acerca.geometry("1000x1000")
    
    #Etiquetas y Campos de Texto 
    lbl_id = tk.Label(acerca, text="Software Pos Sneacker's Club 2025", font=("Arial",14))
    lbl_id.pack(pady=5)
    lbl_creado = tk.Label (acerca, text="Creado por: Alfredo Nicolas Rivas Lerma y Orona Hernandez Diego", font=("Arial", 12) )
    lbl_creado.pack(pady=5)
    lbl_grupo = tk.Label (acerca, text="Grupo: 3A Prog Vesp", font=("Arial", 12))
    lbl_grupo.pack(pady=5)
    
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