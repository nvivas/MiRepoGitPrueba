# Inicialización de variables simples
x = 10  # Variable entera
y = 20.5  # Variable de punto flotante

# Coloca un breakpoint aquí para observar los valores de x e y
z = x + y  # Suma de un entero y un flotante

# Inicialización de una lista (tipo complejo)
mi_lista = [1, 2, 3, 4, 5]

# Añadir un nuevo elemento a la lista
mi_lista.append(z)

# Coloca un breakpoint aquí para observar el valor de 'mi_lista'
# Inicialización de un diccionario (tipo complejo)
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "altura": 1.75
}

# Modificar un valor del diccionario
mi_diccionario["edad"] = 31

# Operaciones simples con cadenas
saludo = "Hola"
nombre = mi_diccionario["nombre"]
mensaje_completo = saludo + ", " + nombre

# Coloca otro breakpoint aquí para observar los valores de las cadenas y el diccionario
# Imprimir el mensaje completo
print(mensaje_completo)

# Operaciones con una lista y un diccionario
suma_edades = mi_diccionario["edad"] + mi_lista[0]

# Coloca un breakpoint aquí para observar los valores finales
print("La suma de las edades y el primer valor de la lista es:", suma_edades)