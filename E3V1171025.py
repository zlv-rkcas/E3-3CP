#Nuestra primera version del software
#Aqui creamos nuestra primera ventana como ejemplo
#Agregamos color de fondo, tamaño de la ventana y agregamos un tiulo

#importar las bibliotecas
import tkinter as tk
#configurar la ventana
ventana = tk.Tk()
ventana.title("ADICCIONES AL CONSUMO DE CONTENIDOS EN REDES SOCIALES") #agregamos titulo
ventana.geometry("600x400") #agregamos medidas a la ventana
ventana.config(bg="#D36969") #agregamos color a la ventana


# MANDAR A TRAER MI VENTANA
ventana.mainloop()