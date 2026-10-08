"""Condicionales: elegir que hacer segun una condicion."""

temperatura = 23

# if ejecuta su bloque cuando la condicion es verdadera.
if temperatura >= 30:
    mensaje = "Hace calor."
elif temperatura >= 18:
    # elif permite comprobar otra condicion si la anterior no se cumplio.
    mensaje = "El clima esta agradable."
else:
    mensaje = "Hace frio."

print(mensaje)

# Las comparaciones producen True o False.
edad = 17
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Puedes entrar.")
elif edad >= 18 and not tiene_permiso:
    print("Necesitas permiso.")
else:
    print("Aun no tienes la edad necesaria.")

# in comprueba si un elemento pertenece a una secuencia.
dia = "sabado"
if dia in ("sabado", "domingo"):
    print("Es fin de semana.")
else:
    print("Es dia laborable.")

# Prueba: cambia temperatura, edad y dia para recorrer distintas ramas.
