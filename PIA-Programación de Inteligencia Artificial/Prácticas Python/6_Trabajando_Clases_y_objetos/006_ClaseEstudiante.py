class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = []

    def anadir_nota(self, nota):
        self.notas.append(float(nota))
        return f"Nota {nota} añadida."

    def promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        promedio = self.promedio()
        if promedio >= 5:
            return f"{self.nombre} ha aprobado con una media de {promedio:.2f}."
        else:
            return f"{self.nombre} ha suspendido con una media de {promedio:.2f}."

e = Estudiante("Oc", "2º DAW")
print(e.anadir_nota(6))
print(e.anadir_nota(4))
print(e.anadir_nota(7))
print(e.aprobado())
