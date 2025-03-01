# Definimos la matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [17, 13, 9],
    [3, 11, 5],
    [15, 7, 19]
]

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    print()

# Algoritmo de Bubble Sort para ordenar una fila específica
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Función para ordenar una fila específica de la matriz
def ordenar_fila_matriz(matriz, fila):
    if fila < len(matriz):
        print(f"Matriz Original:")
        mostrar_matriz(matriz)

        print(f"Ordenando la fila {fila + 1}...\n")
        bubble_sort(matriz[fila])

        print(f"Matriz con la fila {fila + 1} ordenada:")
        mostrar_matriz(matriz)
    else:
        print("Fila fuera de rango.")

# Solicitar al usuario qué fila ordenar
fila_a_ordenar = int(input("Introduce el número de la fila a ordenar (1-3): ")) - 1

# Llamada a la función para ordenar la fila
ordenar_fila_matriz(matriz, fila_a_ordenar)

# En este Programa-2.txt:
# - Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
# - Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.
# - Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo
#   de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).
# - Muestra la matriz original y la matriz con la fila ordenada.
# - Se muestra las dos matrices la primera corresponde a la original y la segunda a la ordenada segun eligio el usuario.