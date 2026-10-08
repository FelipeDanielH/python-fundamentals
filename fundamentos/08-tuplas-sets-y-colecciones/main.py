"""Colecciones: listas, tuplas, sets y diccionarios."""

# Lista: ordenada y mutable.
frutas = ["manzana", "banana", "kiwi"]
print("Lista inicial:", frutas)
print("Primera fruta:", frutas[0])
frutas.append("pera")
print("Después de agregar:", frutas)
frutas.pop()
print("Después de quitar:", frutas)

# Tupla: ordenada e inmutable.
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)

# Set: almacena valores únicos sin orden.
numeros = {1, 2, 3, 1, 2}
print("Set:", numeros)
numeros.add(4)
print("Set actualizado:", numeros)

# Diccionario: guarda pares clave-valor.
usuario = {"nombre": "Felipe", "edad": 30}
print("Nombre:", usuario["nombre"])
print("Edad con get():", usuario.get("edad"))
usuario["email"] = "felipe@mail.com"
usuario["edad"] = 31
print("Usuario actualizado:", usuario)
