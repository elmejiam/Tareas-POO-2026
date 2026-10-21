import tkinter as tk
from tkinter import ttk
import math

class Figura:
    def volumen(self):
        pass
    def superficie(self):
        pass

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    def volumen(self):
        return math.pi * self.radio**2 * self.altura
    def superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(Figura):
    def __init__(self, radio):
        self.radio = radio
    def volumen(self):
        return (4/3) * math.pi * self.radio**3
    def superficie(self):
        return 4 * math.pi * self.radio**2

class Piramide(Figura):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema
    def volumen(self):
        return (self.base**2 * self.altura) / 3
    def superficie(self):
        return self.base**2 + 2 * self.base * self.apotema

class VentanaFiguras:
    def __init__(self):
        self.v = tk.Tk()
        self.v.title("Cálculo de Figuras Geométricas")
        self.v.geometry("400x480")
        self.v.resizable(False, False)
        self._crear_interfaz()
        self.v.mainloop()

    def _crear_interfaz(self):
        ttk.Label(self.v, text="Seleccione la figura:", font=("Arial", 11)).pack(pady=10)
        self.figura = tk.StringVar(value="Cilindro")
        opciones = ["Cilindro", "Esfera", "Pirámide"]
        ttk.OptionMenu(self.v, self.figura, *opciones, command=self._actualizar_campos).pack()

        self.frame_datos = ttk.Frame(self.v)
        self.frame_datos.pack(pady=10)
        self.campos = {}
        self._actualizar_campos()

        ttk.Button(self.v, text="Calcular", command=self._calcular).pack(pady=10)

        self.resultado_volumen = ttk.Label(self.v, text="Volumen: ")
        self.resultado_superficie = ttk.Label(self.v, text="Superficie: ")
        self.resultado_volumen.pack(anchor="w", padx=20, pady=5)
        self.resultado_superficie.pack(anchor="w", padx=20, pady=5)

    def _actualizar_campos(self, *args):
        for widget in self.frame_datos.winfo_children():
            widget.destroy()
        self.campos.clear()
        figura = self.figura.get()
        if figura == "Cilindro":
            self._crear_campo("Radio (cm):")
            self._crear_campo("Altura (cm):")
        elif figura == "Esfera":
            self._crear_campo("Radio (cm):")
        elif figura == "Pirámide":
            self._crear_campo("Base (cm):")
            self._crear_campo("Altura (cm):")
            self._crear_campo("Apotema (cm):")

    def _crear_campo(self, texto):
        frame = ttk.Frame(self.frame_datos)
        frame.pack(pady=4)
        ttk.Label(frame, text=texto).pack(side="left", padx=5)
        entrada = ttk.Entry(frame, width=10)
        entrada.pack(side="left")
        self.campos[texto] = entrada

    def _calcular(self):
        try:
            figura = self.figura.get()
            if figura == "Cilindro":
                r = float(self.campos["Radio (cm):"].get())
                h = float(self.campos["Altura (cm):"].get())
                obj = Cilindro(r, h)
            elif figura == "Esfera":
                r = float(self.campos["Radio (cm):"].get())
                obj = Esfera(r)
            elif figura == "Pirámide":
                b = float(self.campos["Base (cm):"].get())
                h = float(self.campos["Altura (cm):"].get())
                a = float(self.campos["Apotema (cm):"].get())
                obj = Piramide(b, h, a)
            v = obj.volumen()
            s = obj.superficie()
            self.resultado_volumen.config(text=f"Volumen: {v:.2f} cm³")
            self.resultado_superficie.config(text=f"Superficie: {s:.2f} cm²")
        except ValueError:
            self.resultado_volumen.config(text="Error: revise los valores ingresados")
            self.resultado_superficie.config(text="")
