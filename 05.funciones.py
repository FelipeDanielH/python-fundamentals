# definicion de una funcion

def saludar():
    print("¡Hola, Felipe!")

saludar()  # Llamamos la función

#  funcion con parametros y retorno

def suma(a, b):
    return a + b

resultado = suma(3, 5)
print("Resultado:", resultado)


# funciones con valores por defecto

def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar("Felipe")
saludar()

# funciones anidadas

def operacion():
    def mensaje():
        print("Estoy dentro de una función")

    mensaje()

operacion()

# *args y **kargs

def mostrar_args(*args):
    print("Args:", args)

mostrar_args(1, 2, 3)

def mostrar_kwargs(**kwargs):
    print("Kwargs:", kwargs)

mostrar_kwargs(nombre="Felipe", edad=30)

