# operaciones/fibonacci.py

def fibonacci(n):
    """
    Calcula el número de Fibonacci en una posición dada.

    Args:
        n (int): Posición del número de Fibonacci

    Returns:
        int: Número de Fibonacci correspondiente a la posición n
    """
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a

