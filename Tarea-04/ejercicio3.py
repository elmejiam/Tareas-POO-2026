import math
import tkinter as tk
from tkinter import messagebox


class ArithmeticException(Exception):
    pass


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticException("El valor debe ser positivo para calcular el logaritmo neperiano.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticException("El valor debe ser positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)


class VentanaCalculos:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculos Numéricos")
        self.ventana.geometry("360x320")

        tk.Label(self.ventana, text="Ingrese un valor numérico:").pack(pady=(20, 5))
        self.txt_valor = tk.Entry(self.ventana, width=20)
        self.txt_valor.pack(pady=5)

        self.btn_ln = tk.Button(
            self.ventana,
            text="Calcular Logaritmo Neperiano",
            command=self.procesar_logaritmo
        )
        self.btn_ln.pack(pady=(15, 5))

        self.btn_raiz = tk.Button(
            self.ventana,
            text="Calcular Raíz Cuadrada",
            command=self.procesar_raiz
        )
        self.btn_raiz.pack(pady=5)

        self.lbl_resultado = tk.Label(self.ventana, text="", font=("Arial", 10, "bold"))
        self.lbl_resultado.pack(pady=20)

    def obtener_valor(self):
        entrada = self.txt_valor.get().strip()
        if not entrada:
            raise ValueError("Por favor, ingrese un número.")
        try:
            return float(entrada)
        except ValueError:
            raise ValueError("El valor ingresado no es un número válido.")

    def procesar_logaritmo(self):
        try:
            num = self.obtener_valor()
            resultado = CalculosNumericos.calcular_logaritmo_neperiano(num)
            self.lbl_resultado.config(text=f"Ln({num}) = {resultado:.4f}")
        except ArithmeticException as error_aritmetico:
            self.lbl_resultado.config(text="")
            messagebox.showerror("Error aritmético", str(error_aritmetico))
        except ValueError as error_valor:
            self.lbl_resultado.config(text="")
            messagebox.showwarning("Dato inválido", str(error_valor))

    def procesar_raiz(self):
        try:
            num = self.obtener_valor()
            resultado = CalculosNumericos.calcular_raiz_cuadrada(num)
            self.lbl_resultado.config(text=f"√({num}) = {resultado:.4f}")
        except ArithmeticException as error_aritmetico:
            self.lbl_resultado.config(text="")
            messagebox.showerror("Error aritmético", str(error_aritmetico))
        except ValueError as error_valor:
            self.lbl_resultado.config(text="")
            messagebox.showwarning("Dato inválido", str(error_valor))

    def iniciar(self):
        self.ventana.mainloop()


app = VentanaCalculos()
app.iniciar()
