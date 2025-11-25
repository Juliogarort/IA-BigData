class CuentaBancaria:
    def __init__(self, titular, saldo=0.0, tipo="corriente"):
        self.titular = titular
        self.saldo = float(saldo)
        self.tipo = tipo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito realizado. Nuevo saldo: {self.saldo:.2f}€"
        else:
            return "Cantidad inválida."

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "Cantidad no válida para retirar."
        if cantidad > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= cantidad
        return f"Retiro realizado. Nuevo saldo: {self.saldo:.2f}€"

    def mostrar_saldo(self):
        return f"Saldo de {self.titular}: {self.saldo:.2f}€"

c = CuentaBancaria("María", 100)
print(c.depositar(50))
print(c.retirar(200))
print(c.retirar(120))
print(c.mostrar_saldo())
