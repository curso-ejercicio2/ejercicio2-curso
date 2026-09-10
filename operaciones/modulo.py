# operaciones/modulo.py

def calcular_modulo(a: float, b: float) -> float:
    """
    Calcula el módulo (resto) de a dividido por b.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Resto de la división a / b

    Raises:
        ValueError: Si b es cero
        TypeError: Si a o b no son números
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero")
    return a % b