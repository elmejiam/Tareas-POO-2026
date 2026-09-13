import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.longitud = 0

    def calcular(self):
        self.area = math.pi * self.radio ** 2
        self.longitud = 2 * math.pi * self.radio

    def mostrar_resultado(self):
        print(f"Radio: {self.radio}")
        print(f"Área del círculo: {self.area:.2f}")
        print(f"Longitud de la circunferencia: {self.longitud:.2f}")

radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)
circulo.calcular()
circulo.mostrar_resultado()