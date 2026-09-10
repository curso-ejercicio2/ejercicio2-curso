# operaciones/suma.py

def sumar(a, b):
    """
    Suma dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
    
    Returns:
        float: Resultado de a + b
    """
    return a + b

#responsable: jose rojas (eq04)
def sumar_varios(*numeros):
    return sum(numeros)