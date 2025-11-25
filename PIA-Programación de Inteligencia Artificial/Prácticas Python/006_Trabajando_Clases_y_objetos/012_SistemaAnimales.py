class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Sonido genérico de animal")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau 🐕")

    def correr(self):
        print(f"{self.nombre} está corriendo 🏃‍♂️")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau 😺")

class Pajaro(Animal):
    def hacer_sonido(self):
        print("Pío pío 🐦")

    def volar(self):
        print(f"{self.nombre} está volando ✈️")

# Ejemplo
print("-----------------")
perro = Perro("Rocky", 3)
perro.hacer_sonido()
perro.correr()

print("-----------------")
gato = Gato("Oc", 33)
gato.hacer_sonido()

print("-----------------")
perro = Pajaro("Nano",2)
perro.hacer_sonido()
perro.volar()