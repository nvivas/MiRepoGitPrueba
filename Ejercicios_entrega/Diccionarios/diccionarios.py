# Desarrolla un programa en Python que permita almacenar y consultar información de productos mediante
# diccionarios.

# 1. Crear un diccionario llamado productos con cuatro productos: Teclado, Ratón, Monitor y Webcam. 
# Cada clave será el nombre del producto y cada valor, su precio (elegido libremente).

productos: dict = {
    "Teclado": 20,
    "Ratón": 10,
    "Monitor": 120,
    "Webcam": 50
}

# 2. Crear un nuevo diccionario llamado seleccionados que contenga solamente los productos Teclado y Ratón.
# Para obtener sus precios, acceder al diccionario original mediante sus claves.

seleccionados: dict = {
    "Teclado": productos["Teclado"],
    "Ratón": productos["Ratón"],
}

# 3. Mostrar por pantalla el diccionario productos y el nuevo diccionario seleccionados.
print("El diccionario de productos es: ", productos)
print("El nuevo diccionario seleccionado es: ", seleccionados)
print()