import hashlib
import json
import os
 
class Bloque:

    # Añadimos cantidad  para representar el valor de cada transación
    # tambien lo añadimos en el resto de funciones como en calcular_hash, mostrar_info, agregar_bloque y mostrar_transacciones. 
    def __init__(self, id, emisor, receptor, mensaje, cantidad, hash_anterior=""):
        self.id = id
        self.emisor = emisor
        self.receptor = receptor
        self.mensaje = mensaje
        self.cantidad = cantidad
        self.hash_anterior = hash_anterior
        self.hash = self.calcular_hash()
 
    # Calculamos el hash para asegurar la integridad del bloque. 
    def calcular_hash(self):
        contenido = f"{self.id}{self.emisor}{self.receptor}{self.mensaje}{self.cantidad}{self.hash_anterior}"
        return hashlib.sha256(contenido.encode()).hexdigest()
 
    def mostrar_info(self):
        return {
        "id": self.id,
        "emisor": self.emisor,
        "receptor": self.receptor,
        "mensaje": self.mensaje,
        "cantidad": self.cantidad,
        "hash_anterior": self.hash_anterior,
        "hash": self.hash
    }
 
class Blockchain:
    def __init__(self):
        self.cadena = [self.crear_bloque_genesis()]
 
    def crear_bloque_genesis(self):
        return Bloque(0, "GENESIS", "TODOS", "Inicio de la cadena", 0, "0") 


    def agregar_bloque(self, emisor, receptor, mensaje, cantidad):
        ultimo_bloque = self.cadena[-1]
        nuevo_bloque = Bloque(len(self.cadena), emisor, receptor, mensaje, cantidad, ultimo_bloque.hash)
        self.cadena.append(nuevo_bloque)
 
    #Verificamos que no se modifique ningun bloque ni su encadenamiento
    def es_valida(self):
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]
 
            if bloque_actual.hash != bloque_actual.calcular_hash():
                return False
            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return False
        return True
 
    # Mostramos las transacciones sin el hash ni datos tecnicos
    def mostrar_transacciones(self):
        for bloque in self.cadena[1:]:  
            print(f"{bloque.emisor} → {bloque.receptor}: {bloque.mensaje} ({bloque.cantidad}€)")   

    # Guardamos el archivo en formato JSON
    def guardar_en_json(self, nombre_archivo):
        datos = [bloque.mostrar_info() for bloque in self.cadena]
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
        with open(ruta, 'w') as f:
            json.dump(datos, f, indent=4)
    
        print(f"Archivo guardado en: {ruta}")
 

bc = Blockchain()

bc.agregar_bloque("Alice", "Bob", "Pago", 50)
bc.agregar_bloque("Bob", "Carol", "Transferencia", 30)
bc.agregar_bloque("Carol", "Dave", "Deuda", 20)

print((""))
print("VALIDACIÓN INICIAL")
print("¿Blockchain válida?", bc.es_valida())

bc.cadena[1].mensaje = "MENSAJE ALTERADO"

print((""))
print("VALIDACIÓN TRAS MODIFICACIÓN")
print("¿Blockchain válida después de modificar?", bc.es_valida())
print((""))

print("Transacciones realizadas: ")
bc.mostrar_transacciones()
print((""))

bc.guardar_en_json("cadena_blockchain.json")