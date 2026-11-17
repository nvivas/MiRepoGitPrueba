# Programa EsPalindromo
# Descripción: Determina si una cadena introducida por teclado es un palíndromo.

# Inicio
cad: str = input("Introduce una cadena: ")

# Comprueba si la cadena es un palíndromo
print(cad == cad[::-1])

lista: list = [1, 2, 3, 4, 5]

print(lista[4:5])  
# Fin
