from tkinter import *
from tkinter import ttk
import mariadb
from tkinter import simpledialog

class CustomerApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Proyecto Sakila")

        # Crear los botones
        self.button1 = Button(self.ventana, text="Historial cliente", command=self.consulta1)
        self.button2 = Button(self.ventana, text="Ingresos cliente", command=self.consulta2)
        self.button3 = Button(self.ventana, text="Top peliculas", command=self.consulta3)
        self.button4 = Button(self.ventana, text="Disponibles", command=self.consulta4)
        
        # Crear el botón 5
        self.button5 = Button(self.ventana, text="Auditoria", command=self.consulta5)
        self.button5.grid(row=1, column=1, padx=10, pady=10)

        # Crear el Treeview para mostrar los resultados
        self.treeview = ttk.Treeview(self.ventana)
        self.treeview.grid(row=2, columnspan=2, padx=10, pady=10)

        self.button6 = Button(self.ventana, text="Edad", command=self.consulta6)

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

        # Borrar los datos anteriores en el Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Agregar las columnas al Treeview
        self.treeview["columns"] = columns
        self.treeview.heading("#0", text="Index")
        for i, column in enumerate(columns):
            self.treeview.heading(column, text=column)

        # Obtener los resultados de la consulta
        results = cur.fetchall()
        for i, row in enumerate(results):
            self.treeview.insert("", "end", text=str(i+1), values=row)

        conn.close()

    def obtenerIDConsulta(self):
        id_consulta = simpledialog.askinteger("ID de consulta", "Ingrese el ID a consultar:")
        return id_consulta

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
            query = f"call get_payment_history({id_consulta}) "
            columns, results = self.ejecutarConsulta(query)
            if results is not None:
                self.mostrarResultados(columns, results)

    def consulta3(self):
        id_consulta = self.obtenerIDConsulta()
        if id_consulta is not None:
            query = f"call get_populary_films({id_consulta}) "
            columns, results = self.ejecutarConsulta(query)
            if results is not None:
                self.mostrarResultados(columns, results)

    def consulta4(self):
        id_consulta = self.obtenerIDConsulta()
        if id_consulta is not None:
            query = f"call get_film_available({id_consulta}) "
            columns, results = self.ejecutarConsulta(query)
            if results is not None:
                self.mostrarResultados(columns, results)

    
    def consulta5(self):
        query = "SELECT * FROM customer_audit"
        self.ejecutarConsulta(query)

    def consulta6(self):
        query = "SELECT * FROM suppliers"
        self.ejecutarConsulta(query)

if __name__ == "__main__":
    ventana = Tk()
    aplicacion = CustomerApp(ventana)
    ventana.mainloop()


