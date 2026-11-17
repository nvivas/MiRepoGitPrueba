print("\033c", end="")

# Ignacio Vivas Martín

nombre: str = "Ignacio"
apellido: str = "Vivas"
apellido2: str = "Martín"

lista: list = [nombre, apellido, apellido2]

print(lista)

ininombre = list(nombre)
iniapellido = list(apellido)
iniapellido2 = list(apellido2)

print(ininombre[0] + iniapellido[0] + iniapellido2[0])

rango = list(range(1,11, 1))

print(rango)
rango.append(11)
print(rango)
rango.remove(5)
print(rango)
rango.sort(reverse=True)
print(rango)
print(len(rango))

print("Python".upper().replace("PY", "pi"))

numeros = [23, 67, 45, 89, 12, 55, 78, 34, 91]
numero = [numero for numero in numeros if numero >= 50]
print(numero)
