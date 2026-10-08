"""Cadenas de texto: crear, consultar y transformar texto."""

frase = "  aprender Python es divertido  "

# strip() quita espacios de los extremos, no los del interior.
limpia = frase.strip()
print("Texto limpio:", limpia)
print("En mayusculas:", limpia.upper())
print("En minusculas:", limpia.lower())
print("Empieza con 'aprender':", limpia.startswith("aprender"))
print("Cantidad de caracteres:", len(limpia))

# Las cadenas son secuencias: se pueden consultar por indice o por partes.
print("Primer caracter:", limpia[0])
print("Primeras ocho letras:", limpia[:8])

# replace() devuelve una nueva cadena; no modifica la original.
reemplazada = limpia.replace("divertido", "interesante")
print("Texto cambiado:", reemplazada)

# f-strings insertan valores dentro de una cadena.
tema = "cadenas"
print(f"Hoy practicamos {tema} en Python.")

# Prueba: cuenta cuantas veces aparece una letra con limpia.count("a").
