# Un centro educativo necesita almacenar las calificaciones de varios estudiantes mediante un diccionario:
# Estudiante Actividad 1 Actividad 2 Actividad 3
# Alicia 7 8 6
# Bruno 5 4 6
# Celia 9 8 9
# Diego 6 6 5
# Desarrolla un programa en Python que realice estas operaciones:

# 1. Crear un diccionario llamado calificaciones en el que cada clave sea el nombre de un estudiante y su valor
# sea una lista con sus tres calificaciones.

calificaciones: dict = {
    "Alicia": [7, 8, 6],
    "Bruno": [5, 4, 6],
    "Celia": [9, 8, 9],
    "Diego": [6, 6, 5]
}


# 2. Mostrar por pantalla el diccionario completo.
print("El diccionario completo es:", calificaciones)

# 3. Mostrar únicamente las calificaciones de Alicia.
print("Las calificaciones de Alicia son: ", calificaciones["Alicia"])

# 4. Mostrar la nota de la segunda actividad de Bruno.
print("La segunda nota de Bruno es: ", calificaciones["Bruno"][1])

# 5. Modificar la tercera calificación de Diego, sustituyendo su valor por 7.
calificaciones["Diego"][2] = 7

# 6. Añadir una nueva estudiante llamada Elena con las calificaciones [8, 7, 9].
calificaciones["Elena"] = [8, 7, 9]

# 7. Eliminar del diccionario al estudiante Bruno.
del calificaciones["Bruno"]

# 8. Mostrar el diccionario actualizado, los nombres de los estudiantes mediante keys(), las listas de
# calificaciones mediante values() y el número total de estudiantes.

print("Las calificaciones actualizadas son: ",calificaciones)

# Obtener claves
nombres = list(calificaciones.keys())
print("Las claves son: ", nombres)

# Obtener valores
valores = list(calificaciones.values())  
print("Los valores son: ", valores)

print("El número total de estudiantes es:", len(nombres), "estudiantes\n")

