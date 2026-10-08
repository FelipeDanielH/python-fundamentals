"""Funciones: agrupar instrucciones para poder reutilizarlas."""


def saludar(nombre):
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}!"


def calcular_total(precio, cantidad=1):
    """Calcula el precio por cantidad; cantidad tiene un valor por defecto."""
    return precio * cantidad


def es_par(numero):
    """Indica si un numero es divisible por dos."""
    return numero % 2 == 0


# Llamar una funcion ejecuta su bloque y permite usar el valor retornado.
mensaje = saludar("Marta")
print(mensaje)

print("Un cuaderno cuesta:", calcular_total(3.50))
print("Tres cuadernos cuestan:", calcular_total(3.50, 3))

numero = 8
if es_par(numero):
    print(numero, "es par")
else:
    print(numero, "es impar")

# Prueba: crea una funcion que reciba una temperatura en Celsius y la convierta
# a Fahrenheit. La formula es Fahrenheit = Celsius * 9 / 5 + 32.
