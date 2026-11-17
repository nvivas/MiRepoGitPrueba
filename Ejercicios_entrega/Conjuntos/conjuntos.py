# Desarrolla un programa en Python que realice operaciones entre dos conjuntos de números enteros.

# 1. Crear los conjuntos A = {1, 2, 3, 4, 5} y B = {4, 5, 6, 7, 8}.

A: set = {1, 2, 3, 4, 5}
B: set = {4, 5, 6, 7, 8}

print("Conjunto creado A:", A)
print("Conjunto creado B:", B)

# 2. Calcular y mostrar la unión de A y B.

union = A | B
print("La unión de A y B es: ", union)

# 3. Calcular y mostrar la intersección de A y B.

interseccion = A & B
print("La intersección de A y B es: ", interseccion)

# 4. Calcular y mostrar la diferencia de A respecto de B (A − B).

diferencia = A - B
print("La diferencia de A y B es: ", diferencia)

# Cada resultado debe ir acompañado de un mensaje que identifique la operación realizada.

print()

