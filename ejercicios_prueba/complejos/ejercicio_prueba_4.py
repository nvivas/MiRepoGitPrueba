# Programa DeterminaDelegado
# Descripción: Determina el delegado de la clase a partir de 5 papeletas.

# Inicio
result: list = [0, 0]  # El primer elemento es para Ángela, el segundo para Rubén.

for i in range(5):      # 0, 1, 2, 3, 4
    if input("Vota por Ángela o Rubén: ") == "Ángela":
        result[0] += 1
    else:
        result[1] += 1
# Primera papeleta
# if input("Vota por Ángela o Rubén: ") == "Ángela":
#     result[0] += 1
# else:
#     result[1] += 1

# # Segunda papeleta
# if input("Vota por Ángela o Rubén: ") == "Ángela":
#     result[0] += 1
# else:
#     result[1] += 1

# # Tercera papeleta
# if input("Vota por Ángela o Rubén: ") == "Ángela":
#     result[0] += 1
# else:
#     result[1] += 1

# # Cuarta papeleta
# if input("Vota por Ángela o Rubén: ") == "Ángela":
#     result[0] += 1
# else:
#     result[1] += 1

# # Quinta papeleta
# if input("Vota por Ángela o Rubén: ") == "Ángela":
#     result[0] += 1
# else:
#     result[1] += 1

# Determina el ganador
if result[0] > result[1]:
    print("La ganadora es Ángela")
else:
    print("El ganador es Rubén")
# Fin
