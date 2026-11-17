# Definición de variables para comparación de identidad
a: list = [1, 2, 3]
b: list = [1, 2, 3]
c = a  # c es la misma referencia que a

# Operador de identidad (is)
print("a is b: ", a is b)  # False, porque a y b son listas diferentes en la memoria
print("a is c: ", a is c)  # True, porque c es la misma referencia que a

# Operador de no identidad (is not)
print("a is not b: ", a is not b)  # True, porque a y b no son la misma lista en la memoria
print("a is not c: ", a is not c)  # False, porque a y c son la misma referencia
