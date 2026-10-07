from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"


class Planeta:
    def __init__(self, nombre=None, satelites=0, masa=0.0, volumen=0.0,
                 diametro=0, distancia_sol=0, tipo=None, observable=False):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa                  # en kilogramos
        self.volumen = volumen            # en kilómetros cúbicos
        self.diametro = diametro          # en kilómetros
        self.distancia_sol = distancia_sol  # en millones de kilómetros
        self.tipo = tipo
        self.observable = observable

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Cantidad de satélites:", self.satelites)
        print("Masa (kg):", self.masa)
        print("Volumen (km³):", self.volumen)
        print("Diámetro (km):", self.diametro)
        print("Distancia media al Sol (millones de km):", self.distancia_sol)
        print("Tipo de planeta:", self.tipo.value if self.tipo else None)
        print("Observable a simple vista:", self.observable)

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_exterior(self):
        # 1 UA = 149 597 870 km = 149.59787 millones de km
        ua_en_millones_km = 149.59787
        distancia_en_ua = self.distancia_sol / ua_en_millones_km
        # El cinturón de asteroides llega hasta 3.4 UA
        return distancia_en_ua > 3.4


def main():
    tierra = Planeta("Tierra", 1, 5.972e24, 1.08321e12, 12742, 150,
                     TipoPlaneta.TERRESTRE, True)

    jupiter = Planeta("Júpiter", 79, 1.898e27, 1.4313e15, 139820, 778,
                      TipoPlaneta.GASEOSO, True)

    print("Datos del primer planeta")
    tierra.mostrar_datos()
    print("Densidad:", tierra.calcular_densidad(), "kg/km³")
    if tierra.es_exterior():
        print("Es un planeta exterior")
    else:
        print("No es un planeta exterior")

    print()
    print("Datos del segundo planeta")
    jupiter.mostrar_datos()
    print("Densidad:", jupiter.calcular_densidad(), "kg/km³")
    if jupiter.es_exterior():
        print("Es un planeta exterior")
    else:
        print("No es un planeta exterior")


main()
