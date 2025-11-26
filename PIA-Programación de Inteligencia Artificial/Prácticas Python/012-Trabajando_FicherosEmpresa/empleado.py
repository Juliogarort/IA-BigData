from typing import final


class Empleado:

    
    # Variable de clase para generar números únicos de empleado
    _contador_empleados = 0
    
    def __init__(self, empresa, nombre: str, sueldo: int):

        self._empresa = empresa
        self._nombre = nombre
        self._sueldo = sueldo
        
        # Generar número único de empleado
        Empleado._contador_empleados += 1
        self._num_empleado = Empleado._contador_empleados
    
    # Métodos de acceso (getters)
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_sueldo(self) -> int:
        return self._sueldo
    
    def get_num_empleado(self) -> int:
        return self._num_empleado
    
    # Métodos modificadores (setters)
    def set_nombre(self, nombre: str):

        self._nombre = nombre
    
    def set_sueldo(self, sueldo: int):

        self._sueldo = sueldo
    
    def __str__(self) -> str:

        return f"Empleado #{self._num_empleado}: {self._nombre} - Sueldo: ${self._sueldo:,}"
    
    @final
    def aumentar_sueldo(self, porcentaje: float):

        aumento = self._sueldo * (porcentaje / 100)
        self._sueldo += int(aumento)
        print(f"[OK] Sueldo de {self._nombre} aumentado en {porcentaje}%. Nuevo sueldo: ${self._sueldo:,}")
    
    def despedir(self):

        # Buscar la posición del empleado en la empresa
        for i in range(self._empresa.get_tamaño()):
            empleado = self._empresa.get_empleado(i)
            if empleado is not None and empleado.get_num_empleado() == self._num_empleado:
                self._empresa.despide_empleado(i)
                print(f"[OK] Empleado {self._nombre} (#{self._num_empleado}) ha sido despedido")
                return
        
        print(f"[X] No se encontró al empleado {self._nombre} en la empresa")
