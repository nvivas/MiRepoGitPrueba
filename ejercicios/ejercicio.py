# Crea un programa que lea dos números por teclado y muestre por pantalla los resultados de las operaciones básicas: suma, resta, multiplicación y división.

number: int = int(input("Introduce un número: "))
numero: int = int(input("Introduce otro número: "))

print("Suma: ", number + numero)
print("Resta: ", number - numero)
print("Multiplicación: ", number * numero)
print("División: ", number / numero)


# Crea un programa que lea tres números por teclado y determine si los dos primeros son más pequeños que el último.


number1: int = int(input("Introduce el primer número: "))
number2: int = int(input("Introduce el segundo número: "))
number3: int = int(input("Introduce el tercer número: "))

print("Los dos primeros números son más pequeños que el último: ", number1 < number3 and number2 < number3)
