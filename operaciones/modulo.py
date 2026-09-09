# operaciones/modulo.py

def calcular_modulo(a, b):
    """
    Calcula el módulo (resto) de a dividido por b.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
    
    Returns:
        float: Resto de la división a / b
    
    Raises:
        ValueError: Si b es cero
    """
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero")
    return a % b