import math

class Figura:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color, "Círculo")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color, "Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo(Figura):
    def __init__(self, color, base, altura, lado):
        super().__init__(color, "Triángulo")
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.lado * 3

# Ejemplo
circulo = Circulo("Rojo", 5)
print("Área del círculo:", circulo.calcular_area())
