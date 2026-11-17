# Programa SuperiorALaMedia
# Descripción: Determina si los elementos de una lista son superiores a su media.

# Inicio
l: list = []  # Inicializa la lista vacía

# Lee tres números y los agrega a la lista
l = l + [int(input("Introduce el primer número: "))]
l = l + [int(input("Introduce el segundo número: "))]
l = l + [int(input("Introduce el tercer número: "))]

# Calcula la media de los números
mean: float = (l[0] + l[1] + l[2]) / len(l)

# Inicializa una lista vacía para almacenar los resultados
result: list = []

# Comprueba si cada número es superior a la media
result += [l[0] > mean]
result += [l[1] > mean]
result += [l[2] > mean]

# Muestra los resultados
print("Media:", mean)
print(result)
# Fin
