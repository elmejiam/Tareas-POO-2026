import tkinter as tk
from tkinter import ttk


class VentanaExcepciones:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba de Excepciones")
        self.ventana.geometry("450x380")

        self.boton = ttk.Button(
            self.ventana,
            text="Probar flujo",
            command=self.correr_pruebas
        )
        self.boton.pack(pady=15)

        self.caja_texto = tk.Text(self.ventana, width=45, height=14)
        self.caja_texto.pack(padx=10, pady=5)

    def imprimir(self, texto):
        self.caja_texto.insert(tk.END, texto + "\n")

    def correr_pruebas(self):
        self.caja_texto.delete("1.0", tk.END)

        try:
            self.imprimir("Ingresando al primer try")
            resultado = 10000 / 0
            self.imprimir("Después de la división")
        except ZeroDivisionError:
            self.imprimir("División por cero")
        finally:
            self.imprimir("Ingresando al primer finally")

        try:
            self.imprimir("Ingresando al segundo try")
            obj = None
            obj.metodo()
            self.imprimir("Imprimiendo objeto")
        except ZeroDivisionError:
            self.imprimir("División por cero")
        except Exception:
            self.imprimir("Ocurrió una excepción")
        finally:
            self.imprimir("Ingresando al segundo finally")

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaExcepciones()
app.iniciar()
