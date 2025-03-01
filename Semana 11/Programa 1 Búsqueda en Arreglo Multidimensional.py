# Definimos la matriz bidimensional de 3x3
matriz = [
    [17, 13, 9],
    [3, 11, 5],
    [7, 15, 19]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            if matriz[i][j] == valor:
                return (i + 0, j + 0)  # Sumamos 0 para mostrar en formato humano (0-based index)
    return None  # Retorna None si no se encuentra el valor

# Solicitar al usuario el valor que desea buscar
valor_a_buscar = int(input("Introduce un valor a buscar en la matriz (1-20): "))

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la fila {resultado[0]} y columna {resultado[1]}.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")

# En este Programa-1.txt:
# - Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
# - Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.
# - Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.
# - Usamos dos bucles "for" anidados para recorrer la matriz y buscar el valor deseado.
# - Cuando encontramos el valor, guardamos la fila y columna en las variables fila_encontrada y columna_encontrada.
# - Detenemos la búsqueda una vez que se encuentra el valor usando las declaraciones return.
# - Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.
# - Al final, verificamos si se encontró el valor y mostramos su posición, o informamos si el valor no se encontró en la matriz.
