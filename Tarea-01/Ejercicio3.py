class Empleado:
    def __init__(self, horas_trabajadas=48, valor_hora=5000, porcentaje_retencion=12.5):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular_salarios(self):
        self.salario_bruto = self.horas_trabajadas * self.valor_hora
        self.retencion = (self.porcentaje_retencion / 100) * self.salario_bruto
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_resultado(self):
        print(f"Salario Bruto: ${self.salario_bruto:,.0f}")
        print(f"Retención en la fuente (12.5%): ${self.retencion:,.0f}")
        print(f"Salario Neto: ${self.salario_neto:,.0f}")
        
empleado = Empleado()
empleado.calcular_salarios()
empleado.mostrar_resultado()