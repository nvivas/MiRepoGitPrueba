# Programa ContienenA
# Descripción: Lee 3 cadenas y guarda las que contienen la letra 'a'.

# Inicio
cads: list = [
    input("Introduce la primera cadena: "), 
    input("Introduce la segunda cadena: "), 
    input("Introduce la tercera cadena: ")
]

result: list = []

# Comprueba si cada cadena contiene la letra 'a'

if "a" in cads[0]:
    result += [cads[0]]

if "a" in cads[1]:
    result += [cads[1]]

if "a" in cads[2]:
    result += [cads[2]]

# Muestra las cadenas que contienen la letra 'a'
print(result)
# Fin
