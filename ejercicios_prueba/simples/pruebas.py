

numero1: int = int(input("Introduce un número: "))
numero2: int = int(input("Introduce otro número: "))
numero3: int = int(input("Introduce un tercer número: "))

lista: list[int] = [numero1, numero2, numero3]

fijo: int = 5

print("El resultado del primer número es:", lista[0] + fijo)
print("El resultado del segundo número es:", lista[1] + fijo)
print("El resultado del tercer número es:", lista[2] + fijo)
