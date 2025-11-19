import json
import re
import os
from datetime import datetime

# Obtener la ruta del directorio donde está este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Función para cargar datos desde un archivo JSON
def cargar_datos(nombre_archivo):
    """
    Abre y carga el contenido de un archivo JSON.
    """
    # Crear la ruta completa del archivo
    ruta_completa = os.path.join(BASE_DIR, nombre_archivo)
    
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo} en {BASE_DIR}")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {nombre_archivo} no tiene un formato JSON válido")
        return None

# Patrones de expresiones regulares para validar alumnos
patron_email = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
patron_telefono = r'^[679]\d{8}$'
patron_codigo_postal = r'^\d{5}$'

# Patrones de expresiones regulares para validar vehículos
patron_matricula = r'^\d{4}[A-Z]{3}$'
patron_ano = r'^(19\d{2}|20[0-2][0-5])$'  # Años entre 1900 y 2025

def validar_alumno(alumno):
    """
    Valida los datos de un alumno usando expresiones regulares.
    """
    print(f"\n--- Validando alumno: {alumno['nombre']} ---")
    
    # Validar email
    if re.match(patron_email, alumno['email']):
        print(f"✓ Email válido: {alumno['email']}")
    else:
        print(f"✗ Email inválido: {alumno['email']}")
    
    # Validar teléfono
    if re.match(patron_telefono, alumno['telefono']):
        print(f"✓ Teléfono válido: {alumno['telefono']}")
    else:
        print(f"✗ Teléfono inválido: {alumno['telefono']} (debe empezar por 6, 7 o 9 y tener 9 dígitos)")
    
    # Validar código postal
    if re.match(patron_codigo_postal, alumno['codigo_postal']):
        print(f"✓ Código postal válido: {alumno['codigo_postal']}")
    else:
        print(f"✗ Código postal inválido: {alumno['codigo_postal']} (debe tener 5 dígitos)")

def validar_vehiculo(vehiculo):
    """
    Valida los datos de un vehículo usando expresiones regulares.
    """
    print(f"\n--- Validando vehículo: {vehiculo['marca']} {vehiculo['modelo']} ---")
    
    # Validar matrícula
    if re.match(patron_matricula, vehiculo['matricula']):
        print(f"✓ Matrícula válida: {vehiculo['matricula']}")
    else:
        print(f"✗ Matrícula inválida: {vehiculo['matricula']} (formato: 1234ABC)")
    
    # Validar año
    if re.match(patron_ano, vehiculo['año']):
        print(f"✓ Año válido: {vehiculo['año']}")
    else:
        print(f"✗ Año inválido: {vehiculo['año']} (debe estar entre 1900 y 2025)")
    
    # Validar email del propietario
    if re.match(patron_email, vehiculo['propietario_email']):
        print(f"✓ Email del propietario válido: {vehiculo['propietario_email']}")
    else:
        print(f"✗ Email del propietario inválido: {vehiculo['propietario_email']}")

# Programa principal
def main():
    print("=" * 60)
    print("VALIDACIÓN DE DATOS CON EXPRESIONES REGULARES")
    print("=" * 60)
    
    # Cargar y validar alumnos
    print("\n\n### VALIDACIÓN DE ALUMNOS ###")
    alumnos = cargar_datos('alumnos.json')
    
    if alumnos:
        for alumno in alumnos:
            validar_alumno(alumno)
    
    # Cargar y validar vehículos
    print("\n\n### VALIDACIÓN DE VEHÍCULOS ###")
    vehiculos = cargar_datos('vehiculos.json')
    
    if vehiculos:
        for vehiculo in vehiculos:
            validar_vehiculo(vehiculo)
    
    print("\n" + "=" * 60)
    print("VALIDACIÓN COMPLETADA")
    print("=" * 60)

# Ejecutar el programa
if __name__ == "__main__":
    main()