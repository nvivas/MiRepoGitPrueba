# Programa ExcluirUno
# Descripción: Excluye un alumno de un conjunto de alumnos.

# Inicio
students: set = {"Laura", "María", "Nicolás", "Orlando", "Pedro"}

# Lee el nombre del alumno a excluir
excluded: str = input("Introduce el nombre del alumno a excluir: ")

# Muestra el conjunto excluyendo al alumno
print(students - {excluded})
# Fin


# Programa con conjuntos
# Descripción: Realiza la unión de dos conjuntos y muestra el resultado.

# Inicio
a: set = {1, 2, 3}
b: set = {2, 3, 4}

# Realiza la unión de los conjuntos a y b
c: set = a | b

# Muestra el conjunto resultante
print(c)
# Fin


# Programa con conjuntos
# Descripción: Realiza la intersección de dos conjuntos y muestra el resultado.

# Inicio
a: set = {1, 2, 3}
b: set = {2, 3, 4}

# Realiza la intersección de los conjuntos a y b
c: set = a & b

# Muestra el conjunto resultante
print(c)
# Fin
# Programa con conjuntos
# Descripción: Realiza la diferencia entre dos conjuntos y muestra el resultado.
# Devuelve los elementos que están en el primer conjunto pero no en el segundo.

# Inicio
a: set = {1, 2, 3}
b: set = {2, 3, 4}

# Realiza la diferencia de los conjuntos a y b
c: set = a - b

# Muestra el conjunto resultante
print(c)
# Fin

