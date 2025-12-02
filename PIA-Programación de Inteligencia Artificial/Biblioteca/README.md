# 📚 Sistema de Gestión de Biblioteca

![Biblioteca](https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=1200&h=400&fit=crop)

Sistema completo de gestión bibliotecaria desarrollado en Python. Permite administrar libros, usuarios y préstamos mediante una interfaz de línea de comandos intuitiva y profesional.

---

## 📋 Descripción

Este proyecto implementa un sistema de gestión para una biblioteca comarcal que permite:

- ✅ **Gestión de Libros**: Alta, baja, modificación y listado de libros
- ✅ **Gestión de Usuarios**: Administración completa de usuarios registrados
- ✅ **Gestión de Préstamos**: Control de préstamos y devoluciones
- ✅ **Reportes**: Listados de préstamos pendientes e historial completo

Todos los datos se almacenan en archivos CSV locales, garantizando persistencia y portabilidad.

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

## 🛠️ Requisitos

- **Python 3.6 o superior**
- No se requieren librerías externas (solo módulos estándar de Python)

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

## 🎯 Uso del Sistema


### Menú Principal

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

---

## 📖 Funcionalidades Detalladas

### 1️⃣ Gestión de Libros

- **Alta de libro**: Registra nuevos libros con todos sus datos
- **Baja de libro**: Elimina libros del sistema (con confirmación)
- **Modificar libro**: Edita cualquier campo de un libro existente
- **Listar libros**: Muestra todos los libros registrados

**Atributos de Libro:**
- ID, Título, Autor, Año, Número de páginas, Género, Editorial, Estado, Disponibilidad

### 2️⃣ Gestión de Usuarios

- **Alta de usuario**: Registra nuevos usuarios en el sistema
- **Baja de usuario**: Elimina usuarios (con confirmación)
- **Modificar usuario**: Edita datos de usuarios existentes
- **Listar usuarios**: Muestra todos los usuarios registrados

**Atributos de Usuario:**
- ID, Nombre, Apellidos, DNI, Correo electrónico, Teléfono, Dirección, Edad

### 3️⃣ Gestión de Préstamos

- **Registrar préstamo**: Asigna un libro disponible a un usuario
  - Verifica que el usuario exista
  - Verifica que el libro esté disponible
  - Calcula automáticamente la fecha de devolución (15 días)
  - Marca el libro como no disponible

- **Registrar devolución**: Procesa la devolución de un libro
  - Registra la fecha de devolución
  - Marca el libro como disponible nuevamente

### 4️⃣ Listados de Préstamos

- **Préstamos pendientes**: Muestra solo los préstamos sin devolver
- **Historial completo**: Muestra todos los préstamos (pendientes y devueltos)

**Atributos de Préstamo:**
- ID Préstamo, ID Usuario, ID Libro, Fecha inicio, Fecha fin, Fecha devolución

---

## 🗂️ Archivos CSV

Los datos se almacenan en 3 archivos CSV en la carpeta `datos/`:

### biblioLibros.csv
```csv
id_libro,titulo,autor,anyo,n_pags,genero,editorial,estado,disponible
1,Cien años de soledad,Gabriel García Márquez,1967,471,Novela,Sudamericana,Nuevo,True
```

### biblioUsuarios.csv
```csv
id_usuario,nombre,apellidos,dni,correo_e,tlfno,direccion,edad
1,Juan,Pérez García,12345678A,juan.perez@email.com,600123456,"Madrid, España",35
```

### biblioPrestamos.csv
```csv
id_prestamo,id_usuario,id_libro,fecha_inicio,fecha_fin,fecha_devolucion
1,1,2,2025-01-10,2025-01-25,2025-01-20
```

---

## 🏗️ Arquitectura del Código

### Capa de Modelos (`modelos/`)
Define las clases de datos con sus atributos y métodos de conversión:
- `Libro`: Representa un libro de la biblioteca
- `Usuario`: Representa un usuario registrado
- `Prestamo`: Representa un préstamo de libro

### Capa de Lógica (`logica/`)
Implementa las operaciones CRUD y lógica de negocio:
- `logica_libro.py`: Operaciones con libros
- `logica_usuario.py`: Operaciones con usuarios
- `logica_prestamo.py`: Operaciones con préstamos

### Capa de Interfaz (`main.py`)
Gestiona la interacción con el usuario mediante menús CLI.

---

### Requisitos Cumplidos ✅

- ✅ Clases LIBRO, USUARIO y PRESTAMO con todos los atributos requeridos
- ✅ Archivos CSV independientes para cada entidad
- ✅ Menú principal con las 6 opciones especificadas
- ✅ CRUD completo para libros y usuarios
- ✅ Sistema de préstamos y devoluciones funcional
- ✅ Listados de préstamos pendientes
- ✅ Código estructurado, comentado y organizado en módulos
- ✅ Interacción por línea de comandos