# listas:
# guarda multiples valores en orden y es mutable

frutas = ["manzana", "banana", "kiwi"]

print(frutas[0])        # manzana
frutas.append("pera")   # agrega al final
print(frutas)

frutas.pop()            # quita el último elemento
print(frutas)

# tuplas:
# son como listas pero inmutables

coordenadas = (10, 20)
print(coordenadas[0])  # 10

# coordenadas[1] = 50  Esto lanza un error

#  set
#  contiene elemntos unicos y sin orden

numeros = {1, 2, 3, 1, 2}
print(numeros)  # Resultado: {1, 2, 3}

numeros.add(4)
print(numeros)

# diccionarios
# guarda datos en clave/valor

usuario = {
    "nombre": "Felipe",
    "edad": 30
}

print(usuario["nombre"])          # Felipe
print(usuario.get("edad"))        # 30

usuario["edad"] = 31              # Modificar
usuario["email"] = "felipe@mail.com"  # Agregar nuevo campo

print(usuario)

