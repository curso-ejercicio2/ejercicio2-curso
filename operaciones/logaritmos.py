# operaciones/logaritmos.py

import math

def calcular_logaritmo(numero, base=2):
    """
    Calcula el logaritmo de un número en una base dada.

    Args:
        numero (float): Argumento del logaritmo (debe ser mayor que 0)
        base (float): Base del logaritmo (por defecto 2, debe ser > 0 y distinta de 1)

    Returns:
        float: Resultado de log_base(numero)

    Raises:
        ValueError: Si numero <= 0, base <= 0 o base == 1
    """
    if numero <= 0:
        raise ValueError("El argumento del logaritmo debe ser mayor que cero")
    if base <= 0 or base == 1:
        raise ValueError("La base del logaritmo debe ser mayor que cero y distinta de 1")

    return math.log(numero, base)
