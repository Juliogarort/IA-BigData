# Recomendador Académico

Sistema experto híbrido en Python y Prolog para recomendar orientación académica a partir de un archivo CSV con datos de alumnos.

## Requisitos
- Python 3
- SWI-Prolog instalado
- Librería `pandas`

## Instalación de pandas
```bash
/usr/bin/python3 -m pip install pandas
```

## Archivos del proyecto
- `recomendador.py`: programa principal en Python.
- `reglas.pl`: base de conocimiento en Prolog.
- `alumnos.csv`: fichero de entrada con los datos de los alumnos.

## Ejecución
1. Coloca todos los archivos en la misma carpeta.
2. Abre una terminal en esa carpeta.
3. Ejecuta el programa:

```bash
/usr/bin/python3 recomendador.py
```

## Salida
El programa mostrará por pantalla las recomendaciones de cada alumno y también generará un archivo `resultados.txt` con el resumen completo.