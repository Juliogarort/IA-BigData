class Smartphone:
    def __init__(self, marca, modelo, memoria_gb, bateria_max=100):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria_gb
        self.bateria_max = bateria_max
        self.bateria = bateria_max

    def llamar(self, minutos):
        consumo = minutos * 0.5
        if self.bateria <= 0:
            return "El móvil está apagado por falta de batería."
        self.bateria = max(0, self.bateria - consumo)
        return f"Llamada de {minutos} minutos realizada. Batería restante: {self.bateria:.1f}%"

    def cargar(self, porcentaje):
        self.bateria = min(self.bateria_max, self.bateria + porcentaje)
        return f"Batería cargada al {self.bateria:.1f}%"

    def nivel_bateria(self):
        return f"Nivel de batería actual: {self.bateria:.1f}%"

s = Smartphone("Nothing", "Phone 2", 256)
print(s.llamar(30))
print(s.cargar(20))
print(s.nivel_bateria())
