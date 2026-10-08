"""Condicionales: elegir una ruta según una condición."""

edad = 17

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres menor de edad.")

nota = 8

if nota >= 6 and nota <= 10:
    print("Aprobado")
elif nota < 6 and nota >= 0:
    print("Reprobado")
else:
    print("Nota inválida")

# También se puede comprobar si un valor está dentro de varios posibles.
dia = "sábado"
if dia in ("sábado", "domingo"):
    print("Es fin de semana.")
else:
    print("Es día laborable.")
