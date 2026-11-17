# Desarrolla un programa en Python que permita realizar las siguientes operaciones sobre una lista de números
# enteros:


# 1. Crear una lista que contenga los números enteros del 1 al 10, ambos incluidos.
lista = list(range(1, 11))

# 2. Modificar el elemento que ocupa la quinta posición de la lista, sustituyendo su valor por 99.
lista[4] = 99

# 3. Añadir el número 11 al final de la lista.
lista.append(11)

# 4. Eliminar de la lista el elemento cuyo valor sea 7.
lista.remove(7)

# 5. Mostrar por pantalla la lista resultante y el número total de elementos que contiene.
print("La lista resultante es:", lista)
print("Número de elementos:", len(lista))
print()

