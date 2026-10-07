from enum import Enum


class Combustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"


class TipoAutomovil(Enum):
    CARRO_DE_CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"


class Automovil:
    def __init__(self, marca, modelo, motor, combustible, tipo, puertas,
                 asientos, velocidad_maxima, color, velocidad_actual=0):
        self.marca = marca
        self.modelo = modelo                    # año de fabricación
        self.motor = motor                      # cilindraje en litros
        self.combustible = combustible
        self.tipo = tipo
        self.puertas = puertas
        self.asientos = asientos
        self.velocidad_maxima = velocidad_maxima  # km/h
        self.color = color
        self.velocidad_actual = velocidad_actual  # km/h

    # ---------- Getters ----------
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_combustible(self):
        return self.combustible

    def get_tipo(self):
        return self.tipo

    def get_puertas(self):
        return self.puertas

    def get_asientos(self):
        return self.asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    # ---------- Setters ----------
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_combustible(self, combustible):
        self.combustible = combustible

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_puertas(self, puertas):
        self.puertas = puertas

    def set_asientos(self, asientos):
        self.asientos = asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    # ---------- Comportamiento ----------
    def acelerar(self, incremento):
        nueva_velocidad = self.velocidad_actual + incremento
        if nueva_velocidad > self.velocidad_maxima:
            print("No se puede acelerar más allá de la velocidad máxima de",
                  self.velocidad_maxima, "km/h")
        else:
            self.velocidad_actual = nueva_velocidad

    def desacelerar(self, decremento):
        nueva_velocidad = self.velocidad_actual - decremento
        if nueva_velocidad < 0:
            print("No se puede desacelerar a una velocidad negativa")
        else:
            self.velocidad_actual = nueva_velocidad

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            print("El automóvil está detenido, no se puede calcular el tiempo")
            return None
        return distancia / self.velocidad_actual  # en horas

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Modelo (año):", self.modelo)
        print("Motor (litros):", self.motor)
        print("Combustible:", self.combustible.value)
        print("Tipo de automóvil:", self.tipo.value)
        print("Número de puertas:", self.puertas)
        print("Cantidad de asientos:", self.asientos)
        print("Velocidad máxima (km/h):", self.velocidad_maxima)
        print("Color:", self.color.value)
        print("Velocidad actual (km/h):", self.velocidad_actual)


def main():
    auto = Automovil("Mazda", 2022, 2.0, Combustible.GASOLINA,
                     TipoAutomovil.COMPACTO, 4, 5, 200, Color.ROJO)

    print("Datos del automóvil")
    auto.mostrar_datos()
    print()

    auto.set_velocidad_actual(100)
    print("Velocidad actual:", auto.get_velocidad_actual(), "km/h")

    auto.acelerar(20)
    print("Después de acelerar 20 km/h:", auto.get_velocidad_actual(), "km/h")

    auto.desacelerar(50)
    print("Después de desacelerar 50 km/h:", auto.get_velocidad_actual(), "km/h")

    auto.frenar()
    print("Después de frenar:", auto.get_velocidad_actual(), "km/h")


main()
