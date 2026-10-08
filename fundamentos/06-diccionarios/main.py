"""Diccionarios: relacionar claves con valores."""

persona = {
    "nombre": "Mateo",
    "edad": 25,
    "ciudad": "Quito",
}

# Se obtiene un valor usando su clave. get() permite indicar un valor alternativo.
print("Nombre:", persona["nombre"])
print("Pais:", persona.get("pais", "No especificado"))

# Se pueden agregar claves y actualizar valores.
persona["profesion"] = "disenador"
persona["edad"] = 26
print("Datos actualizados:", persona)

# items() entrega pares de clave y valor para recorrer el diccionario.
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Un diccionario tambien puede guardar listas u otros diccionarios.
curso = {
    "nombre": "Python inicial",
    "alumnos": ["Ana", "Leo", "Sol"],
}
print("Alumnos del curso:", len(curso["alumnos"]))

# Prueba: agrega una clave 'hobbies' que contenga una lista de actividades.
