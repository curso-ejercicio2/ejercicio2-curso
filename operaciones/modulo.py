# operaciones/modulo.py
# Responsable: Francisco Lazarte Salazar (eq02)
# Responsable: Gael Villarroel (eq02)

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


def modulo_lista(lista, divisor):
    """
    Calcula el módulo de cada elemento de una lista respecto a un divisor fijo.
    
    Args:
        lista (list): Lista de números (dividendos)
        divisor (float): Divisor
    
    Returns:
        list: Lista con los restos de cada división
    """
    if divisor == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero")
    return [num % divisor for num in lista]


def modulo_lista_negativos(lista, divisor):
    """
    Calcula el módulo de una lista incluyendo valores negativos.

    Args:
        lista (list): Lista de números.
        divisor (float): Número divisor.

    Returns:
        list: Lista con los módulos calculados.
    """
    if divisor == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero")
    return [numero % divisor for numero in lista]