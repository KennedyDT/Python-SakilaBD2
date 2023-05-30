from tkinter import *
from tkinter import ttk
import mariadb
from tkinter import simpledialog

class CustomerApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Consulta de Clientes")

        # Crear los botones
        self.button1 = Button(self.ventana, text="Consulta 1", command=self.consulta1)
        self.button2 = Button(self.ventana, text="Consulta 2", command=self.consulta2)
        self.button3 = Button(self.ventana, text="Consulta 3", command=self.consulta3)
        self.button4 = Button(self.ventana, text="Consulta 4", command=self.consulta4)
        self.button5 = Button(self.ventana, text="Consulta 5", command=self.consulta5)
        self.button6 = Button(self.ventana, text="Consulta 6", command=self.consulta6)

        # Posicionar los botones en la ventana
        self.button1.grid(row=0, column=0, padx=10, pady=10)
        self.button2.grid(row=0, column=1, padx=10, pady=10)
        self.button3.grid(row=0, column=2, padx=10, pady=10)
        self.button4.grid(row=1, column=0, padx=10, pady=10)
        self.button5.grid(row=1, column=1, padx=10, pady=10)
        self.button6.grid(row=1, column=2, padx=10, pady=10)

    def ejecutarConsulta(self, query):
        try:
            conn = mariadb.connect(
                host="localhost",
                user="root",
                password="",  # Aquí debes proporcionar la contraseña correcta si es necesario
                database="sakila"
            )
        except mariadb.Error as e:
            print("Error al conectar a la base de datos", e)
            return

        cur = conn.cursor()
        cur.execute(query)

        # Obtener los nombres de las columnas
        columns = [desc[0] for desc in cur.description]

        # Obtener los resultados de la consulta
        results = cur.fetchall()

        conn.close()

        return columns, results

    def obtenerIDConsulta(self):
        id_consulta = simpledialog.askinteger("ID de consulta", "Ingrese el ID a consultar:")
        return id_consulta

    def mostrarResultados(self, columns, results):
        ventana_resultados = Toplevel(self.ventana)
        ventana_resultados.title("Resultados de consulta")

        # Crear el Treeview para mostrar los resultados
        treeview = ttk.Treeview(ventana_resultados)
        treeview.grid(row=0, columnspan=len(columns), padx=10, pady=10)

        # Agregar las columnas al Treeview
        treeview["columns"] = columns
        treeview.heading("#0", text="Index")
        for i, column in enumerate(columns):
            treeview.heading(column, text=column)

        # Agregar los resultados al Treeview
        for i, row in enumerate(results):
            treeview.insert("", "end", text=str(i+1), values=row)

    def consulta1(self):
        id_consulta = self.obtenerIDConsulta()
        if id_consulta is not None:
            query = f"call get_rental_history({id_consulta}) "
            columns, results = self.ejecutarConsulta(query)
            if results is not None:
                self.mostrarResultados(columns, results)

    def consulta2(self):
        id_consulta = self.obtenerIDConsulta()
        if id_consulta is not None:
            query = f"SELECT * FROM tabla2 WHERE id = {id_consulta}"
            columns, results = self.ejecutarConsulta(query)
            if results is not None:
                self.mostrarResultados(columns, results)

    def consulta3(self):
        id_consulta = self.obtenerIDConsulta()
        if id_consulta is not None:
            query = f"SELECT * FROM tabla3 WHERE id = {id_consulta}"
            columns, results = self.ejecutarConsulta(query)
            if results is not None:
                self.mostrarResultados(columns, results)

    def consulta4(self):
        query = "SELECT * FROM tabla4"
        columns, results = self.ejecutarConsulta(query)
        if results is not None:
            self.mostrarResultados(columns, results)

    def consulta5(self):
        query = "SELECT * FROM tabla5"
        columns, results = self.ejecutarConsulta(query)
        if results is not None:
            self.mostrarResultados(columns, results)

    def consulta6(self):
        query = "SELECT * FROM tabla6"
        columns, results = self.ejecutarConsulta(query)
        if results is not None:
            self.mostrarResultados(columns, results)

if __name__ == "__main__":
    ventana = Tk()
    aplicacion = CustomerApp(ventana)
    ventana.mainloop()
