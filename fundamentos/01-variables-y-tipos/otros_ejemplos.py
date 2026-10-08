"""Variables: guardar y reutilizar datos."""

# Una variable es un nombre asociado a un valor. Python deduce el tipo.
nombre = "Lucia"
edad = 20
estatura = 1.68
estudia_python = True

print("Hola,", nombre)
print(f"Tienes {edad} anos y mides {estatura} m.")
print("Estas aprendiendo Python:", estudia_python)

# type() permite inspeccionar el tipo de un valor.
print("Tipo de edad:", type(edad).__name__)

# Una variable puede recibir un nuevo valor (incluso de otro tipo).
edad = edad + 1
print("El proximo ano tendras", edad)

# Prueba: cambia estos valores y agrega una variable para tu ciudad.
