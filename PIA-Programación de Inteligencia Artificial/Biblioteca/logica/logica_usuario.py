import csv
import os
from modelos.usuario import Usuario

DIRECTORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_CSV_USUARIOS = os.path.join(DIRECTORIO_BASE, "datos", "biblioUsuarios.csv")


def leer_usuarios():
# Lee los usuarios del csv

    if not os.path.exists(RUTA_CSV_USUARIOS):
        return []
    
    usuarios = []
    try:
        with open(RUTA_CSV_USUARIOS, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuario = Usuario.desde_diccionario(fila)
                usuarios.append(usuario)
    except Exception as e:
        print(f"Error al leer usuarios: {e}")
    
    return usuarios


def guardar_usuarios(usuarios):
# Guarda los usuarios en el csv
    try:
        with open(RUTA_CSV_USUARIOS, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['id_usuario', 'nombre', 'apellidos', 'dni', 'correo_e', 'tlfno', 'direccion', 'edad']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for usuario in usuarios:
                escritor.writerow(usuario.a_diccionario())
        print("✓ Datos guardados correctamente")
    except Exception as e:
        print(f"Error al guardar usuarios: {e}")


def generar_id_usuario():
# Genera un ID único para un nuevo usuario
    usuarios = leer_usuarios()
    if not usuarios:
        return "1"
    
    numeros = []
    for usuario in usuarios:
        try:
            numero = int(usuario.id_usuario)
            numeros.append(numero)
        except:
            pass
    
    if numeros:
        nuevo_numero = max(numeros) + 1
    else:
        nuevo_numero = 1
    
    return str(nuevo_numero)


def buscar_usuario_por_id(id_usuario):
# Busca un usuario por su ID

    usuarios = leer_usuarios()
    for usuario in usuarios:
        if usuario.id_usuario == id_usuario:
            return usuario
    return None


def alta_usuario():
# Registra un nuevo usuario en el sistema
    print("\n=== ALTA DE USUARIO ===")
    
    id_usuario = generar_id_usuario()
    print(f"ID asignado automáticamente: {id_usuario}")
    
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío")
        return
    
    apellidos = input("Apellidos: ").strip()
    dni = input("DNI: ").strip()
    correo_e = input("Correo electrónico: ").strip()
    tlfno = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()
    edad = input("Edad: ").strip()
    
    nuevo_usuario = Usuario(id_usuario, nombre, apellidos, dni, correo_e, tlfno, direccion, edad)
    
    usuarios = leer_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    
    print(f"\n✓ Usuario '{nombre} {apellidos}' registrado correctamente con ID {id_usuario}")


def baja_usuario():
# Elimina un usuario del sistema
    print("\n=== BAJA DE USUARIO ===")
    
    usuarios = leer_usuarios()
    if not usuarios:
        print("No hay usuarios registrados en el sistema")
        return
    
    print("\nUsuarios registrados:")
    for usuario in usuarios:
        print(f"  {usuario}")
    
    id_usuario = input("\nIngrese el ID del usuario a dar de baja (o 'cancelar' para volver): ").strip()
    
    if id_usuario.lower() == 'cancelar':
        return
    
    usuario_encontrado = None
    indice_usuario = -1
    for i, usuario in enumerate(usuarios):
        if usuario.id_usuario == id_usuario:
            usuario_encontrado = usuario
            indice_usuario = i
            break
    
    if not usuario_encontrado:
        print(f"Error: No se encontró ningún usuario con ID {id_usuario}")
        return
    
# Mostrar datos del usuario a eliminar
    print(f"\nUsuario seleccionado:")
    print(f"  ID: {usuario_encontrado.id_usuario}")
    print(f"  Nombre: {usuario_encontrado.nombre} {usuario_encontrado.apellidos}")
    print(f"  DNI: {usuario_encontrado.dni}")
    print(f"  Correo: {usuario_encontrado.correo_e}")
    print(f"  Teléfono: {usuario_encontrado.tlfno}")
    
# Pedir confirmación
    confirmacion = input("\n¿Está seguro de que desea dar de baja a este usuario? (si/no): ").strip().lower()
    
    if confirmacion in ['si', 'sí', 's', 'yes', 'y']:
# Eliminar el usuario de la lista
        usuarios.pop(indice_usuario)
        guardar_usuarios(usuarios)
        print(f"\n✓ Usuario '{usuario_encontrado.nombre} {usuario_encontrado.apellidos}' dado de baja correctamente")
    else:
        print("\nOperación cancelada. El usuario no ha sido eliminado.")


def modificar_usuario():
# Modifica el usuario que el usuario seleccione mediante su id

    print("\n=== MODIFICAR USUARIO ===")
    
# Mostramos los usuarios disponibles
    usuarios = leer_usuarios()
    if not usuarios:
        print("No hay usuarios registrados en el sistema")
        return
    
    print("\nUsuarios registrados:")
    for usuario in usuarios:
        print(f"  {usuario}")
    
# Solicitamos el ID del usuario a modificar
    id_usuario = input("\nIngrese el ID del usuario a modificar (o 'cancelar' para volver): ").strip()
    
    if id_usuario.lower() == 'cancelar':
        return
    
# Buscamos el usuario
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.id_usuario == id_usuario:
            usuario_encontrado = usuario
            break
    
    if not usuario_encontrado:
        print(f"Error: No se encontró ningún usuario con ID {id_usuario}")
        return
    
# Mostramos los datos actuales
    print(f"\nDatos actuales del usuario '{usuario_encontrado.nombre} {usuario_encontrado.apellidos}':")
    print(f"1. Nombre: {usuario_encontrado.nombre}")
    print(f"2. Apellidos: {usuario_encontrado.apellidos}")
    print(f"3. DNI: {usuario_encontrado.dni}")
    print(f"4. Correo electrónico: {usuario_encontrado.correo_e}")
    print(f"5. Teléfono: {usuario_encontrado.tlfno}")
    print(f"6. Dirección: {usuario_encontrado.direccion}")
    print(f"7. Edad: {usuario_encontrado.edad}")
    
# Solicitamos qué campo modificar
    print("\n¿Qué campo desea modificar? (1-7, o 0 para cancelar)")
    opcion = input("Opción: ").strip()
    
    if opcion == "0":
        return
    elif opcion == "1":
        nuevo_valor = input("Nuevo nombre: ").strip()
        if nuevo_valor:
            usuario_encontrado.nombre = nuevo_valor
    elif opcion == "2":
        nuevo_valor = input("Nuevos apellidos: ").strip()
        if nuevo_valor:
            usuario_encontrado.apellidos = nuevo_valor
    elif opcion == "3":
        nuevo_valor = input("Nuevo DNI: ").strip()
        if nuevo_valor:
            usuario_encontrado.dni = nuevo_valor
    elif opcion == "4":
        nuevo_valor = input("Nuevo correo electrónico: ").strip()
        if nuevo_valor:
            usuario_encontrado.correo_e = nuevo_valor
    elif opcion == "5":
        nuevo_valor = input("Nuevo teléfono: ").strip()
        if nuevo_valor:
            usuario_encontrado.tlfno = nuevo_valor
    elif opcion == "6":
        nuevo_valor = input("Nueva dirección: ").strip()
        if nuevo_valor:
            usuario_encontrado.direccion = nuevo_valor
    elif opcion == "7":
        nuevo_valor = input("Nueva edad: ").strip()
        if nuevo_valor:
            usuario_encontrado.edad = nuevo_valor
    else:
        print("Opción no válida")
        return
    
# Guardamos los cambios
    guardar_usuarios(usuarios)
    print("\n✓ Usuario modificado correctamente")


def listar_usuarios():
# Muestra un listado de todos los usuarios registrados
    print("\n=== LISTADO DE USUARIOS ===")
    
    usuarios = leer_usuarios()
    
    if not usuarios:
        print("No hay usuarios registrados en el sistema")
        return
    
    print(f"\nTotal de usuarios: {len(usuarios)}\n")
    
    for usuario in usuarios:
        print(f"  {usuario}")
    
    print()