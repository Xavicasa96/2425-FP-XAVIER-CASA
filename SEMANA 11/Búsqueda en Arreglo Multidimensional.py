# Programa 1: Búsqueda en Arreglo Multidimensional

# Crear una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Valor a buscar
valor_buscado = int(input("Introduce el valor a buscar: "))

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
