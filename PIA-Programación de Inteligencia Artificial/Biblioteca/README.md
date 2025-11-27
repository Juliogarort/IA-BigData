# 📚 Sistema de Gestión de Biblioteca

![Biblioteca](https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=1200&h=400&fit=crop)

Sistema de gestión para una biblioteca, desarrollado en Python. Permite administrar libros, usuarios y préstamos mediante una interfaz de línea de comandos intuitiva.

## 📋 Descripción

Este proyecto implementa un sistema completo de gestión bibliotecaria que permite:

- **Gestión de Libros**: Registrar, modificar, eliminar y consultar libros
- **Gestión de Usuarios**: Administrar los usuarios de la biblioteca
- **Gestión de Préstamos**: Controlar préstamos y devoluciones de libros
- **Reportes**: Generar listados de préstamos pendientes e historial completo

Todos los datos se almacenan en archivos CSV locales, facilitando la portabilidad y el mantenimiento del sistema.

## 🚀 Características

- Interfaz mediante línea de comandos
- Generación automática de IDs únicos
- Validación de datos (disponibilidad de libros, existencia de usuarios)
- Cálculo automático de fechas de devolución (15 días)
- Persistencia de datos en archivos CSV
- Código bien documentado y estructurado
- Datos de prueba incluidos

## 🛠️ Requisitos

- Python 3.6 o superior
- No se requieren librerías externas (solo módulos estándar de Python)




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

