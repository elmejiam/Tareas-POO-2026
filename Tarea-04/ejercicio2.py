import tkinter as tk
from tkinter import messagebox


class Vendedor:
    def __init__(self, nombre, apellidos, edad):
        self.verificar_edad(edad)
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def verificar_edad(self, edad):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

    def imprimir(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEdad: {self.edad}"


class VentanaVendedor:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro de Vendedor")
        self.ventana.geometry("340x360")

        tk.Label(self.ventana, text="Nombre:").pack(pady=(15, 2))
        self.txt_nombre = tk.Entry(self.ventana, width=30)
        self.txt_nombre.pack()

        tk.Label(self.ventana, text="Apellidos:").pack(pady=(10, 2))
        self.txt_apellidos = tk.Entry(self.ventana, width=30)
        self.txt_apellidos.pack()

        tk.Label(self.ventana, text="Edad:").pack(pady=(10, 2))
        self.txt_edad = tk.Entry(self.ventana, width=30)
        self.txt_edad.pack()

        self.btn_guardar = tk.Button(
            self.ventana,
            text="Guardar Vendedor",
            command=self.procesar_registro
        )
        self.btn_guardar.pack(pady=15)

        self.lbl_resultado = tk.Label(self.ventana, text="", justify=tk.LEFT)
        self.lbl_resultado.pack(pady=10)

    def procesar_registro(self):
        nombre = self.txt_nombre.get().strip()
        apellidos = self.txt_apellidos.get().strip()
        edad_str = self.txt_edad.get().strip()

        if not nombre or not apellidos or not edad_str:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        try:
            edad = int(edad_str)
            vendedor = Vendedor(nombre, apellidos, edad)
            
            datos = vendedor.imprimir()
            self.lbl_resultado.config(text=datos, fg="black")
            messagebox.showinfo("Éxito", "Vendedor registrado correctamente")

        except ValueError as e:
            if "invalid literal" in str(e):
                mensaje_error = "La edad debe ser un número entero válido"
            else:
                mensaje_error = str(e)
            
            self.lbl_resultado.config(text="")
            messagebox.showerror("Error de validación", mensaje_error)

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaVendedor()
app.iniciar()
