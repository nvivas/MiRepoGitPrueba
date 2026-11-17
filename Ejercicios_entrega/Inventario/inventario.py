# Un centro educativo necesita organizar los productos informáticos disponibles en un aula. Se dispone de los
# siguientes datos:

# Producto Cantidad Precio unitario
# Teclado 3 24,50 €
# Ratón 2 13,75 €
# Monitor 1 169,90 €

# Desarrolla un programa en Python que realice estas operaciones:
# 1. Crear un diccionario para cada producto con las claves nombre, cantidad y precio.

producto1: dict = {
    "nombre": "Teclado",
    "cantidad": 3,
    "precio": 24.50,
}

producto2: dict = {
    "nombre": "Ratón",
    "cantidad": 2,
    "precio": 13.75,
}

producto3: dict = {
    "nombre": "Monitor",
    "cantidad": 1,
    "precio": 169.90,
}

# 2. Almacenar los tres diccionarios en una lista llamada inventario.
inventario: list = [producto1, producto2, producto3]

# 3. Mostrar por pantalla la lista completa de productos.
print("La lista completa es: ", inventario)

# 4. Mostrar únicamente el nombre del segundo producto de la lista.
print("\nEl nombre del segundo inventario es: ", inventario[1])

# 5. Modificar la cantidad de monitores disponibles, estableciendo su valor en 4.
inventario[2]["cantidad"] = 4

# 6. Añadir a la lista un nuevo producto: nombre «Webcam», cantidad 2 y precio 39.90.
producto4: dict = {
    "nombre": "Webcam",
    "cantidad": 2,
    "precio": 39.90,
}

inventario.append(producto4)

# 7. Eliminar de la lista el producto correspondiente al ratón.

indice = inventario.index(producto2)
inventario.pop(indice)

# 8. Mostrar el inventario actualizado y el número de productos que contiene.
print("\nInventario actualizado: ", inventario)
print("\nNúmero de productos: ", len(inventario), "\n")
