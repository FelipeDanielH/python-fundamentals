"""Errores: anticipar problemas y responder con excepciones."""

texto_numero = "42"

# Una entrada externa puede tener un formato inesperado.
try:
    numero = int(texto_numero)
    resultado = 100 / numero
except ValueError:
    # ValueError ocurre si el texto no representa un entero valido.
    print("El valor debe ser un numero entero.")
except ZeroDivisionError:
    # ZeroDivisionError ocurre al dividir por cero.
    print("No se puede dividir por cero.")
else:
    # else se ejecuta solo si no ocurrio ninguna excepcion.
    print("El resultado es:", resultado)
finally:
    # finally se ejecuta tanto si hubo error como si no.
    print("La operacion termino.")

# raise permite indicar que un valor no cumple una regla del programa.
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    return edad


try:
    print("Edad validada:", validar_edad(18))
except ValueError as error:
    print("Error de validacion:", error)

# Prueba: cambia texto_numero por "hola" y luego por "0" para ver dos errores.
