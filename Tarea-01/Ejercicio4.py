class Potencias:
    def __init__(self, numero):
        self.numero = numero
        self.cuadrado = 0
        self.cubo = 0

    def calcular(self):
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3

    def mostrar_resultado(self):
        print(f"Número: {self.numero}")
        print(f"Cuadrado: {self.cuadrado}")
        print(f"Cubo: {self.cubo}")

numero = float(input("Ingrese un número: "))

potencia = Potencias(numero)
potencia.calcular()
potencia.mostrar_resultado()