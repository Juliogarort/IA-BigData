# Clase Pelota
class Pelota:
    def __init__(self, deporte, tamaño, presion):
        self.deporte = deporte
        self.tamaño = tamaño
        self.presion = float(presion)

    def inflar(self, cantidad):
        self.presion += cantidad
        return f"Pelota inflada. Presión actual: {self.presion:.2f}"

    def desinflar(self, cantidad):
        self.presion = max(0.0, self.presion - cantidad)
        return f"Pelota desinflada. Presión actual: {self.presion:.2f}"

    def estado_presion(self):
        if self.presion < 0.5:
            return "La pelota está desinflada."
        elif self.presion > 1.5:
            return "La pelota está demasiado inflada."
        else:
            return "La presión de la pelota es correcta."

# Ejemplo
pel = Pelota("fútbol", "grande", 1.0)
print(pel.inflar(0.3))
print(pel.estado_presion())
print(pel.desinflar(1.0))
print(pel.estado_presion())
