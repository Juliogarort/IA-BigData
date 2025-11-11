class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, cantidad, consumo_energetico):
        super().__init__(nombre, precio, cantidad)
        self.consumo_energetico = consumo_energetico

    def calcular_total(self):
        return self.precio * self.cantidad

class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def calcular_total(self):
        total = self.precio * self.cantidad
        if self.cantidad >= 3:
            total *= 0.9  # 10% de descuento
        return total

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_vencimiento = fecha_vencimiento

    def calcular_total(self):
        return self.precio * self.cantidad

# Ejemplo
ropa = Ropa("Camiseta", 20, 4, "M")
print("Total con descuento:", ropa.calcular_total())
electrodomestico = Electrodomestico("Televisor", 500, 1, "A++")
print("Total electrodoméstico:", electrodomestico.calcular_total())
alimento = Alimento("Leche", 1.5, 10, "2024-12-31")
print("Total alimento:", alimento.calcular_total())
