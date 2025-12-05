#Esta es la tercera version
#Aqui tenemos un ejemplo de como tiene que quedar nuestro software
#Tenemos el menu lateral, 3 ventanas (bienvenida, registro y el test)
#Se les agregó botones, color de fondo, color de la letra, estilo de texto, etc

import tkinter as tk
from tkinter import ttk

# ---------- CONFIGURACIÓN DE COLORES Y FUENTE ----------
COLOR_FONDO = "#F5F5F5"
COLOR_MENU = "#007ACC"
COLOR_TEXTO = "#FFFFFF"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# ---------- VENTANA PRINCIPAL ----------
root = tk.Tk()
root.title("Bienestar Total")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# ---------- FRAME MENÚ LATERAL ----------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# ---------- FRAME CONTENIDO ----------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# ---------- FUNCIÓN PARA CAMBIAR DE PÁGINA ----------
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# ---------- PÁGINAS ----------
def pagina_bienvenida():
    tk.Label(contenido_frame, text=" Bienvenido a Bienestar Total", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="Tu espacio de apoyo, información y salud emocional.", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text=" 📋 Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    
    # Campo Nombre
    tk.Label(contenido_frame, text="Nombre", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)
    tk.Entry(contenido_frame, width=40).pack(pady=5)
    
    # Campo Edad
    tk.Label(contenido_frame, text="Edad", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)
    tk.Entry(contenido_frame, width=40).pack(pady=5)
    
    # Campo Correo
    tk.Label(contenido_frame, text="Correo", font=FUENTE_TEXTO, bg=COLOR_FONDO).pack(pady=5)
    tk.Entry(contenido_frame, width=40).pack(pady=5)


def pagina_test():
    tk.Label(contenido_frame, text=" 🧠 Test de Bienestar", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Responde las siguientes preguntas para conocer tu nivel de bienestar.", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="Iniciar Test").pack(pady=20)

# ---------- DICCIONARIO DE PÁGINAS ----------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
}

# ---------- BOTONES DE MENÚ LATERAL ----------
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)


# ---------- MOSTRAR PÁGINA INICIAL ----------
pagina_bienvenida()

root.mainloop()