"""Funciones: encapsulan bloques de código reutilizables."""


def saludar():
    print("¡Hola, Felipe!")


saludar()


def suma(a, b):
    return a + b


resultado = suma(3, 5)
print("Resultado:", resultado)


def saludar_persona(nombre="invitado"):
    print(f"Hola, {nombre}")


saludar_persona("Felipe")
saludar_persona()


def mostrar_args(*args):
    print("Args:", args)


def mostrar_kwargs(**kwargs):
    print("Kwargs:", kwargs)


mostrar_args(1, 2, 3)
mostrar_kwargs(nombre="Felipe", edad=30)
