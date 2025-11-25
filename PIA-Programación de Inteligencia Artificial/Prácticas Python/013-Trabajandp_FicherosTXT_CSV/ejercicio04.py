

import os

# Obtener la ruta del directorio donde está este script
DIRECTORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))

def leer_calificaciones(fichero):
    alumnos = []
    
    # Creamos la ruta completa del fichero
    ruta_completa = os.path.join(DIRECTORIO_SCRIPT, fichero)
    
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            # Leemos la primera línea (cabecera con los nombres de las columnas)
            primera_linea = f.readline().strip()
            columnas = primera_linea.split(';')
            
            # Leemos cada línea del fichero
            for linea in f:
                linea = linea.strip()
                
                # Si la línea no está vacía
                if linea:
                    valores = linea.split(';')
                    
                    # Creamos un diccionario para este alumno
                    alumno = {}
                    
                    for i, columna in enumerate(columnas):
                        valor = valores[i] if i < len(valores) else ''
                        
                        # Convertimos los valores según el tipo de columna
                        if columna == 'Asistencia':
                            # Quitamos el símbolo % y convertimos a número
                            if valor:
                                alumno[columna] = int(valor.replace('%', ''))
                            else:
                                alumno[columna] = 0
                        elif columna in ['Apellidos', 'Nombre']:
                            # Guardamos el texto tal cual
                            alumno[columna] = valor
                        else:
                            # Para las notas, convertimos a float (coma por punto)
                            if valor:
                                try:
                                    alumno[columna] = float(valor.replace(',', '.'))
                                except ValueError:
                                    alumno[columna] = 0.0
                            else:
                                alumno[columna] = 0.0
                    
                    alumnos.append(alumno)
        
        # Ordenamos la lista por apellidos
        alumnos.sort(key=lambda x: x['Apellidos'])
        
        print(f"Calificaciones leídas correctamente de {fichero}")
        print(f"Total de alumnos: {len(alumnos)}")
        return alumnos
        
    except FileNotFoundError:
        print(f"Error: No se encontró el fichero {fichero}")
        return None


def calcular_nota_final(lista_alumnos):
    
    if lista_alumnos is None:
        return None
    
    for alumno in lista_alumnos:
        # Determinamos qué nota usar para el Parcial 1
        if alumno['Parcial1'] < 4 and alumno['Ordinario1'] > 0:
            nota_parcial1 = alumno['Ordinario1']
        else:
            nota_parcial1 = alumno['Parcial1']
        
        # Determinamos qué nota usar para el Parcial 2
        if alumno['Parcial2'] < 4 and alumno['Ordinario2'] > 0:
            nota_parcial2 = alumno['Ordinario2']
        else:
            nota_parcial2 = alumno['Parcial2']
        
        # Determinamos qué nota usar para Prácticas
        if alumno['Practicas'] < 4 and alumno['OrdinarioPracticas'] > 0:
            nota_practicas = alumno['OrdinarioPracticas']
        else:
            nota_practicas = alumno['Practicas']
        
        # Calculamos la nota final
        nota_final = (nota_parcial1 * 0.30) + (nota_parcial2 * 0.30) + (nota_practicas * 0.40)
        
        # Añadimos la nota final al diccionario del alumno
        alumno['NotaFinal'] = round(nota_final, 2)
    
    return lista_alumnos


def separar_aprobados_suspensos(lista_alumnos):

    if lista_alumnos is None:
        return None, None
    
    aprobados = []
    suspensos = []
    
    for alumno in lista_alumnos:
        # Determinamos qué notas usar (las mismas que para calcular la nota final)
        nota_parcial1 = alumno['Ordinario1'] if (alumno['Parcial1'] < 4 and alumno['Ordinario1'] > 0) else alumno['Parcial1']
        nota_parcial2 = alumno['Ordinario2'] if (alumno['Parcial2'] < 4 and alumno['Ordinario2'] > 0) else alumno['Parcial2']
        nota_practicas = alumno['OrdinarioPracticas'] if (alumno['Practicas'] < 4 and alumno['OrdinarioPracticas'] > 0) else alumno['Practicas']
        
        # Verificamos los criterios de aprobado
        asistencia_ok = alumno['Asistencia'] >= 75
        notas_ok = nota_parcial1 >= 4 and nota_parcial2 >= 4 and nota_practicas >= 4
        nota_final_ok = alumno['NotaFinal'] >= 5
        
        # Si cumple todos los criterios, está aprobado
        if asistencia_ok and notas_ok and nota_final_ok:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    
    return aprobados, suspensos


def mostrar_alumnos(lista_alumnos, titulo):
    """
    Muestra una lista de alumnos de forma bonita
    """
    if not lista_alumnos:
        print(f"\n{titulo}: No hay alumnos")
        return
    
    print("\n" + "=" * 90)
    print(titulo)
    print("=" * 90)
    print(f"{'Apellidos':<25} {'Nombre':<15} {'Asist.':<8} {'Nota Final':<12} {'Estado':<10}")
    print("-" * 90)
    
    for alumno in lista_alumnos:
        estado = "APROBADO" if alumno in lista_alumnos else "SUSPENSO"
        print(f"{alumno['Apellidos']:<25} {alumno['Nombre']:<15} {alumno['Asistencia']:>6}% "
              f"{alumno['NotaFinal']:>10.2f}  {estado:<10}")
    
    print("=" * 90)
    print(f"Total: {len(lista_alumnos)} alumnos")


def menu():
    """
    Menú principal para gestionar las calificaciones
    """
    alumnos = None
    aprobados = None
    suspensos = None
    
    while True:
        print("\n" + "=" * 90)
        print("EJERCICIO 04 - GESTIÓN DE CALIFICACIONES")
        print("=" * 90)
        print("1. Leer fichero de calificaciones (calificaciones.csv)")
        print("2. Calcular notas finales")
        print("3. Separar aprobados y suspensos")
        print("4. Mostrar resultados completos")
        print("5. Salir")
        print("=" * 90)
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            print("\n1. Leyendo fichero de calificaciones...")
            alumnos = leer_calificaciones('calificaciones.csv')
            if alumnos:
                # Reiniciamos las notas finales y separación
                aprobados = None
                suspensos = None
                
        elif opcion == '2':
            if alumnos is None:
                print("\nError: Primero debes leer el fichero de calificaciones (opción 1)")
            else:
                print("\n2. Calculando notas finales...")
                alumnos = calcular_nota_final(alumnos)
                
                # Mostramos cada alumno con su nota final
                print("\n" + "=" * 90)
                print("NOTAS FINALES CALCULADAS")
                print("=" * 90)
                print(f"{'Apellidos':<25} {'Nombre':<15} {'Nota Final':>12}")
                print("-" * 90)
                for alumno in alumnos:
                    print(f"{alumno['Apellidos']:<25} {alumno['Nombre']:<15} {alumno['NotaFinal']:>12.2f}")
                print("=" * 90)
                
                # Reiniciamos la separación porque las notas cambiaron
                aprobados = None
                suspensos = None
                
        elif opcion == '3':
            if alumnos is None:
                print("\nError: Primero debes leer el fichero de calificaciones (opción 1)")
            elif 'NotaFinal' not in alumnos[0]:
                print("\nError: Primero debes calcular las notas finales (opción 2)")
            else:
                print("\n3. Separando aprobados y suspensos...")
                aprobados, suspensos = separar_aprobados_suspensos(alumnos)
                
                # Mostramos dos columnas: aprobados y suspensos
                print("\n" + "=" * 90)
                print("SEPARACIÓN DE APROBADOS Y SUSPENSOS")
                print("=" * 90)
                print(f"{'APROBADOS':<44} | {'SUSPENSOS':<44}")
                print("-" * 90)
                
                # Determinamos cuántas filas necesitamos (el máximo entre aprobados y suspensos)
                max_filas = max(len(aprobados), len(suspensos))
                
                for i in range(max_filas):
                    # Columna de aprobados
                    if i < len(aprobados):
                        nombre_aprobado = f"{aprobados[i]['Apellidos']}, {aprobados[i]['Nombre']}"
                        # Truncamos si es muy largo
                        if len(nombre_aprobado) > 42:
                            nombre_aprobado = nombre_aprobado[:39] + "..."
                    else:
                        nombre_aprobado = ""
                    
                    # Columna de suspensos
                    if i < len(suspensos):
                        nombre_suspenso = f"{suspensos[i]['Apellidos']}, {suspensos[i]['Nombre']}"
                        # Truncamos si es muy largo
                        if len(nombre_suspenso) > 42:
                            nombre_suspenso = nombre_suspenso[:39] + "..."
                    else:
                        nombre_suspenso = ""
                    
                    print(f"{nombre_aprobado:<44} | {nombre_suspenso:<44}")
                
                print("=" * 90)
                print(f"Total aprobados: {len(aprobados):<15} Total suspensos: {len(suspensos)}")
                print("=" * 90)
                
        elif opcion == '4':
            if aprobados is None or suspensos is None:
                print("\nError: Primero debes separar aprobados y suspensos (opción 3)")
            else:
                # Mostramos los resultados
                print("\n" + "=" * 90)
                print("RESULTADOS COMPLETOS")
                print("=" * 90)
                
                # Mostramos aprobados
                mostrar_alumnos(aprobados, "ALUMNOS APROBADOS")
                
                # Mostramos suspensos
                mostrar_alumnos(suspensos, "ALUMNOS SUSPENSOS")
                
                # Resumen
                print("\n" + "=" * 90)
                print("RESUMEN")
                print("=" * 90)
                print(f"Total de alumnos: {len(alumnos)}")
                print(f"Aprobados: {len(aprobados)} ({len(aprobados)/len(alumnos)*100:.1f}%)")
                print(f"Suspensos: {len(suspensos)} ({len(suspensos)/len(alumnos)*100:.1f}%)")
                print("=" * 90)
                
        elif opcion == '5':
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Elige entre 1 y 5.")


# Programa principal
if __name__ == "__main__":
    menu()
