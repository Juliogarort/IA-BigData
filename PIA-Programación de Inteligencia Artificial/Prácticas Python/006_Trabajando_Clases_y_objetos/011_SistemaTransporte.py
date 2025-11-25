class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Coche(Vehiculo):
    def acelerar(self):
        print("El coche está acelerando 🚗💨")

    def frenar(self):
        print("El coche está frenando 🛑")

class Motocicleta(Vehiculo):
    def tocar_claxon(self):
        print("¡Piiiiip! 🏍️")

class Bicicleta(Vehiculo):
    def pedalear(self):
        print("Pedaleando la bicicleta 🚴‍♂️")

# Ejemplo
bici = Bicicleta("Orbea", "MX40", 2021)
bici.pedalear()
print(bici.mostrar_info())
coche = Coche("Ferrari", "812 Competizione", 2020)
coche.frenar()
print(coche.mostrar_info())