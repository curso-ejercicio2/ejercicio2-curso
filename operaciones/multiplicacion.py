# operaciones/multiplicacion.py

def multiplicar(a, b):
    """
    Multiplica dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
    
    Returns:
        float: Resultado de a * b
    """
    return a * b

def multiplicar_matriz (matriz_a, matriz_b):
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0])
    columnas_b = len(matriz_b[0])

    resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado