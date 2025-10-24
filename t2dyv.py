import random

# Conjunto de vocales
VOCALES = set('aeiou')

# Generar una palabra aleatoria de 4 letras
def palabra_random():
    return ''.join(chr(random.randint(97, 122)) for _ in range(4))

# Generar la matriz cuadrada con palabras aleatorias
def generar_matriz(tamaño):
    return [[palabra_random() for _ in range(tamaño)] for _ in range(tamaño)]

# Verificar si una palabra contiene al menos una vocal
def contiene_vocal(palabra):
    return any(letra in VOCALES for letra in palabra)

# Algoritmo divide y vencerás para contar palabras con vocales
def DyV(matriz):
    n = len(matriz)
    if n == 1:  # Caso base: matriz de 1x1
        return 1 if contiene_vocal(matriz[0][0]) else 0

    mitad = n // 2
    # Dividimos la matriz en 4 submatrices
    A = [fila[:mitad] for fila in matriz[:mitad]]
    B = [fila[mitad:] for fila in matriz[:mitad]]
    C = [fila[:mitad] for fila in matriz[mitad:]]
    D = [fila[mitad:] for fila in matriz[mitad:]]

    # Llamadas recursivas
    return DyV(A) + DyV(B) + DyV(C) + DyV(D)

# Imprimir la matriz en forma de cuadrado
def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))

# Programa principal
if __name__ == "__main__":
    tamaño = int(input("Ingrese el tamaño de la matriz (por ejemplo 8): "))
    matriz = generar_matriz(tamaño)

    print("\nMatriz generada:")
    imprimir_matriz(matriz)

    total_con_vocal = DyV(matriz)
    print(f"\nCantidad de palabras con al menos una vocal: {total_con_vocal}")

