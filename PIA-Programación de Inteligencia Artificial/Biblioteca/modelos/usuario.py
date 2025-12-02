class Usuario:
# Clase que declara la estructura y atributos de usuarios
    
    def __init__(self, id_usuario, nombre, apellidos, dni, correo_e, tlfno, direccion, edad):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.correo_e = correo_e
        self.tlfno = tlfno
        self.direccion = direccion
        self.edad = edad
    
    def a_diccionario(self):
# Obtiene los datos del csv
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'dni': self.dni,
            'correo_e': self.correo_e,
            'tlfno': self.tlfno,
            'direccion': self.direccion,
            'edad': self.edad
        }
    
    @staticmethod
    def desde_diccionario(datos):
# Mediante el objeto del csv crea los usuarios
        return Usuario(
            datos['id_usuario'],
            datos['nombre'],
            datos['apellidos'],
            datos['dni'],
            datos['correo_e'],
            datos['tlfno'],
            datos['direccion'],
            datos['edad']
        )
    
    def __str__(self):
# Se muestran los datos del usuario
        return (f"ID: {self.id_usuario} | {self.nombre} {self.apellidos} | "
                f"DNI: {self.dni} | Tel: {self.tlfno} | Email: {self.correo_e}")
