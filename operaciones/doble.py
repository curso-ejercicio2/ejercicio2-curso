# operaciones/doble.py
# Responsable: Fabio Inturias Vera (eq06)

from .validaciones import es_numero


def doble(a):
    """
    Calcula el doble de un número.

    Args:
        a (float): Número al que se le calculará el doble.

    Returns:
        float: Resultado de multiplicar a por 2.
    """
    es_numero(a, "El número")
    return a * 2