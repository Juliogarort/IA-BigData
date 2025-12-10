# Windows IA - Versión Simplificada

**Sistema Operativo Gráfico en Python - Ultra Simple**

## 🎯 Características

Esta es la versión **MÁS SIMPLE POSIBLE** del sistema:

- ✅ **Un solo archivo**: Todo el código en `main.py`
- ✅ **Sin módulos complejos**: Solo las librerías estándar + Pillow
- ✅ **Código en español**: Variables y clases con nombres descriptivos
- ✅ **Misma funcionalidad**: Las 4 aplicaciones completas
- ✅ **Fácil de entender**: Código minimalista y directo

## 🚀 Ejecución Rápida

```bash
# Solo necesitas esto:
python main.py
```

¡Así de simple! No hay múltiples archivos, ni imports complicados.

## 📦 Aplicaciones Incluidas

Las 4 aplicaciones funcionales implementadas:

### 1. **🖩 Calculadora**
   - Operaciones básicas (+, -, *, /, %)
   - Botones C (limpiar) y ← (borrar)
   - Interfaz intuitiva estilo calculadora moderna

### 2. **📝 Bloc de Notas**
   - Nuevo, Abrir, Guardar archivos .txt
   - Atajos de teclado: Ctrl+S (guardar), Ctrl+O (abrir)
   - Editor con scroll automático

### 3. **⚙️ Configuración**
   - 6 colores sólidos predefinidos
   - Selector de color personalizado (RGB)
   - **Miniaturas de wallpapers** con vista previa
   - Carga dinámica de imágenes desde carpeta `wallpapers/`
   - Importar imagen personalizada desde PC
   - Interfaz con scroll para mejor navegación

### 4. **🕐 Reloj Digital**
   - Hora en tiempo real (formato 24h)
   - Fecha completa en español
   - Actualización automática cada segundo


## ⚠️ Dependencias Críticas

> [!IMPORTANT]
> **Pillow es OBLIGATORIO** para que el programa funcione correctamente. Sin este módulo, el programa no se ejecutará.

### Instalación de Pillow:

```bash
# Windows
pip install Pillow

# Linux/Mac
pip3 install Pillow
```

Si obtienes el error `ModuleNotFoundError: No module named 'PIL'`, significa que Pillow no está instalado. Ejecuta el comando de instalación correspondiente a tu sistema operativo.

## 🔧 Requisitos del Sistema

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk python3-pil.imagetk

# Windows
pip install Pillow

# Verificar instalación
python -c "import tkinter; from PIL import ImageTk; print('✓ Todo OK')"

# Ejecutar el programa
python main.py
```

## 📂 Estructura del Proyecto

```
Windows_IA_Simple/
├── main.py                  ← TODO EL CÓDIGO AQUÍ (450 líneas)
├── resources/
│   ├── icons/               ← Iconos de aplicaciones (opcional)
│   └── wallpapers/          ← Fondos de pantalla (carga dinámica)
└── README.md                ← Esta documentación
```

## 👨‍💻 Estructura del Código

El código está organizado en 3 secciones principales:

### 1. **Clases de Aplicaciones** (líneas 19-312)
   - `Calculadora` (líneas 19-80)
   - `BlocNotas` (líneas 83-136)
   - `Configuracion` (líneas 139-285)
   - `Reloj` (líneas 288-312)

### 2. **Clase Escritorio Principal** (líneas 318-436)
   - Crea el escritorio con fondo personalizable
   - Maneja iconos y barra de tareas
   - Gestiona el fondo (colores e imágenes)
   - Reloj del sistema en tiempo real

### 3. **Ejecución** (líneas 441-449)
   - Inicializa y ejecuta el bucle principal



## 🎨 Funcionalidades Destacadas

### Configuración Avanzada
- **Miniaturas de wallpapers**: Vista previa de imágenes en la carpeta `wallpapers/`
- **Carga dinámica**: Detecta automáticamente todas las imágenes (.png, .jpg, .jpeg, .bmp)
- **Interfaz con scroll**: Navegación fluida en la ventana de configuración
- **Tooltips visuales**: Efectos hover en las miniaturas

### Personalización del Escritorio
- Cambio de color de fondo en tiempo real
- Carga de imágenes de fondo con redimensionamiento automático
- Los iconos siempre permanecen visibles sobre el fondo

## 📝 Notas Técnicas

- **Resolución**: 1024x768 píxeles (configurable en constantes)
- **Codificación**: UTF-8 para soporte completo de español
- **Compatibilidad**: Windows, Linux, macOS (con tkinter instalado)
- **Recursos**: Los wallpapers e iconos son opcionales
- **Variables en español**: Todo el código usa nomenclatura en español

## 🔍 Variables Globales

```python
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
ANCHO_PANTALLA = 1024
ALTO_PANTALLA = 768
ALTURA_BARRA_TAREAS = 50
COLOR_FONDO = "#667eea"  # Azul/púrpura por defecto
```

---

**¡Disfruta de la simplicidad de Python!** 🐍✨

_Versión: Simple v1.0_  
_Proyecto: Programación IA - Curso de Especialización_  
_Última actualización: Diciembre 2025_
