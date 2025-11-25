class Cafetera:
    def __init__(self, marca, capacidad_litros):
        self.marca = marca
        self.capacidad = float(capacidad_litros)
        self.nivel = 0.0

    def servir(self, cantidad_litros):
        if cantidad_litros <= 0:
            return "Cantidad inválida."
        if self.nivel == 0:
            return "No hay café disponible."
        servido = min(self.nivel, cantidad_litros)
        self.nivel -= servido
        return f"Servidos {servido:.2f}L de café. Nivel restante: {self.nivel:.2f}L."

    def rellenar(self):
        self.nivel = self.capacidad
        return "Cafetera rellenada al máximo."

    def estado(self):
        if self.nivel == 0:
            return "La cafetera está vacía."
        elif self.nivel == self.capacidad:
            return "La cafetera está llena."
        else:
            return f"La cafetera tiene {self.nivel:.2f}L."

caf = Cafetera("Nespresso", 1.5)
print(caf.rellenar())
print(caf.servir(0.2))
print(caf.estado())
