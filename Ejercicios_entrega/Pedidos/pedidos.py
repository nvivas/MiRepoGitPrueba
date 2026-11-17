# Una tienda de informática almacena sus pedidos mediante una lista de diccionarios. Los datos iniciales son:

# pedidos = [
#  {"codigo": "A1", "producto": "SSD", "unidades": 2, "precio": 58},
#  {"codigo": "A2", "producto": "RAM", "unidades": 3, "precio": 32},
#  {"codigo": "A3", "producto": "SSD", "unidades": 1, "precio": 58}
# ]

# Desarrolla un programa en Python que realice estas operaciones:
# 1. Crear una lista llamada pedidos con los tres diccionarios proporcionados.
pedidos = [
    {"codigo": "A1", "producto": "SSD", "unidades": 2, "precio": 58},
    {"codigo": "A2", "producto": "RAM", "unidades": 3, "precio": 32},
    {"codigo": "A3", "producto": "SSD", "unidades": 1, "precio": 58}
]

# 2. Mostrar por pantalla la lista completa de pedidos.
print("Lista completa de pedidos: ", pedidos)

# 3. Mostrar únicamente el nombre del producto correspondiente al primer pedido.
print("El producto correspondiente al primer pedido es: ", pedidos[0]["producto"])

# 4. Mostrar el número de unidades del segundo pedido.
print("El número de unidades del segundo pedido es: ", pedidos[1]["unidades"])

# 5. Modificar las unidades del tercer pedido, estableciendo su valor en 5.
pedidos[2]["unidades"] = 5

# 6. Añadir a la lista un nuevo pedido con código «A4», producto «Teclado», unidades 4 y precio 25.
pedido: dict = {"codigo": "A4", "producto": "Teclado", "unidades": 4, "precio": 25}
pedidos.append(pedido)

# 7. Eliminar de la lista el segundo pedido.
pedidos.remove(pedidos[1])

# 8. Mostrar por pantalla la lista de pedidos actualizada.
print("Lista de pedidos: ", pedidos)

# 9. Mostrar el número total de pedidos almacenados en la lista.
print("Total de pedidos almacenados: ", len(pedidos))

print()
