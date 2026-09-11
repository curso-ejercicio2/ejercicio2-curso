# operaciones/modulo.py
# Responsable: Francisco Lazarte Salazar (eq02)
# Responsable: Gael Villarroel (eq02)

from .validaciones import es_numero, lista_no_vacia, no_cero


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
    es_numero(a, "El dividendo")
    es_numero(b, "El divisor")
    no_cero(b, "El divisor")
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
    lista_no_vacia(lista)
    es_numero(divisor, "El divisor")
    no_cero(divisor, "El divisor")
    for num in lista:
        es_numero(num, f"El elemento '{num}'")
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
    lista_no_vacia(lista)
    es_numero(divisor, "El divisor")
    no_cero(divisor, "El divisor")
    for numero in lista:
        es_numero(numero, f"El elemento '{numero}'")
    return [numero % divisor for numero in lista]