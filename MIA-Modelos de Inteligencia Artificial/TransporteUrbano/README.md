# Sistema Experto – Transporte Urbano

**MIA · ILERNA Sevilla · Julio García**

Sistema experto híbrido desarrollado en **Python + Prolog** que recomienda el medio de transporte urbano más adecuado según distintas condiciones del desplazamiento.

---

## 📂 Archivos del proyecto

| Fichero                           | Descripción                     |
| --------------------------------- | ------------------------------- |
| `transporte.py`                   | Script principal en Python      |
| `TransporteUrbano_JulioGarcía.pl` | Base de conocimiento en Prolog  |
| `transporte_urbano.csv`           | Dataset con los casos de prueba |

---

## ⚙️ Requisitos

### 1. Python 3

Comprobar instalación:

```bash
python3 --version
```

En Windows:

```bash
python --version
```

---

### 2. SWI-Prolog

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install swi-prolog
```

#### Windows

1. Descargar desde: https://www.swi-prolog.org/download/stable
2. Instalar normalmente (Next → Next)
3. Asegurarse de que está en el PATH

Comprobar:

```bash
swipl --version
```

---

### 3. Librería pyswip

#### Ubuntu

```bash
pip3 install pyswip
```

#### Windows

```bash
pip install pyswip
```

⚠️ En Windows puede ser necesario instalar también:

* Visual C++ Build Tools
* Reiniciar el sistema tras instalar Prolog

---

## ▶️ Ejecución del programa

⚠️ IMPORTANTE:
Los 3 archivos deben estar en la **misma carpeta**.

---

### En Ubuntu

```bash
python3 transporte.py
```

---

### En Windows

```bash
python transporte.py
```

---

## 🔄 Funcionamiento del sistema

1. Python lee el archivo `transporte_urbano.csv`
2. Valida los datos
3. Convierte valores numéricos en categorías:

   * Distancia → corta / media / larga
   * Tiempo → poco / normal / suficiente
4. Envía los hechos a Prolog
5. Prolog aplica reglas y genera recomendaciones
6. Python muestra los resultados

---

## 📊 Ejemplo de salida

```
──────────────────────────────────────────────────
 CASO 01 | 16.2km [larga] | 8min [poco] | alto | lluvia | bajo | rapidez
 metro (rapido)
    Trafico alto o distancia larga. El metro es rapido y evita el trafico en ciudad.
    Alternativas: autobus
```

---

## ⚠️ Validaciones

El sistema verifica:

* Valores numéricos correctos (> 0)
* Categorías válidas (tráfico, clima, etc.)
* Campos no vacíos

Los casos incorrectos se ignoran.

---

## ❗ Posibles errores comunes

### Error: `pyswip not found`

```bash
pip install pyswip
```

---


## 💡 Notas técnicas

* Python gestiona datos e interacción
* Prolog gestiona reglas e inferencia
* Comunicación mediante la librería `pyswip`
* Uso de hechos dinámicos en Prolog (`assertz` / `retractall`)

---

