# operaciones/valor_absoluto.py - Cálculo de valor absoluto
# responsable: nayraoviedo / eq1

from .validaciones import es_numero


def calcular_valor_absoluto(a):
    """
    Calcula el valor absoluto de un número.
    Lanza TypeError si a no es un número.
    """
    es_numero(a, "El número")
    return abs(a)