"""Bucles: repetir instrucciones mientras se cumpla una condición."""

contador = 0
while contador < 3:
    print("Intento", contador)
    contador += 1

print("\nUso de break y continue:")
for i in range(5):
    if i == 3:
        break
    print("i:", i)

for i in range(5):
    if i == 2:
        continue
    print("i con continue:", i)
