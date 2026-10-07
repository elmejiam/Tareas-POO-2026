from enum import Enum


class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"


class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0  # toda cuenta nueva inicia con saldo cero

    def mostrar_datos(self):
        print("Nombres del titular:", self.nombres)
        print("Apellidos del titular:", self.apellidos)
        print("Número de cuenta:", self.numero_cuenta)
        print("Tipo de cuenta:", self.tipo_cuenta.value)
        print("Saldo:", self.saldo)

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, valor):
        if valor <= 0:
            print("El valor a consignar debe ser mayor que cero")
        else:
            self.saldo = self.saldo + valor
            print("Consignación exitosa. Nuevo saldo:", self.saldo)

    def retirar(self, valor):
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero")
        elif valor > self.saldo:
            print("No se puede realizar el retiro: el valor supera el saldo actual")
        else:
            self.saldo = self.saldo - valor
            print("Retiro exitoso. Nuevo saldo:", self.saldo)


def main():
    cuenta1 = CuentaBancaria("Juan Carlos", "Pérez Gómez", "123456789",
                             TipoCuenta.AHORROS)
    cuenta2 = CuentaBancaria("María Fernanda", "López Ruiz", "987654321",
                             TipoCuenta.CORRIENTE)

    print("--- Cuenta 1 ---")
    cuenta1.mostrar_datos()
    cuenta1.consignar(500000)
    cuenta1.retirar(200000)
    cuenta1.retirar(400000)  # supera el saldo, no se permite
    print("Saldo actual:", cuenta1.consultar_saldo())

    print()
    print("--- Cuenta 2 ---")
    cuenta2.mostrar_datos()
    cuenta2.consignar(1000000)
    cuenta2.retirar(300000)
    print("Saldo actual:", cuenta2.consultar_saldo())


main()
