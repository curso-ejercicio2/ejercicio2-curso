# operaciones/multiplicacion.py
#Responsable : Darlin Almanza (eq02)
# Responsable: Jhosias Daza Albornoz
# Responsable: Juan Carlos Anagua Kahuana
# Responsable: Joel Mauricio Mamani Mamani (eq06)

def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de a * b

    Raises:
        TypeError: Si alguno de los argumentos no es numérico
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser numéricos")
    return a * b


def multiplicar_lista(valores):
    """
    Multiplica todos los elementos de una lista (producto acumulado).

    Args:
        valores (list): Lista de números

    Returns:
        float: Producto de todos los elementos

    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si algún elemento no es numérico
    """
    if not valores:
        raise ValueError("La lista no puede estar vacía")
    resultado = 1
    for valor in valores:
        if not isinstance(valor, (int, float)):
            raise TypeError(f"El valor '{valor}' no es numérico")
        resultado *= valor
    return resultado


# Responsable: Darlin Almanza (eq02)
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


# Responsable: Joel Mauricio Mamani Mamani (eq06)
def multiplicar_matriz_por_un_escalar (matriz, escalar):
    """
    Multiplica una matriz por un escalar.

    Args:
        matriz (list): Matriz de números
        escalar (float): Número por el cual se multiplica la matriz

    Returns:
        list: Matriz resultante
    """
    filas = len(matriz)
    columnas = len(matriz[0])

    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz[i][j] * escalar

    return resultado
