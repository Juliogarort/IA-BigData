from datetime import datetime

class Prestamo:
    # Clase que declara la estructura y atributos de prestamos
    
    def __init__(self, id_prestamo, id_usuario, id_libro, fecha_inicio, fecha_fin, fecha_devolucion=""):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_devolucion = fecha_devolucion
    
    def a_diccionario(self):
# Obtiene los datos del csv

        return {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'fecha_devolucion': self.fecha_devolucion
        }
    
    @staticmethod
    def desde_diccionario(datos):
# Mediante el objeto del csv crea los prestamos

        return Prestamo(
            datos['id_prestamo'],
            datos['id_usuario'],
            datos['id_libro'],
            datos['fecha_inicio'],
            datos['fecha_fin'],
            datos.get('fecha_devolucion', '')
        )
    
    def esta_pendiente(self):
#  Comprueba si el prestamo esta pendiente de devolucion

        return self.fecha_devolucion == "" or self.fecha_devolucion is None or self.fecha_devolucion == "."
    
    def __str__(self):  
#  Muestra los datos del prestamo

        estado = "PENDIENTE" if self.esta_pendiente() else f"Devuelto el {self.fecha_devolucion}"
        return (f"ID: {self.id_prestamo} | Usuario: {self.id_usuario} | "
                f"Libro: {self.id_libro} | Inicio: {self.fecha_inicio} | "
                f"Fin: {self.fecha_fin} | Estado: {estado}")
