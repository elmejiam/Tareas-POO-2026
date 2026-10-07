import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio  # en cm

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base      # en cm
        self.altura = altura  # en cm

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado  # en cm

    def calcular_area(self):
        return math.pow(self.lado, 2)

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base      # en cm
        self.altura = altura  # en cm

    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def tipo_triangulo(self):
        a = self.base
        b = self.altura
        c = self.calcular_hipotenusa()

        if (a == b) and (b == c):
            return "Equilátero"
        elif (a == b) or (a == c) or (b == c):
            return "Isósceles"
        else:
            return "Escaleno"

def main():
    circulo = Circulo(5)
    rectangulo = Rectangulo(8, 4)
    cuadrado = Cuadrado(6)
    triangulo = TrianguloRectangulo(3, 4)

    print("--- Círculo ---")
    print("Radio:", circulo.radio, "cm")
    print("Área:", round(circulo.calcular_area(), 2), "cm²")
    print("Perímetro:", round(circulo.calcular_perimetro(), 2), "cm")

    print()
    print("--- Rectángulo ---")
    print("Base:", rectangulo.base, "cm, Altura:", rectangulo.altura, "cm")
    print("Área:", rectangulo.calcular_area(), "cm²")
    print("Perímetro:", rectangulo.calcular_perimetro(), "cm")

    print()
    print("--- Cuadrado ---")
    print("Lado:", cuadrado.lado, "cm")
    print("Área:", cuadrado.calcular_area(), "cm²")
    print("Perímetro:", cuadrado.calcular_perimetro(), "cm")

    print()
    print("--- Triángulo rectángulo ---")
    print("Base:", triangulo.base, "cm, Altura:", triangulo.altura, "cm")
    print("Hipotenusa:", triangulo.calcular_hipotenusa(), "cm")
    print("Área:", triangulo.calcular_area(), "cm²")
    print("Perímetro:", triangulo.calcular_perimetro(), "cm")
    print("Tipo de triángulo:", triangulo.tipo_triangulo())
main()
