# operaciones/division.py
# Responsable: Alexander J. Padilla (eq02)
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

def dividir_positivos(a, b):
    """
    Divide dos números positivos.
    """
    if a < 0 or b <= 0:
        raise ValueError("Los números deben ser positivos")

    return a / b