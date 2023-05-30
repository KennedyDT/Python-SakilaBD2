from tkinter import *
from tkinter import ttk
import mariadb

class customer:
    def __init__(self,ventana):

        self.ventana = ventana
        self.ventana.title("Hola")

        Label(self.ventana, text="Nombre").grid(row=0, column=0)


# def consultaCustom(self,query):
#     try:

#         conn = mariadb.connect(
#             host="localhost",
#             user = "root",
#             password="",
#             database = "sakila"
#         )
#     except mariadb.Erro as e:
#         print("Error al conectar a la base de datos",e)

#     cur = conn.cursor()
#     cur.execute(query)
#     return cur

def mostrarDatos(self) :
    cur=self.consultaCustom("SELECT * FROM `customer`")
    for (name,clave) in cur :
        print(name,clave)

if __name__=="__main":
    ventana = Tk()
    aplicacion=customer(ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()