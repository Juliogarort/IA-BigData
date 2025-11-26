import pickle
import os
from empleado import Empleado


class Empresa:

    
    # Obtener la ruta del directorio donde está este archivo
    _DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
    ARCHIVO_EMPLEADOS = os.path.join(_DIRECTORIO_ACTUAL, "MisEmpleados.dat")
    
    def __init__(self, nombre: str, tamaño: int):

        self.__nombre = nombre
        self.__tamaño = tamaño
        self.__empleados = [None] * tamaño  # Lista con tamaño fijo
    
    # Métodos de acceso (getters)
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_tamaño(self) -> int:
        return self.__tamaño
    
    def get_empleado(self, indice: int):

        if 0 <= indice < self.__tamaño:
            return self.__empleados[indice]
        else:
            raise IndexError(f"Índice {indice} fuera de rango (0-{self.__tamaño-1})")
    
    def despide_empleado(self, indice: int):

        if 0 <= indice < self.__tamaño:
            if self.__empleados[indice] is not None:
                self.__empleados[indice] = None
                self.guardar_empleados()
            else:
                print(f"[X] La posición {indice} ya está vacía")
        else:
            raise IndexError(f"Índice {indice} fuera de rango (0-{self.__tamaño-1})")
    
    def nuevo_empleado(self, nombre: str, sueldo: int):

        # Buscar primera posición disponible
        for i in range(self.__tamaño):
            if self.__empleados[i] is None:
                nuevo_emp = Empleado(self, nombre, sueldo)
                self.__empleados[i] = nuevo_emp
                self.guardar_empleados()
                print(f"[OK] Empleado {nombre} añadido en posición {i}")
                return nuevo_emp
        
        print(f"[X] No hay espacio disponible en la empresa (capacidad máxima: {self.__tamaño})")
        return None
    
    def guardar_empleados(self):

        # Crear lista de datos de empleados (sin None)
        datos_empleados = []
        for empleado in self.__empleados:
            if empleado is not None:
                datos_empleados.append({
                    'nombre': empleado.get_nombre(),
                    'sueldo': empleado.get_sueldo(),
                    'num_empleado': empleado.get_num_empleado()
                })
        
        # Guardar en archivo usando pickle
        try:
            with open(self.ARCHIVO_EMPLEADOS, 'wb') as archivo:
                pickle.dump(datos_empleados, archivo)
            print(f"[GUARDADO] Datos guardados en {self.ARCHIVO_EMPLEADOS}")
        except Exception as e:
            print(f"[X] Error al guardar empleados: {e}")
    
    def cargar_empleados(self):

        if not os.path.exists(self.ARCHIVO_EMPLEADOS):
            print(f"[INFO] No existe el archivo {self.ARCHIVO_EMPLEADOS}. Se creará uno nuevo.")
            return
        
        try:
            with open(self.ARCHIVO_EMPLEADOS, 'rb') as archivo:
                datos_empleados = pickle.load(archivo)
            
            # Reconstruir empleados
            posicion = 0
            for datos in datos_empleados:
                if posicion < self.__tamaño:
                    # Crear empleado sin incrementar contador (usar número guardado)
                    empleado = Empleado.__new__(Empleado)
                    empleado._empresa = self
                    empleado._nombre = datos['nombre']
                    empleado._sueldo = datos['sueldo']
                    empleado._num_empleado = datos['num_empleado']
                    
                    # Actualizar contador global si es necesario
                    if datos['num_empleado'] > Empleado._contador_empleados:
                        Empleado._contador_empleados = datos['num_empleado']
                    
                    self.__empleados[posicion] = empleado
                    posicion += 1
            
            print(f"[CARGADO] Cargados {len(datos_empleados)} empleados desde {self.ARCHIVO_EMPLEADOS}")
            
        except Exception as e:
            print(f"[X] Error al cargar empleados: {e}")
    
    def mostrar_empleados(self):
        
        print(f"\n{'='*60}")
        print(f"  EMPRESA: {self.__nombre}")
        print(f"  Capacidad: {self.__tamaño} empleados")
        print(f"{'='*60}")
        
        empleados_activos = 0
        for i, empleado in enumerate(self.__empleados):
            if empleado is not None:
                print(f"  [{i}] {empleado}")
                empleados_activos += 1
        
        if empleados_activos == 0:
            print("  (No hay empleados activos)")
        
        print(f"{'='*60}")
        print(f"  Total empleados activos: {empleados_activos}/{self.__tamaño}")
        print(f"{'='*60}\n")
