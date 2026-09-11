# operaciones/division.py
# Mejora realizada por: Diego Rafael Mancilla Flores (eq05)
# Código original: Alexander J. Padilla (eq02)

def dividir(a: float, b: float) -> float:
    """
    Divide dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: Resultado de a / b.

    Raises:
        TypeError: Si alguno de los valores no es numérico.
        ValueError: Si b es cero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los valores deben ser numéricos")

    if b == 0:
        raise ValueError("No se puede dividir por cero")

    return a / b


def dividir_positivos(a: float, b: float) -> float:
    """
    Divide dos números positivos.

    Args:
        a (float): Dividendo positivo.
        b (float): Divisor positivo.

    Returns:
        float: Resultado de la división.

    Raises:
        ValueError: Si a no es positivo o b no es mayor que cero.
    """
    if a < 0 or b <= 0:
        raise ValueError("Los números deben ser positivos")

    return a / b
