# operaciones/valor_absoluto.py - Cálculo de valor absoluto
# responsable: nayraoviedo / eq1

def calcular_valor_absoluto(a):
    """
    Calcula el valor absoluto de un número.
    Lanza TypeError si a no es un número.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("El argumento debe ser un número")
    return abs(a)