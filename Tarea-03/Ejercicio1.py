import tkinter as tk
from tkinter import ttk
from statistics import mean, stdev

class CalculadoraNotas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculo de Notas")
        self.ventana.geometry("350x380")
        self.ventana.resizable(False, False)
        self._crear_interfaz()
        self.ventana.mainloop()

    def _crear_interfaz(self):
        ttk.Label(self.ventana, text="Ingrese las 5 notas del estudiante:", font=("Arial", 11)).pack(pady=10)

        self.notas = []
        for i in range(5):
            frame = ttk.Frame(self.ventana)
            frame.pack(pady=3)
            ttk.Label(frame, text=f"Nota {i+1}:").pack(side="left", padx=5)
            entrada = ttk.Entry(frame, width=10)
            entrada.pack(side="left")
            self.notas.append(entrada)

        ttk.Button(self.ventana, text="Calcular", command=self.calcular).pack(pady=15)

        self.resultado_promedio = ttk.Label(self.ventana, text="Promedio: ", font=("Arial", 10))
        self.resultado_desviacion = ttk.Label(self.ventana, text="Desviación estándar: ", font=("Arial", 10))
        self.resultado_mayor = ttk.Label(self.ventana, text="Nota mayor: ", font=("Arial", 10))
        self.resultado_menor = ttk.Label(self.ventana, text="Nota menor: ", font=("Arial", 10))

        self.resultado_promedio.pack(anchor="w", padx=20, pady=3)
        self.resultado_desviacion.pack(anchor="w", padx=20, pady=3)
        self.resultado_mayor.pack(anchor="w", padx=20, pady=3)
        self.resultado_menor.pack(anchor="w", padx=20, pady=3)

    def calcular(self):
        try:
            valores = [float(e.get()) for e in self.notas]
            if len(valores) != 5:
                return
            promedio = mean(valores)
            desviacion = stdev(valores)
            mayor = max(valores)
            menor = min(valores)

            self.resultado_promedio.config(text=f"Promedio: {promedio:.2f}")
            self.resultado_desviacion.config(text=f"Desviación estándar: {desviacion:.2f}")
            self.resultado_mayor.config(text=f"Nota mayor: {mayor:.2f}")
            self.resultado_menor.config(text=f"Nota menor: {menor:.2f}")
        except ValueError:
            for label in [self.resultado_promedio, self.resultado_desviacion, self.resultado_mayor, self.resultado_menor]:
                label.config(text="Error: verifique las notas ingresadas")
