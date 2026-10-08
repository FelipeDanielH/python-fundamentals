# este es el archivo que debemos ejecutar para iniciar el programa principal con 'python 06.modulos/app.py'

import calculadora
import math
import random

print(calculadora.sumar(5, 3))
print(calculadora.restar(10, 4))

# extra: modulo math y random



print(math.sqrt(25))       # raíz cuadrada
print(math.pi)             # constante pi
print(math.pow(2, 3))      # 2^3



print(random.randint(1, 10))     # Número aleatorio del 1 al 10
print(random.choice(["sol", "nube", "lluvia"]))  # elige aleatorio
