# operaciones/fibonacci.py
# Responsables:
#   - Jonas Vidal Zenzano (eq03)          # autor original
#   - Ian Nicolas Flores Candia (eq06)    # refactorizó y agregó validaciones

from .validaciones import es_entero, no_negativo


def fibonacci(n):
    """
    Calcula el número de Fibonacci en una posición dada.

    Args:
        n (int): Posición del número de Fibonacci

    Returns:
        int: Número de Fibonacci correspondiente a la posición n
    """
    no_negativo(n, "La posición")
    es_entero(n, "La posición")

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a