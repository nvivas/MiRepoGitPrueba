# Programa Lee3Suma5
# Descripción: Lee 3 números y les suma 5.

# Inicio
l: list = []  # Inicializa la lista vacía

# Lee el primer número y lo agrega a la lista
l = l + [int(input("Introduce el primer número: "))]

# Lee el segundo número y lo agrega a la lista
l = l + [int(input("Introduce el segundo número: "))]

# Lee el tercer número y lo agrega a la lista
l = l + [int(input("Introduce el tercer número: "))]

# Suma 5 a cada número de la lista
l[0] = l[0] + 5
l[1] = l[1] + 5
l[2] = l[2] + 5

# Muestra la lista con los nuevos valores
print(l)
# Fin


# Programa Primera
# Descripción: Muestra la primera letra de una cadena.

# Inicio
cad: str = input("Introduce una cadena: ")

# Muestra la primera letra de la cadena
print(cad[0])
# Fin

