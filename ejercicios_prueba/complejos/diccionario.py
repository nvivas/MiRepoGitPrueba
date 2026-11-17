# Programa con diccionario
# Descripción: Muestra un valor de un diccionario y añade un nuevo par clave-valor.

# Inicio
d: dict = {
    "nombre": "Pepe",
    "edad": 18,
    "FP": True,
    "hermanos": ["Víctor", "Andrea"]
}

# Muestra el valor de la clave "edad"
print(d["edad"])

# Muestra todo el conjunto del diccionario antes de la modificación
print(d)

# Añade una nueva clave "colorOjos" con valor "Verde"
d["colorOjos"] = "Verde"

# Muestra todo el conjunto del diccionario después de la modificación
print(d)
# Fin
