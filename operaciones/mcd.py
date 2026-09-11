# operaciones/mcd.py

# Responsable: Abad Alvaro Villca Gutierrez (eq03)
def calcular_mcd(a, b):
    """
    Calcula el máximo común divisor de dos números.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Máximo común divisor de a y b.
    """
    while b:
        a, b = b, a % b

    return abs(a)