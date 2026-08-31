# Proyecto de análisis y simulación de datos

Este proyecto simula información de árboles sembrados a lo largo de la avenida 80. La idea principal es mostrar cómo se pueden generar datos aleatorios, limpiarlos y convertirlos en una tabla para analizarlos con Python.

## 1. ¿Qué hace este proyecto?

En el archivo `notebook/simulacion.py` se define la función `generar_simulacion(numero_simulaciones)`, la cual:

- crea una lista de árboles simulados
- asigna valores aleatorios como:
  - nombre del árbol
  - altura
  - estado
  - dirección
  - nombre del botánico encargado
- puede generar errores artificiales para simular datos sucios o inconsistentes
- convierte esa lista en un `DataFrame` de pandas para trabajar con una tabla

Es una práctica muy útil para entender:

- cómo generar datos sintéticos
- cómo detectar valores nulos o incorrectos
- cómo limpiar datos antes de analítica
- cómo hacer análisis con tablas en Python

---

## 2. Conceptos clave

### 2.1. `random`

La librería `random` de Python permite generar números aleatorios y hacer elecciones aleatorias.

#### `random.randint(a, b)`
Genera un número entero aleatorio entre `a` y `b` inclusive.

```python
import random

id_aleatorio = random.randint(0, 200)
print(id_aleatorio)
```

En el proyecto se usa para crear IDs aleatorios:

```python
"id": random.randint(0, 200)
```

#### `random.choice(lista)`
Elige un elemento aleatorio de una lista.

```python
nombres = ["pino", "sauce", "cedro"]
nombre = random.choice(nombres)
```

Se usa en el proyecto para elegir:

- botánico encargado
- dirección
- altura
- nombre del árbol
- estado

#### `random.random()`
Genera un número decimal aleatorio entre 0 y 1.

```python
probabilidad = random.random()
print(probabilidad)
```

Se usa para decidir si se genera un dato inconsistente o faltante.

---

### 2.2. `pandas`

`pandas` es una librería usada para trabajar con datos tabulares. La estructura principal es el `DataFrame`.

#### ¿Qué es un `DataFrame`?
Es como una tabla de Excel o una hoja de cálculo:

- filas = registros
- columnas = características
- cada columna puede tener un tipo de dato distinto

Ejemplo:

```python
import pandas as pd

tabla = pd.DataFrame([
    {"id": 1, "nombre": "pino", "estado": "optimo"},
    {"id": 2, "nombre": "cedro", "estado": "malo"}
])

print(tabla)
```

En este proyecto, después de crear la lista de simulaciones, se hace:

```python
tabla = pd.DataFrame(simulaciones)
print(tabla)
```

Eso convierte la lista de diccionarios en una tabla de datos fácilmente manipulable.

---

### 2.3. Datos faltantes y datos sucios

La simulación genera valores problemáticos para imitar datos reales:

```python
if probabilidad_error < 0.2:
    simulacion["id"] = None
elif probabilidad_error < 0.4:
    simulacion["id"] = random.choice([-10, -1, 0])
    simulacion["direccion"] = random.choice(["av 7 bogota", None])
elif probabilidad_error < 0.6:
    simulacion["estado"] = "chocolate"
    simulacion["nombre"] = simulacion["nombre"].upper()
elif probabilidad_error < 0.8:
    simulacion["botanico_encargado"] = random.choice([None, -1, "sin"])
```

Esto permite ver situaciones comunes en analítica:

- `None` = dato faltante
- valores negativos = posible error de captura
- texto extraño = dato inconsistente
- mayúsculas en nombres = falta de estandarización

#### Ejemplo realista
En proyectos reales, esto suele ocurrir por:

- formularios incompletos
- digitación incorrecta
- errores del sistema
- valores no estandarizados

---

## 3. Flujo del proyecto

El flujo básico es:

1. definir una semilla de datos
2. generar valores aleatorios
3. generar una probabilidad de error
4. introducir anomalías controladas
5. guardar los registros en una lista
6. convertir la lista en un `DataFrame`
7. analizar la tabla

Esto es una base muy buena para entender analítica, ciencia de datos y ETL básico.

---

## 4. ¿Qué es Faker?

`Faker` es una librería de Python que genera datos falsos pero realistas, como:

- nombres
- correos
- teléfonos
- direcciones
- ciudades
- fechas
- empresas

### Ejemplo:

```python
from faker import Faker

fake = Faker('es_ES')

print(fake.name())
print(fake.email())
print(fake.address())
print(fake.date_of_birth())
```

#### ¿Por qué se usa?
Porque permite crear bases de datos de prueba sin usar información real.

Ejemplos de uso:

- pruebas de software
- generación de datos para dashboards
- simulación de clientes, productos o empleados
- educación y demostraciones

### Diferencia entre `random` y `Faker`

- `random` sirve para valores aleatorios simples
- `Faker` sirve para generar datos más realistas y estructurados

Ejemplo:

```python
random.choice(["pino", "cedro"])  # valor simple
fake.name()                        # nombre realista
```

---

## 5. ¿Qué más se puede hacer con este tipo de datos?

Una vez los datos están en un `DataFrame`, puedes hacer cosas como:

- contar cuántos árboles hay por estado
- contar cuántos árboles están en buena condición
- detectar registros con datos faltantes
- buscar direcciones raras o inválidas
- limpiar nombres y textos
- visualizar estadísticas con `matplotlib` o `seaborn`

Ejemplo:

```python
print(tabla["estado"].value_counts())
print(tabla.isnull().sum())
```

Eso sirve para realizar analítica descriptiva básica.

---

## 6. Diferencias importantes entre librerías

### `random`
- viene con Python
- útil para valores simples y aleatorios
- no genera datos con contexto realista

### `Faker`
- librería extra
- genera nombres, direcciones, correos, etc.
- útil para pruebas o datos más naturales

### `pandas`
- transforma datos en tablas
- facilita limpieza, análisis y visualización
- es imprescindible en ciencia de datos

---

## 7. Conceptos que suelen preguntar en entrevista

### Pregunta 1: ¿Qué es `random.choice()`?
Respuesta breve:

> Es una función que selecciona un elemento al azar dentro de una lista.

### Pregunta 2: ¿Qué diferencia hay entre `random.randint()` y `random.random()`?
Respuesta:

- `randint(a, b)` devuelve un entero entre `a` y `b`
- `random()` devuelve un float entre 0 y 1

### Pregunta 3: ¿Para qué sirve `pandas`?
Respuesta:

> Para manipular datos tabulares con estructuras como `DataFrame` y series, ideal para análisis y limpieza de datos.

### Pregunta 4: ¿Qué es un `DataFrame`?
Respuesta:

> Es una tabla bidimensional con filas y columnas, comparable a una hoja de Excel.

### Pregunta 5: ¿Qué es Faker?
Respuesta:

> Es una librería para generar datos falsos pero realistas, útiles para pruebas y simulaciones.

### Pregunta 6: ¿Por qué es importante limpiar datos?
Respuesta:

> Porque los datos reales casi siempre tienen valores vacíos, inconsistentes o erróneos; si no se limpian, el análisis puede dar resultados engañosos.

---

## 8. Simulación de entrevista tipo examen

### Entrevista simulada

#### Entrevistador:
¿Puedes explicar qué hace este proyecto y qué librerías están involucradas?

#### Estudiante:
Este proyecto genera datos simulados de árboles y luego los transforma en una tabla con pandas. Para generar valores aleatorios usamos `random`, y para trabajar con el resultado usamos `pandas` y `DataFrame`.

---

#### Entrevistador:
¿Qué es `random.choice()` y cómo se usa aquí?

#### Estudiante:
`random.choice()` selecciona un elemento aleatorio de una lista. En este caso se usa para elegir el nombre del árbol, la dirección, la altura, el estado o el botánico encargado.

---

#### Entrevistador:
Y `random.randint()`, ¿para qué sirve?

#### Estudiante:
Genera un número entero aleatorio entre dos valores. En este proyecto se usa para crear los IDs de cada registro.

---

#### Entrevistador:
¿Y `random.random()`?

#### Estudiante:
Genera un número entre 0 y 1. Aquí se usa para decidir si el registro va a tener un problema o inconsistencia, como un valor nulo o un nombre raro.

---

#### Entrevistador:
¿Qué es exactamente un `DataFrame`?

#### Estudiante:
Es una estructura tabular de pandas. Tiene filas y columnas, y se puede comparar con una tabla de Excel. Permite ordenar, filtrar y analizar datos con mucha facilidad.

---

#### Entrevistador:
¿Para qué sirve `Faker` y por qué podría usarse en lugar de `random`?

#### Estudiante:
`Faker` sirve para generar datos falsos pero muy realistas, como nombres, correos, fechas o direcciones. La diferencia con `random` es que `random` genera valores simples y más genéricos, mientras `Faker` crea datos con contexto y apariencia más natural.

---

#### Entrevistador:
¿Qué pasa si hay datos como `None`, `-10` o textos raros como `"sin"`?

#### Estudiante:
Eso son datos sucios o inconsistentes. En analítica es necesario detectarlos, limpiarlos y corregirlos porque pueden afectar el análisis final.

---

#### Entrevistador:
¿Cómo podrías mejorar este proyecto?

#### Estudiante:
Podría añadir más validaciones, una limpieza más robusta, análisis estadísticos, visualizaciones, y también usar `Faker` para generar datos más realistas. Además, se podría transformar cada registro en una fila más uniforme y consistente.

---

#### Entrevistador:
¿Qué harías si te preguntan en una entrevista: “¿qué es pandas?”

#### Estudiante:
Diría que pandas es una librería de Python para manejo de datos tabulares, muy útil para crear DataFrames, limpiar información, hacer filtros, agrupar datos y preparar datos para análisis o machine learning.

---

#### Entrevistador:
¿Y si te preguntan por `random`?

#### Estudiante:
Respondería que es la librería estándar de Python para trabajar con aleatoriedad, muy útil para simular escenarios, generar pruebas, muestreos y datos aleatorios simples.

---

## 9. Resumen final

Lo más importante para estudiar es esto:

- `random` se usa para generar aleatoriedad
- `random.choice()` elige una opción dentro de una lista
- `random.randint()` genera enteros aleatorios
- `random.random()` genera números flotantes aleatorios entre 0 y 1
- `pandas` organiza los datos en tablas
- `DataFrame` es la estructura central para analizar datos
- `Faker` genera datos falsos pero realistas
- la limpieza de datos es clave para análisis confiables

---

## 10. Guía de repaso rápida

Si vas a presentar un examen oral, memoriza estas respuestas:

- `random` = aleatoriedad en Python
- `choice` = seleccionar al azar un elemento de lista
- `randint` = entero aleatorio en rango
- `DataFrame` = tabla de pandas
- `Faker` = generar datos realistas falsos
- `pandas` = análisis y manipulación de datos
- limpieza = corregir errores para no analizar basura

---

## 11. Sugerencia de práctica

Haz una mini práctica en tu consola:

```python
import random
import pandas as pd

lista = []
for i in range(5):
    lista.append({
        "id": random.randint(1, 100),
        "nombre": random.choice(["pino", "cedro", "sauce"]),
        "estado": random.choice(["optimo", "malo", "mejoria"])
    })

print(lista)
print(pd.DataFrame(lista))
```

Esto te va a servir para explicar en la entrevista que sabes lo que estás haciendo y por qué.

---

## 12. Cierre

Este proyecto no solo muestra Python básico, sino que también representa la lógica de un análisis real: generar datos, detectar errores, organizar la información y prepararla para decisiones futuras.

Si el profesor te hace preguntas sobre `choice`, `random`, `Faker`, `pandas` y `DataFrame`, estas son las ideas clave que debes defender con claridad.
