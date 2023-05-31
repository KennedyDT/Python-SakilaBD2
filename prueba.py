import tkinter as tk

# Crear una instancia de la ventana
ventana = tk.Tk()

# Configurar el título de la ventana
ventana.title("Mi ventana Tkinter")

# Configurar las dimensiones de la ventana
ventana.geometry("400x300")

# Agregar widgets a la ventana
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!")
etiqueta.pack()

boton = tk.Button(ventana, text="Cerrar", command=ventana.quit)
boton.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()