# Responsables: Guimela, Luis Santiago (eq03)

def calcular_potencia(a, b):
    """Calcula a elevado a b."""
    return a ** b

def potencia_vectorizada(bases, exponentes):
    """
    Calcula la potencia elemento por elemento entre dos listas.
    
    Args:
        bases (list): Lista de números base.
        exponentes (list): Lista de exponentes.
    
    Returns:
        list: Lista con los resultados de elevar cada base a su exponente.
    """
    if len(bases) != len(exponentes):
        raise ValueError("Las listas deben tener el mismo tamaño")
    return [b ** e for b, e in zip(bases, exponentes)]