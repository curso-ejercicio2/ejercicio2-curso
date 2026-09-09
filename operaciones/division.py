# operaciones/division.py

def dividir(a, b):
    """
    Divide dos números.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
    
    Returns:
        float: Resultado de a / b
    
    Raises:
        ValueError: Si b es cero
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b