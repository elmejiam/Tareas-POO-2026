class Persona:
    def __init__(self, nombre, edad=0):
        self.nombre = nombre
        self.edad = edad

class Familia:
    def __init__(self, edad_juan):
        self.juan = Persona("Juan", edad_juan)
        self.alberto = Persona("Alberto", (2/3) * self.juan.edad)
        self.ana = Persona("Ana", (4/3) * self.juan.edad)
        self.mama = Persona("Mamá", self.juan.edad + self.alberto.edad + self.ana.edad)

    def mostrar_edades(self):
        print(f"{self.alberto.nombre}: {self.alberto.edad:.2f} años")
        print(f"{self.juan.nombre}: {self.juan.edad:.2f} años")
        print(f"{self.ana.nombre}: {self.ana.edad:.2f} años")
        print(f"{self.mama.nombre}: {self.mama.edad:.2f} años")
        
edad_juan = int(input("Ingrese la edad de Juan: "))
familia = Familia(edad_juan)
familia.mostrar_edades()