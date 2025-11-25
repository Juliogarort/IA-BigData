# Ejercicios de Trabajando con Ficheros - Python

Este directorio contiene 4 ejercicios prácticos sobre manejo de ficheros en Python (TXT y CSV).

## 📁 Archivos del Proyecto

- `ejercicio01.py` - Tablas de multiplicar
- `ejercicio02.py` - Listín telefónico
- `ejercicio03.py` - Análisis de cotizaciones del IBEX35
- `ejercicio04.py` - Gestión de calificaciones de estudiantes
- `cotizacion.csv` - Datos de cotizaciones (proporcionado)
- `calificaciones.csv` - Datos de calificaciones (proporcionado)

---

## 📝 Ejercicio 01: Tablas de Multiplicar

### Descripción
Programa interactivo para crear, leer y consultar tablas de multiplicar guardadas en ficheros de texto.

### Funciones principales
- **crear_tabla_multiplicar()**: Crea un fichero `tabla-n.txt` con la tabla de multiplicar del número n
- **leer_tabla_multiplicar()**: Lee y muestra la tabla completa
- **leer_linea_tabla()**: Muestra una línea específica de la tabla

### Cómo ejecutar
```bash
python ejercicio01.py
```

### Ejemplo de uso
1. Selecciona opción 1 para crear una tabla (por ejemplo, del número 5)
2. Selecciona opción 2 para leer la tabla completa
3. Selecciona opción 3 para leer una línea específica (por ejemplo, línea 7)

---

## 📞 Ejercicio 02: Listín Telefónico

### Descripción
Sistema de gestión de un listín telefónico que permite crear, consultar, añadir y eliminar contactos.

### Funciones principales
- **crear_listin()**: Crea el fichero `listin.txt` si no existe
- **consultar_telefono()**: Busca el teléfono de un cliente
- **anadir_cliente()**: Añade un nuevo cliente al listín
- **eliminar_cliente()**: Elimina un cliente del listín
- **mostrar_listin()**: Muestra todos los contactos

### Cómo ejecutar
```bash
python ejercicio02.py
```

### Ejemplo de uso
1. Crea el listín con la opción 1
2. Añade clientes con la opción 3 (ejemplo: "Juan Pérez", "123456789")
3. Consulta teléfonos con la opción 2
4. Visualiza todos los contactos con la opción 5

### Formato del fichero
```
Nombre,Teléfono
```

---

## 📊 Ejercicio 03: Análisis de Cotizaciones del IBEX35

### Descripción
Programa que lee datos de cotizaciones del IBEX35, calcula estadísticas (mínimo, máximo y media) y guarda los resultados en un fichero CSV.

### Funciones principales
- **leer_cotizaciones(fichero)**: Lee el CSV y devuelve un diccionario por columnas
- **calcular_estadisticas(datos)**: Calcula min, max y media de cada columna numérica
- **guardar_estadisticas(estadisticas, fichero_salida)**: Guarda las estadísticas en CSV
- **mostrar_estadisticas(estadisticas)**: Muestra las estadísticas por pantalla

### Cómo ejecutar
```bash
python ejercicio03.py
```

### Salida
- Muestra estadísticas por pantalla
- Crea el fichero `estadisticas.csv` con los resultados

### Columnas analizadas
- Final (precio de cierre)
- Máximo (precio máximo)
- Mínimo (precio mínimo)
- Volumen (volumen de negociación)
- Efectivo (capitalización)

---

## 🎓 Ejercicio 04: Gestión de Calificaciones

### Descripción
Programa que procesa las calificaciones de un curso, calcula notas finales y separa alumnos aprobados y suspensos.

### Funciones principales
- **leer_calificaciones(fichero)**: Lee el CSV y devuelve lista de diccionarios ordenada por apellidos
- **calcular_nota_final(lista_alumnos)**: Calcula la nota final de cada alumno
- **separar_aprobados_suspensos(lista_alumnos)**: Separa en dos listas según criterios

### Criterios de evaluación
**Cálculo de nota final:**
- Parcial 1 de teoría: 30% (usa recuperación si nota < 4)
- Parcial 2 de teoría: 30% (usa recuperación si nota < 4)
- Prácticas: 40% (usa recuperación si nota < 4)

**Criterios para aprobar:**
- Asistencia ≥ 75%
- Todas las notas de exámenes ≥ 4
- Nota final ≥ 5

### Cómo ejecutar
```bash
python ejercicio04.py
```

### Salida
- Lista de alumnos aprobados
- Lista de alumnos suspensos
- Resumen con porcentajes

---

## 🎯 Conceptos de Python Utilizados

### Ejercicio 01
- Manejo de ficheros de texto (`open`, `read`, `write`)
- Uso de `with` para gestión automática de ficheros
- Manejo de excepciones (`try-except`)
- Formateo de strings con f-strings

### Ejercicio 02
- Lectura y escritura de ficheros
- Manipulación de strings (`split`, `strip`, `lower`)
- Listas y búsqueda en listas
- Actualización de ficheros (leer, modificar, reescribir)

### Ejercicio 03
- Lectura de ficheros CSV
- Diccionarios en Python
- Conversión de tipos de datos
- Funciones con parámetros y valores de retorno
- Cálculos estadísticos (min, max, promedio)

### Ejercicio 04
- Lectura de CSV con datos complejos
- Listas de diccionarios
- Ordenamiento con `sort` y `lambda`
- Lógica condicional compleja
- Formateo de salida con alineación

---

## ⚠️ Notas Importantes

1. **Codificación**: Todos los ficheros usan codificación UTF-8 para soportar caracteres especiales (tildes, ñ, etc.)

2. **Separador CSV**: Los ficheros CSV usan punto y coma (`;`) como separador

3. **Formato de números**: Los números en los CSV españoles usan coma (`,`) como separador decimal

4. **Ficheros generados**:
   - Ejercicio 01: `tabla-n.txt` (donde n es el número elegido)
   - Ejercicio 02: `listin.txt`
   - Ejercicio 03: `estadisticas.csv`

---

## 🚀 Ejecución Rápida de Todos los Ejercicios

Para probar rápidamente todos los ejercicios:

```bash
# Ejercicio 01 - Tablas de multiplicar
python ejercicio01.py

# Ejercicio 02 - Listín telefónico
python ejercicio02.py

# Ejercicio 03 - Análisis de cotizaciones (ejecución automática)
python ejercicio03.py

# Ejercicio 04 - Gestión de calificaciones (ejecución automática)
python ejercicio04.py
```

---

## 📚 Recursos de Aprendizaje

Si eres principiante en Python, estos ejercicios te ayudarán a aprender:
- Manejo de ficheros de texto y CSV
- Estructuras de datos (listas, diccionarios)
- Funciones y modularización de código
- Manejo de excepciones
- Formateo de salida
- Procesamiento de datos

¡Buena suerte con los ejercicios! 🎉
