print("\033c", end="")

# lista con set
conjunto: set = {3, 3, 1}
print(conjunto) #aparacerá {1, 3} porque los sets no admiten elementos repetidos

texto: str = "Hola"
# Cadenas
print(texto[0]) # Muestra H, la primera letra de la cadena
texto += "!"
print(texto) # Muestra Hola!

print("--------------------------------")
# Creación de cadenas
mensaje = "Hola, mundo"

# Acceso a caracteres (indexación)
print(mensaje[0])  # 'H' (primer carácter)
print(mensaje[-1]) # 'o' (último carácter)

# Slicing (subcadenas)
print(mensaje[0:4])  # "Hola"

# Concatenación (unión de dos cadenas de texto)
nombre = "Ana"
saludo = "Hola, " + nombre  # "Hola, Ana"

# Longitud de una cadena
print(len(mensaje))  # 11

print("--------------------------------")
# Mayúsculas y minúsculas
texto = "Python"
print(texto.upper())  # "PYTHON" pasa texto a mayúsculas
print(texto.lower())  # "python" pasa texto a minúsculas

# Búsqueda y reemplazo
frase = "Aprendiendo Python"
print(frase.find("Python"))  # 12 (posición donde empieza) Recuerda que la primera posición es el 0
print(frase.replace("Python", "programación"))  # "Aprendiendo programación" Sustituye Python por programación

# División y unión
palabras = frase.split(" ")  # ["Aprendiendo", "Python"]
nueva_frase = "-".join(palabras)  # "Aprendiendo-Python"

# Otros métodos
texto = "   Python es genial!   "
print(texto.strip())  # Elimina espacios: "Python es genial!"
print(texto.startswith("Python"))  # False (por los espacios)
print("genial" in texto)  # True (búsqueda de subcadena)

print("--------------------------------")

texto = "El perro persigue al gato. El gato escapa del perro."

# Contar ocurrencias
print(texto.count("perro"))  # 2

# Encontrar posición
print(texto.find("gato"))  # 17 (primera ocurrencia)
print(texto.rfind("gato"))  # 36 (última ocurrencia)

# Reemplazo múltiple
reemplazos = {"perro": "can", "gato": "felino"}
for k, v in reemplazos.items():
    texto = texto.replace(k, v)
print(texto)  # "El can persigue al felino. El felino escapa del can."

print("--------------------------------")

nombre = "Ana"
edad = 28
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
# Salida: "Hola, me llamo Ana y tengo 28 años."

print("--------------------------------")

# Operaciones matemáticas
print(f"El doble de 5 es {5 * 2}")  # Salida: "El doble de 5 es 10"

# Formateo de números
pi = 3.141592
print(f"Valor de PI: {pi:.2f}")  # Salida: "Valor de PI: 3.14"

# Llamadas a funciones
def calcular_iva(precio):
    return precio * 0.21

print(f"El IVA de 100€ es {calcular_iva(100):.2f}€")  # Salida: "El IVA de 100€ es 21.00€"

print("--------------------------------")

print("Hola, me llamo {} y tengo {} años.".format("Ana", 28))
# Salida: "Hola, me llamo Ana y tengo 28 años."
# print("Hola, me llamo {} y tengo {} años.".format(input("Introduce tu nombre: "), input("Introduce tu edad: ")))
# Salida: "Hola, me llamo [nombre] y tengo [edad] años." con los valores introducidos por el usuario.

print("--------------------------------")

# Referencia por posición
print("{1} tiene {0} años".format(25, "Carlos"))  # Salida: "Carlos tiene 25 años"

# Formateo de números
precio = 49.99
print("Precio: ${:.2f}".format(precio))  # Salida: "Precio: $49.99"

# Alineación de texto
print("{:<10} | {:^10} | {:>10}".format("Izquierda", "Centro", "Derecha"))
# Salida: "Izquierda |   Centro   |   Derecha"
print("--------------------------------")
nombre = "Luis"
edad = 35
print("Hola, soy " + nombre + " y tengo " + str(edad) + " años.")
# Salida: "Hola, soy Luis y tengo 35 años."

print("--------------------------------")


print("--------------------------------")