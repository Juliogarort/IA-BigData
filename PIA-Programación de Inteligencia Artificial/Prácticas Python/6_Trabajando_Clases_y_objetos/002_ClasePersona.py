class Persona:
    def __init__(self, nombre, edad, genero, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura

    def saludar(self, otra_persona):
        return f"{self.nombre} saluda a {otra_persona}."

    def es_mayor(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} es menor de edad."

    def edad_en_5_anos(self):
        return f"En 5 años, {self.nombre} tendrá {self.edad + 5} años."

p = Persona("Ana", 17, "F", 1.65)
print(p.saludar("Luis"))
print(p.es_mayor())
print(p.edad_en_5_anos())
