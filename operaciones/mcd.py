# operaciones/mcd.py

# Responsable: Abad Alvaro Villca Gutierrez (eq01)

from .validaciones import es_numero


def calcular_mcd(a, b):
    """
    Calcula el máximo común divisor de dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Máximo común divisor de a y b.
    """
    es_numero(a, "El primer número")
    es_numero(b, "El segundo número")

    while b:
        a, b = b, a % b

    return abs(a)