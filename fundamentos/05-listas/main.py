"""Listas: colecciones ordenadas que se pueden modificar."""

frutas = ["manzana", "pera", "uva"]
print("Lista inicial:", frutas)

# Las posiciones empiezan en cero.
print("Primera fruta:", frutas[0])
print("Ultima fruta:", frutas[-1])

# append agrega al final; remove elimina el valor indicado.
frutas.append("naranja")
frutas.remove("pera")
print("Despues de agregar y quitar:", frutas)

# Un for visita cada elemento de la lista.
print("Frutas disponibles:")
for fruta in frutas:
    print("-", fruta)

# len() cuenta elementos y sum() suma valores numericos.
precios = [1.25, 2.50, 0.90]
print("Cantidad de precios:", len(precios))
print("Total:", sum(precios))

# Una comprension crea una lista nueva aplicando una expresion a cada elemento.
mayusculas = [fruta.upper() for fruta in frutas]
print("Nombres en mayusculas:", mayusculas)

# Prueba: agrega otra fruta y crea una lista solo con nombres de mas de 4 letras.
