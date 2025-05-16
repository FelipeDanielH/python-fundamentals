
# 📘 Nivel 1: Fundamentos de Python

¡Bienvenido, Felipe! Este es un resumen estructurado y práctico de todo lo que vimos en el Nivel 1, con explicaciones, ejemplos clave y desafíos.

---

## ✅ 1. Instalación y Entorno

- Instala Python desde https://python.org
- Usa `python --version` y `pip --version` para verificar
- Crea entornos virtuales con:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  .\venv\Scripts\activate  # Windows
  ```

---

## 🔤 2. Sintaxis Básica y Tipos de Datos

- `int`, `float`, `str`, `bool`
- `type()` para conocer el tipo
- Conversión: `int("5")`, `str(10)`, `float("3.14")`

```python
edad = 30
nombre = "Felipe"
precio = 9.99
activo = True
```

---

## ➕ 3. Operadores Aritméticos y Lógicos

- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Lógicos: `and`, `or`, `not`
- Comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`

```python
a = 5
b = 3
print(a + b)
print(a > b and b > 0)
```

---

## 🔁 4. Estructuras de Control

### Condicionales
```python
if edad > 18:
    print("Mayor de edad")
elif edad == 18:
    print("Exactamente 18")
else:
    print("Menor de edad")
```

### Bucles
```python
for i in range(5):
    print(i)

while condicion:
    # repetir
    break  # salir
    continue  # salta al siguiente ciclo
```

---

## 📚 5. Colecciones

### list
```python
frutas = ["manzana", "banana"]
frutas.append("pera")
frutas.pop()
```

### tuple
```python
coordenadas = (10, 20)
```

### set
```python
numeros = {1, 2, 3, 1}
numeros.add(4)
```

### dict
```python
usuario = {"nombre": "Felipe", "edad": 30}
usuario["email"] = "felipe@mail.com"
```

---

## 🧠 6. Funciones

```python
def saludar(nombre="Invitado"):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b
```

### *args y **kwargs
```python
def mostrar_args(*args):
    print(args)

def mostrar_kwargs(**kwargs):
    print(kwargs)
```

---

## 📦 7. Módulos y Paquetes

### Crear módulos
```python
# archivo: calculadora.py
def sumar(a, b):
    return a + b

# archivo: app.py
import calculadora
calculadora.sumar(5, 3)
```

### Módulos estándar
```python
import math
math.sqrt(16)

import random
random.randint(1, 6)
```
