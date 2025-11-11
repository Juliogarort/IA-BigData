class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso):
        super().__init__(nombre, edad, genero)
        self.curso = curso

    def estudiar(self):
        print(f"{self.nombre} está estudiando 📚")

    def informacion(self):
        return super().informacion() + f", Curso: {self.curso}"

class Profesor(Persona):
    def __init__(self, nombre, edad, genero, asignatura):
        super().__init__(nombre, edad, genero)
        self.asignatura = asignatura

    def enseñar(self):
        print(f"{self.nombre} está enseñando {self.asignatura} 👨‍🏫")

    def informacion(self):
        return super().informacion() + f", Asignatura: {self.asignatura}"

class Director(Persona):
    def __init__(self, nombre, edad, genero, años_experiencia):
        super().__init__(nombre, edad, genero)
        self.años_experiencia = años_experiencia

    def supervisar(self):
        print(f"{self.nombre} está supervisando la institución 🏫")

    def informacion(self):
        return super().informacion() + f", Años de experiencia: {self.años_experiencia}"

# Ejemplo
profe = Profesor("Laura", 35, "Femenino", "Matemáticas")
print(profe.informacion())
profe.enseñar()
est = Estudiante("Carlos", 20, "Masculino", "Ingeniería")
print(est.informacion())
est.estudiar()
dir = Director("Ana", 50, "Femenino", 25)
print(dir.informacion())
dir.supervisar()