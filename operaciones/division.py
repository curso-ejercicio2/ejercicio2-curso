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

# Responsable: Santiago Huapalla (eq03)
def dividir_lista(lista, divisor):
    """Divide cada elemento de una lista entre un número divisor.

    Args:
        lista (list): Lista de números a dividir.
        divisor (int/float): Número por el cual se divide cada elemento.

    Returns:
        list of float: Nueva lista con los resultados de cada división.
    """
    return [elemento / divisor for elemento in lista]
