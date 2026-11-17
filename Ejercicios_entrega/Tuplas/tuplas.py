# Desarrolla un programa en Python que permita almacenar y consultar los días de la semana mediante una
# tupla.

# 1. Solicitar al usuario, uno a uno, los nombres de los siete días de la semana, comenzando por el lunes.
# Mostrar mensajes como «Introduce el nombre del día 1», «Introduce el nombre del día 2», etc.
lunes: str = input("Introduce el día 1 de la semana: ")
martes: str = input("Introduce el día 2 de la semana: ")
miercoles: str = input("Introduce el día 3 de la semana: ")
jueves: str = input("Introduce el día 4 de la semana: ")
viernes: str = input("Introduce el día 5 de la semana: ")
sabado: str = input("Introduce el día 6 de la semana: ")
domingo: str = input("Introduce el día 7 de la semana: ")

# 2. Almacenar los siete nombres introducidos en una tupla, respetando el orden de entrada.
semana: tuple = (lunes, martes, miercoles, jueves, viernes, sabado, domingo)

# 3. Solicitar al usuario un número entero comprendido entre 1 y 7.
numero: int = int(input("Introduce un número del 1 al 7: "))

# 4. Mostrar por pantalla el día de la semana correspondiente al número introducido (lunes = 1; domingo = 7).
print("El día correspondiente es:", semana[numero - 1])
print()
