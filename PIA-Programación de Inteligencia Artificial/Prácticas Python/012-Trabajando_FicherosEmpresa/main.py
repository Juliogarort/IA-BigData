from empresa import Empresa


def mostrar_menu():
    print("\n" + "="*50)
    print("  MENU - GESTION DE EMPLEADOS")
    print("="*50)
    print("1. Ver todos los empleados")
    print("2. Dar de alta un empleado")
    print("3. Dar de baja un empleado")
    print("4. Aumentar sueldo a un empleado")
    print("5. Salir")
    print("="*50)


def main():
    
    print("\n" + "="*50)
    print("  SISTEMA DE GESTION DE EMPLEADOS")
    print("="*50 + "\n")
    
    # Crear empresa
    empresa = Empresa("Mi Empresa", 10)
    
    # Cargar empleados desde archivo
    print("[INFO] Cargando empleados desde archivo...")
    empresa.cargar_empleados()
    
    # Si no hay empleados, crear 5 iniciales
    if all(empresa.get_empleado(i) is None for i in range(empresa.get_tamaño())):
        print("\n[INFO] No hay empleados. Creando 5 empleados iniciales...\n")
        
        # Pedir datos de 5 empleados
        for i in range(5):
            print(f"--- Empleado {i+1} ---")
            nombre = input("Nombre: ")
            sueldo = int(input("Sueldo: "))
            empresa.nuevo_empleado(nombre, sueldo)
            print()
    
    # Menú principal
    while True:
        mostrar_menu()
        opcion = input("\nElige una opcion (1-5): ")
        
        if opcion == "1":
            # Ver empleados
            empresa.mostrar_empleados()
            
        elif opcion == "2":
            # Dar de alta
            print("\n--- DAR DE ALTA EMPLEADO ---")
            nombre = input("Nombre del empleado: ")
            sueldo = int(input("Sueldo: "))
            empresa.nuevo_empleado(nombre, sueldo)
            
        elif opcion == "3":
            # Dar de baja
            print("\n--- DAR DE BAJA EMPLEADO ---")
            empresa.mostrar_empleados()
            
            try:
                indice = int(input("\nIndice del empleado a despedir: "))
                empleado = empresa.get_empleado(indice)
                
                if empleado is not None:
                    confirmar = input(f"¿Seguro que quieres despedir a {empleado.get_nombre()}? (s/n): ")
                    if confirmar.lower() == 's':
                        empleado.despedir()
                    else:
                        print("[INFO] Operacion cancelada")
                else:
                    print("[ERROR] No hay empleado en esa posicion")
            except (ValueError, IndexError):
                print("[ERROR] Indice invalido")
        
        elif opcion == "4":
            # Aumentar sueldo
            print("\n--- AUMENTAR SUELDO ---")
            empresa.mostrar_empleados()
            
            try:
                indice = int(input("\nIndice del empleado: "))
                empleado = empresa.get_empleado(indice)
                
                if empleado is not None:
                    porcentaje = float(input("Porcentaje de aumento: "))
                    empleado.aumentar_sueldo(porcentaje)
                    empresa.guardar_empleados()
                else:
                    print("[ERROR] No hay empleado en esa posicion")
            except (ValueError, IndexError):
                print("[ERROR] Datos invalidos")
        
        elif opcion == "5":
            # Salir
            print("\n[INFO] Guardando datos y saliendo...")
            print("[OK] Hasta luego!\n")
            break
        
        else:
            print("\n[ERROR] Opcion invalida. Elige 1-5")


if __name__ == "__main__":
    main()
