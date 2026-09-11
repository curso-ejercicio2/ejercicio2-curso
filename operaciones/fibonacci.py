# operaciones/fibonacci.py
# Responsables:
#   - Jonas Vidal Zenzano (eq03)          # autor original
#   - Ian Nicolas Flores Candia (eq06)    # refactorizó y agregó validaciones

def fibonacci(n):
    """
    Calcula el número de Fibonacci en una posición dada.

    Args:
        n (int): Posición del número de Fibonacci

    Returns:
        int: Número de Fibonacci correspondiente a la posición n
    """
    if not isinstance(n, int):
        raise TypeError("El índice debe ser un número entero")
    if n < 0:
        raise ValueError("El índice no puede ser negativo")

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a