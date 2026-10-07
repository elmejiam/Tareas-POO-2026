class Persona:
    def __init__(self, nombre, apellido, documento, anio_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento:", self.documento)
        print("Año de nacimiento:", self.anio_nacimiento)


def main():
    persona1 = Persona("Juan", "Pérez", "1012345678", 1995)
    persona2 = Persona("María", "Gómez", "1098765432", 2000)

    print("Datos de la primera persona")
    persona1.mostrar_datos()

    print()
    print("Datos de la segunda persona")
    persona2.mostrar_datos()


main()
