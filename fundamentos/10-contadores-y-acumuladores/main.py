"""Contadores y acumuladores: resumir datos al recorrerlos."""

notas = [8, 5, 10, 7, 6, 9, 4]
aprobadas = 0
suma_notas = 0

# Un contador aumenta por cada elemento que cumple una condicion.
# Un acumulador guarda un total que se va actualizando.
for nota in notas:
    suma_notas += nota
    if nota >= 6:
        aprobadas += 1

promedio = suma_notas / len(notas)
print("Cantidad de notas:", len(notas))
print("Notas aprobadas:", aprobadas)
print(f"Promedio: {promedio:.2f}")

# count() cuenta cuantas veces aparece un valor concreto.
votos = ["azul", "rojo", "azul", "verde", "azul", "rojo"]
print("Votos por azul:", votos.count("azul"))

# Un diccionario sirve para contar varios valores en una sola pasada.
conteo = {}
for voto in votos:
    conteo[voto] = conteo.get(voto, 0) + 1
print("Conteo de votos:", conteo)

# Prueba: cambia la nota minima para aprobar y observa como varia el contador.
