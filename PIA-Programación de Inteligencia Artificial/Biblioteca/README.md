
# 📚 Sistema de Gestión de Biblioteca


![Biblioteca](https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=1200&h=400&fit=crop)


Sistema completo de gestión bibliotecaria desarrollado en Python. Permite administrar libros, usuarios y préstamos mediante una interfaz de línea de comandos intuitiva y profesional.


---


## 📋 Descripción del Programa


Este proyecto implementa un sistema de gestión para una biblioteca comarcal que permite administrar libros, usuarios y préstamos mediante una interfaz de línea de comandos. Los datos se almacenan en archivos CSV locales, garantizando persistencia y portabilidad.


**Funcionalidades principales:**


- ✅ **Gestión de Libros**: Alta, baja, modificación y listado de libros
- ✅ **Gestión de Usuarios**: Administración completa de usuarios registrados
- ✅ **Gestión de Préstamos**: Control de préstamos y devoluciones
- ✅ **Reportes**: Listados de préstamos pendientes e historial completo


---


## 🚀 Características


- 📝 **Interfaz CLI intuitiva** con menús organizados
- 🔢 **Generación automática de IDs** únicos para cada entidad
- ✔️ **Validación de datos** (disponibilidad, existencia de registros)
- 📅 **Cálculo automático** de fechas de devolución (15 días)
- 💾 **Persistencia en CSV** - Todos los cambios se guardan automáticamente
- 🏗️ **Arquitectura modular** - Código organizado en capas (modelos, lógica, interfaz)
- 📚 **Datos de prueba incluidos** para empezar a usar inmediatamente
- 💬 **Código bien documentado** con comentarios explicativos


---


## 📦 Manual de Instalación


### Requisitos Previos


- **Python 3.6 o superior** instalado en el sistema
- **Sistema operativo**: Windows, Linux o macOS
- No se requieren librerías externas (solo módulos estándar de Python)


### Pasos de Instalación


#### 1. Verificar instalación de Python


```bash
python --version
```


o


```bash
python3 --version
```


#### 2. Navegar al directorio del proyecto


```bash
cd /ruta/a/Biblioteca
```


#### 3. Verificar estructura de archivos


Asegúrate de que existan los siguientes elementos:


- `main.py` - Archivo principal
- `modelos/` - Carpeta con las clases
- `logica/` - Carpeta con la lógica de negocio
- `datos/` - Carpeta con los archivos CSV


### Ejecución del Programa


```bash
python main.py
```


o


```bash
python3 main.py
```


---


## 📁 Estructura del Proyecto


```
Biblioteca/
├── main.py                    # Punto de entrada - Menús principales
├── datos/                     # Archivos CSV con los datos
│   ├── biblioLibros.csv       # Base de datos de libros
│   ├── biblioUsuarios.csv     # Base de datos de usuarios
│   └── biblioPrestamos.csv    # Base de datos de préstamos
├── modelos/                   # Clases de datos
│   ├── __init__.py
│   ├── libro.py               # Clase Libro
│   ├── usuario.py             # Clase Usuario
│   └── prestamo.py            # Clase Prestamo
├── logica/                    # Lógica de negocio (CRUD)
│   ├── __init__.py
│   ├── logica_libro.py        # Operaciones con libros
│   ├── logica_usuario.py      # Operaciones con usuarios
│   └── logica_prestamo.py     # Operaciones con préstamos
├── .gitignore                 # Archivos ignorados por Git
├── README.md                  # Este archivo
└── ProyectoPython.pdf         # Especificación del proyecto
```


---


## 🎯 Funcionamiento del Programa


### Menú Principal


Al ejecutar el programa, se presenta un menú con 6 opciones:


```
============================================================
MENÚ PRINCIPAL
============================================================
1. Gestión de Libros
2. Gestión de Usuarios
3. Registrar Préstamo
4. Registrar Devolución
5. Listados de Préstamos
6. Salir
============================================================
```


### Flujo de Trabajo Típico


1. **Dar de alta usuarios** (Opción 2 → 1)
2. **Registrar libros** (Opción 1 → 1)
3. **Realizar préstamos** (Opción 3)
4. **Consultar préstamos pendientes** (Opción 5 → 1)
5. **Registrar devoluciones** (Opción 4)


---


## 📖 Funcionalidades Detalladas


### 1️⃣ Gestión de Libros


**Operaciones disponibles:**


- **Alta de libro**: Registra nuevos libros con todos sus datos
- **Baja de libro**: Elimina libros del sistema (con confirmación)
- **Modificar libro**: Edita cualquier campo de un libro existente
- **Listar libros**: Muestra todos los libros registrados


**Atributos de Libro:**


- ID, Título, Autor, Año, Número de páginas, Género, Editorial, Estado, Disponibilidad


### 2️⃣ Gestión de Usuarios


**Operaciones disponibles:**


- **Alta de usuario**: Registra nuevos usuarios en el sistema
- **Baja de usuario**: Elimina usuarios (con confirmación)
- **Modificar usuario**: Edita datos de usuarios existentes
- **Listar usuarios**: Muestra todos los usuarios registrados


**Atributos de Usuario:**


- ID, Nombre, Apellidos, DNI, Correo electrónico, Teléfono, Dirección, Edad


### 3️⃣ Gestión de Préstamos


**Registrar préstamo:**


- Verifica que el usuario exista
- Verifica que el libro esté disponible
- Calcula automáticamente la fecha de devolución (15 días)
- Marca el libro como no disponible


**Registrar devolución:**


- Registra la fecha de devolución
- Marca el libro como disponible nuevamente


### 4️⃣ Listados de Préstamos


- **Préstamos pendientes**: Muestra solo los préstamos sin devolver
- **Historial completo**: Muestra todos los préstamos (pendientes y devueltos)


**Atributos de Préstamo:**


- ID Préstamo, ID Usuario, ID Libro, Fecha inicio, Fecha fin, Fecha devolución


---


## 🏗️ Descripción de las Clases


### Clase LIBRO (`modelos/libro.py`)


**Propósito:** Representa un libro en el sistema de la biblioteca.


**Atributos:**


- `id_libro` - Identificador único del libro
- `titulo` - Título del libro
- `autor` - Autor del libro
- `anyo` - Año de publicación
- `n_pags` - Número de páginas
- `genero` - Género literario
- `editorial` - Editorial que publicó el libro
- `estado` - Estado físico del libro (Nuevo/Usado)
- `disponible` - Indica si está disponible para préstamo (True/False)


**Métodos principales:**


- `a_diccionario()` - Convierte el objeto a diccionario para guardar en CSV
- `desde_diccionario()` - Crea un objeto Libro desde un diccionario
- `__str__()` - Representación en texto del libro


### Clase USUARIO (`modelos/usuario.py`)


**Propósito:** Representa un usuario registrado en la biblioteca.


**Atributos:**


- `id_usuario` - Identificador único del usuario
- `nombre` - Nombre del usuario
- `apellidos` - Apellidos del usuario
- `dni` - Documento Nacional de Identidad
- `correo_e` - Correo electrónico
- `tlfno` - Número de teléfono
- `direccion` - Dirección postal
- `edad` - Edad del usuario


**Métodos principales:**


- `a_diccionario()` - Convierte el objeto a diccionario para guardar en CSV
- `desde_diccionario()` - Crea un objeto Usuario desde un diccionario
- `__str__()` - Representación en texto del usuario


### Clase PRESTAMO (`modelos/prestamo.py`)


**Propósito:** Representa un préstamo de un libro a un usuario.


**Atributos:**


- `id_prestamo` - Identificador único del préstamo
- `id_usuario` - ID del usuario que realiza el préstamo
- `id_libro` - ID del libro prestado
- `fecha_inicio` - Fecha en que se realizó el préstamo
- `fecha_fin` - Fecha límite para devolver el libro
- `fecha_devolucion` - Fecha real de devolución (vacío si está pendiente)


**Métodos principales:**


- `a_diccionario()` - Convierte el objeto a diccionario para guardar en CSV
- `desde_diccionario()` - Crea un objeto Prestamo desde un diccionario
- `esta_pendiente()` - Verifica si el préstamo está pendiente de devolución
- `__str__()` - Representación en texto del préstamo


---


## 📚 Módulos de Lógica


### `logica_libro.py`


Gestiona todas las operaciones relacionadas con libros:


- Alta de nuevos libros
- Baja de libros existentes
- Modificación de datos de libros
- Listado de todos los libros
- Generación automática de IDs
- Lectura y escritura en `biblioLibros.csv`


### `logica_usuario.py`


Gestiona todas las operaciones relacionadas con usuarios:


- Alta de nuevos usuarios
- Baja de usuarios existentes
- Modificación de datos de usuarios
- Listado de todos los usuarios
- Generación automática de IDs
- Lectura y escritura en `biblioUsuarios.csv`


### `logica_prestamo.py`


Gestiona todas las operaciones relacionadas con préstamos:


- Registro de nuevos préstamos
- Registro de devoluciones
- Listado de préstamos pendientes
- Historial completo de préstamos
- Actualización de disponibilidad de libros
- Cálculo automático de fechas
- Lectura y escritura en `biblioPrestamos.csv`


---


## 🗂️ Archivos de Datos


### `biblioLibros.csv`


Almacena información de todos los libros registrados en el sistema.


**Formato:**


```csv
id_libro,titulo,autor,anyo,n_pags,genero,editorial,estado,disponible
1,Cien años de soledad,Gabriel García Márquez,1967,471,Novela,Sudamericana,Nuevo,True
```


### `biblioUsuarios.csv`


Almacena información de todos los usuarios registrados en el sistema.


**Formato:**


```csv
id_usuario,nombre,apellidos,dni,correo_e,tlfno,direccion,edad
1,Juan,Pérez García,12345678A,juan.perez@email.com,600123456,"Madrid, España",35
```


### `biblioPrestamos.csv`


Almacena el historial completo de préstamos realizados.


**Formato:**


```csv
id_prestamo,id_usuario,id_libro,fecha_inicio,fecha_fin,fecha_devolucion
1,1,2,2025-01-10,2025-01-25,2025-01-20
```


---


## ✅ Requisitos del Proyecto Cumplidos


- ✅ Clases LIBRO, USUARIO y PRESTAMO con todos los atributos requeridos
- ✅ Archivos CSV independientes para cada entidad (`biblioLibros.csv`, `biblioUsuarios.csv`, `biblioPrestamos.csv`)
- ✅ Menú principal con las 6 opciones especificadas
- ✅ CRUD completo para libros y usuarios (Alta, Baja, Modificación, Listado)
- ✅ Sistema de préstamos y devoluciones funcional
- ✅ Listados de préstamos pendientes e historial completo
- ✅ Código estructurado en módulos separados
- ✅ Comentarios explicativos en todo el código
- ✅ Interacción por línea de comandos
- ✅ Validaciones y confirmaciones en operaciones críticas
- ✅ Manejo de errores y excepciones
