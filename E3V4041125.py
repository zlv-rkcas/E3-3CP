#La version mas reciente de nuestro software (4) 



#Importamos las bibliotecas
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


# Configuración de todos los frames
COLOR_FONDO = "#2E3440"
COLOR_MENU = "#3B4252"
COLOR_TEXTO = "#ECEFF4"
COLOR_BOTON = "#81A1C1"
FUENTE_TITULO = ("Segoe UI Semibold", 18)
FUENTE_TEXTO = ("Century Gothic", 12)

# Ventana Principal
root = tk.Tk()
root.title("Software de Detección de Adicciones (Consumo De Contenidos)")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# Frame del menú lateral
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# Frame del contenido (derecha)
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# Función para cambiar a las siguientes páginas
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]() 
    # Llama a la función correspondiente

# Página Bienvenida
def pagina_bienvenida():
    tk.Label(contenido_frame, text="Bienvenido/a al Software de Detección de Adicciones",
             font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=30)
    
    #Cargar Imagenes
    img1 = Image.open("images.png")
    img1 = img1.resize((180,180))
    img2 = Image.open("Facebook.png")
    img2 = img2.resize((180,180))
    img3 = Image.open("insta.png")
    img3 = img3.resize((180,180))

    contenido_frame.img1 = ImageTk.PhotoImage(img1)
    contenido_frame.img2 = ImageTk.PhotoImage(img2)
    contenido_frame.img3 = ImageTk.PhotoImage(img3)

    #Frame Contenedor para ponerlas lado a lado
    frame_imagenes = tk.Frame(contenido_frame, bg=COLOR_FONDO)
    frame_imagenes.pack(pady=20)

    tk.Label(frame_imagenes, image=contenido_frame.img1, bg=COLOR_FONDO).pack(side="left", padx=10)
    tk.Label(frame_imagenes, image=contenido_frame.img2, bg=COLOR_FONDO).pack(side="left", padx=10)
    tk.Label(frame_imagenes, image=contenido_frame.img3, bg=COLOR_FONDO).pack(side="right", padx=10)
    
    texto_bienvenida = "¡Hola!, Somos unos estudiantes del CETis 151, BIenvenido a nuestro Software. Aqui detectaremos si tienes una adiccion a la tecnologia (en este caso al Consumo de Contenidos). Estamos Solamente para detectar un problema y dar un pequeño apoyo"
    tk.Label(contenido_frame, text=texto_bienvenida, bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO, wraplength=600, justify="left").pack(pady=10)
    tk.Label(contenido_frame, text="Usa el menú lateral para navegar entre secciones.",
             bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO).pack(pady=10)
    tk.Button(contenido_frame, text="Siguiente", bg=COLOR_BOTON, fg="black", width=20, command=lambda:mostrar_pagina("Inicio De Sesión")).pack(pady=15)

    # Pagina de Inicio De Sesion
def pagina_inicio():
    tk.Label(contenido_frame, text="Iniciar Sesión", font=FUENTE_TITULO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=20)
    tk.Button(contenido_frame, text="Regresar", bg=COLOR_BOTON, fg="black", width=10, command=lambda:mostrar_pagina("Bienvenida")).pack(pady=10)
    
    sesion = ["Correo", "Contraseña", "Confirmar Contraseña"]
    for sesion in sesion:
        tk.Label(contenido_frame, text=f"{sesion}:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO).pack(pady=3)
        tk.Entry(contenido_frame, width=40, show="*" if "Contraseña" in sesion else "").pack(pady=3)
    
    tk.Button(contenido_frame, text="Entrar", bg=COLOR_BOTON, fg="black", width=15, command=lambda:mostrar_pagina("Aviso")).pack(pady=15)
    tk.Label(contenido_frame, text="¿No Tienes Cuenta?, Registrate", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO).pack(pady=10)
    tk.Button(contenido_frame, text="Registrarse", bg=COLOR_BOTON, fg="black", width=15, command=lambda: mostrar_pagina("Registro")).pack(pady=15)

#Pagina Aviso
def pagina_aviso():
    tk.Label(contenido_frame, text="¡Aviso!", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=10)
    tk.Button(contenido_frame, text="Regresar", bg=COLOR_BOTON, fg="black", width=10, command=lambda:mostrar_pagina("Inicio De Sesión")).pack(pady=10)
    img4 = Image.open("adiccion.jpg")
    img4 = img4.resize((400, 300))
    contenido_frame.imagen_adiccion = ImageTk.PhotoImage(img4)
    tk.Label(contenido_frame, image=contenido_frame.imagen_adiccion, bg=COLOR_FONDO).pack(pady=20)
    text2 = "Estas a punto de hacer un formulario en donde tienes que contestar con toda sinceridad, ya que se detectara si tienes con una adiccion, y si es asi el caso, se brindara una agenda o numeros de una asociación"
    tk.Label(contenido_frame, text=text2, bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO, wraplength=600, justify="left").pack(pady=10)
    tk.Button(contenido_frame, text="Comenzar", bg=COLOR_BOTON, fg="black", width=15, command=lambda:mostrar_pagina("Test")).pack(pady=15)

# Página de Registro
def pagina_registro():
    tk.Label(contenido_frame, text="Registro de Usuario", font=FUENTE_TITULO,
             bg=COLOR_FONDO, fg=COLOR_TEXTO).pack(pady=20)
    tk.Button(contenido_frame, text="Regresar", bg=COLOR_BOTON, fg="black", width=10, command=lambda:mostrar_pagina("Inicio De Sesión")).pack(pady=10)
    campos = ["Nombre", "Correo", "Teléfono", "Contraseña", "Confirmar Contraseña"]
    for campo in campos:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO).pack(pady=3)
        tk.Entry(contenido_frame, width=40, show="*" if "Contraseña" in campo else "").pack(pady=3)
    tk.Button(contenido_frame, text="Registrar", bg=COLOR_BOTON, fg="black", width=15, command=lambda:mostrar_pagina("Inicio De Sesión")).pack(pady=15)

# Página del Test (Formulario)
def pagina_test():
    tk.Label(contenido_frame, text="Formulario de 10 Preguntas", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TITULO).pack(pady=10)
    tk.Button(contenido_frame, text="Regresar", bg=COLOR_BOTON, fg="black", width=10, command=lambda:mostrar_pagina("Aviso")).pack(pady=10)
    test = ["¿Revisas tus redes sociales apenas te despiertas o antes de dormir?", "¿Sientes ansiedad o incomodidad cuando no puedes usar tus redes sociales?", "¿pasa mas de tres horas al dia conectado(a) a redes sociales?","¿Prefieres interactuar por redes antes de hablar en persona?","¿Te distraes facilmente con notificaciones mientras estudias o trabajas?","¿Has intentado redusir el uso de redes sociales sin lograrlo?","¿Te compras con otras personas por lo que publican en redes siciales?","¿Publicas constantemente para recibir 'me gusta' o comentarios?","¿Sientes que pierdes tiempo valioso por estar en redes sociales?","¿Tus familiares y amigos te han dicho que usasdemasiado el celular a las redes?"]
    for test in test:
        tk.Label(contenido_frame, text=f"{test}:", bg=COLOR_FONDO, fg=COLOR_TEXTO, font=FUENTE_TEXTO).pack(pady=3)
        tk.Entry(contenido_frame, width=40).pack(pady=3)
    tk.Button(contenido_frame, text="Enviar", bg=COLOR_BOTON, fg="black", width=15).pack(pady=15)

# Diccionario de páginas
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Inicio De Sesión": pagina_inicio,
    "Aviso": pagina_aviso,
    "Registro": pagina_registro,
    "Test": pagina_test
}

# Botones del menú lateral
botones = [
    ("Bienvenida", "Bienvenida"),
    ("Inicio De Sesión", "Inicio De Sesión"),
    ("Aviso", "Aviso"),
    ("Registro", "Registro"),
    ("Formulario (Test)", "Test"),
]

for texto, clave in botones:
    tk.Button(menu_frame, text=texto, font=FUENTE_TEXTO, bg=COLOR_BOTON,
              fg="white", relief="flat", cursor="hand2",
              command=lambda n=clave: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

# Mostrar la página de bienvenida por defecto
mostrar_pagina("Bienvenida")

# Mandamos a llamar a la ventana
root.mainloop()