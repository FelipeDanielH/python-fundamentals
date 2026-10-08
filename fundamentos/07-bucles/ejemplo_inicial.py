contador = 0

while contador < 3:
    print("Intento", contador)
    contador += 1

#  Break y continue

for i in range(5):
    if i == 3:
        break  # Detiene el bucle
    print("i:", i)

for i in range(5):
    if i == 2:
        continue  # Salta esta vuelta
    print("i con continue:", i)