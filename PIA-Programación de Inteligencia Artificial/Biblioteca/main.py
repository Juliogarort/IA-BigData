# Importaciones de los módulos de lógica
import os
import shutil
from logica import logica_libro
from logica import logica_usuario
from logica import logica_prestamo


def mostrar_bienvenida():
    print(" "*10 + "SISTEMA DE GESTIÓN DE BIBLIOTECA")



def inicializar_sistema():
# Crea copias temporales de los archivos CSV para trabajar sobre ellas.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    datos_dir = os.path.join(base_dir, "datos")
    
    archivos = [
        ("biblioLibros.csv", "biblioLibros_temp.csv"),
        ("biblioUsuarios.csv", "biblioUsuarios_temp.csv"),
        ("biblioPrestamos.csv", "biblioPrestamos_temp.csv")
    ]
    
    for original, temporal in archivos:
        ruta_original = os.path.join(datos_dir, original)
        ruta_temporal = os.path.join(datos_dir, temporal)
        
        if os.path.exists(ruta_original):
            shutil.copy2(ruta_original, ruta_temporal)
        else:
            print(f"  ⚠ Advertencia: No se encuentra {original}")


def menu_principal():

    inicializar_sistema()
    mostrar_bienvenida()
    
    while True:
        print("\n" + "="*60)
        print("MENÚ PRINCIPAL")
        print("="*60)
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Registrar Préstamo")
        print("4. Registrar Devolución")
        print("5. Listados de Préstamos")
        print("6. Salir")
        print("="*60)
        
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            gestion_libros()
            
        elif opcion == "2":
            gestion_usuarios()
            
        elif opcion == "3":
            registrar_prestamo()
            
        elif opcion == "4":
            registrar_devolucion()
            
        elif opcion == "5":
            menu_listados_prestamos()
            
        elif opcion == "6":
            # Salir de la aplicación
            print("\n" + "="*60)
            print("Gracias por usar el Sistema de Gestión de Biblioteca")
            print("¡Hasta pronto!")
            print("="*60 + "\n")
            break
            
        else:
            print("\n⚠ Opción no válida. Por favor, seleccione una opción del 1 al 6")


def gestion_libros():
    while True:
        print("\n" + "="*50)
        print("GESTIÓN DE LIBROS")
        print("="*50)
        print("1. Alta de libro")
        print("2. Baja de libro")
        print("3. Modificar libro")
        print("4. Listar libros")
        print("5. Volver al menú principal")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            logica_libro.alta_libro()
            
        elif opcion == "2":
            logica_libro.baja_libro()
            
        elif opcion == "3":
            logica_libro.modificar_libro()
            
        elif opcion == "4":
            logica_libro.listar_libros()
            
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5")


def gestion_usuarios():

    while True:
        print("\n" + "="*50)
        print("GESTIÓN DE USUARIOS")
        print("="*50)
        print("1. Alta de usuario")
        print("2. Baja de usuario")
        print("3. Modificar usuario")
        print("4. Listar usuarios")
        print("5. Volver al menú principal")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            logica_usuario.alta_usuario()
            
        elif opcion == "2":
            logica_usuario.baja_usuario()
            
        elif opcion == "3":
            logica_usuario.modificar_usuario()
            
        elif opcion == "4":
            logica_usuario.listar_usuarios()
            
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5")


def registrar_prestamo():
    logica_prestamo.registrar_prestamo()


def registrar_devolucion():
    logica_prestamo.registrar_devolucion()


def menu_listados_prestamos():

    while True:
        print("\n" + "="*50)
        print("LISTADOS DE PRÉSTAMOS")
        print("="*50)
        print("1. Préstamos pendientes")
        print("2. Historial completo de préstamos")
        print("3. Volver al menú principal")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            logica_prestamo.listar_prestamos_pendientes()
            
        elif opcion == "2":
            logica_prestamo.listar_todos_prestamos()
            
        elif opcion == "3":
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3")


if __name__ == "__main__":

    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n" + "="*60)
        print("Aplicación cerrada por el usuario")
        print("="*60 + "\n")
    except Exception as e:
        print(f"\n⚠ Error inesperado: {e}")
        print("Por favor, contacte con el administrador del sistema\n")