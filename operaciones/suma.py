# operaciones/suma.py
# Responsable: Ronald Escobar Vargas (eq02)

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