"""Sintaxis básica: variables, tipos y salida."""

# Una variable guarda un valor y Python infiere su tipo.
nombre = "Felipe"
edad = 30
altura = 1.75
es_estudiante = True

print("Hola,", nombre)
print("Edad:", edad, "Tipo:", type(edad).__name__)
print("Altura:", altura, "Tipo:", type(altura).__name__)
print("¿Es estudiante?", es_estudiante, "Tipo:", type(es_estudiante).__name__)

# También puedes convertir valores entre tipos.
numero_texto = "42"
numero = int(numero_texto)
print("Texto convertido a entero:", numero)
print("Entero convertido a cadena:", str(numero))
