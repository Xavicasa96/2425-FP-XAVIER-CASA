# Programa 2: Ordenación de Arreglo Multidimensional

# Crear una matriz 3x3
matriz = [
    [9, 7, 5],
    [3, 2, 1],
    [6, 8, 4]
]

# Función para ordenar una fila usando el algoritmo Bubble Sort
def ordenar_fila(matriz, fila):
    # Implementación de Bubble Sort
    for i in range(len(matriz[fila]) - 1):
        for j in range(len(matriz[fila]) - 1 - i):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambio de elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar
fila_a_ordenar = int(input("Introduce el número de la fila a ordenar (0, 1, 2): "))

# Llamar a la función para ordenar la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de ordenar la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)

