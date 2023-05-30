from tkinder import *
from tkinder import ttk
import mariadb





def consultaCustom(self,query):
    try:

        conn = mariadb.connect(
            host="localhost",
            user = "root",
            password="",
            database = "sakila"
        )
    except mariadb.Erro as e:
        print("Error al conectar a la base de datos",e)

    cur = conn.cursor()
    cur.execute(query)
    return cur

def mostrarDatos(self) :

    cur = self.consultaCustom("SELECT * FROM `customer`")
    for (name,clave) in cur :
        print(nombre,clave)

if __name__=="__main":
    ventana = Th()
    aplicacion = Alumno (ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()