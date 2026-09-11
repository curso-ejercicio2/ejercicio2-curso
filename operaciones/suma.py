# operaciones/suma.py
# Responsable: Ronald Escobar Vargas (eq02), Josue Lara Paqui (eq06)

from .validaciones import es_numero


def sumar(a, b):
    """
    Suma dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de a + b
    """
    es_numero(a, "El primer número")
    es_numero(b, "El segundo número")
    return a + b


def suma_lista(lista):
    """
    Suma todos los elementos de una lista de números.

    Args:
        lista (list): Lista de números

    Returns:
        float: Suma total de los elementos
    """
    for elemento in lista:
        es_numero(elemento, f"El elemento '{elemento}'")
    return sum(lista)


def sumar_multiples(*args):
    """
    Suma una cantidad arbitraria de números.

    Args:
        *args: Múltiples números a sumar separados por comas.

    Returns:
        float: Suma total de todos los argumentos proporcionados.
    """
    for valor in args:
        es_numero(valor, f"El valor '{valor}'")
    return sum(args)