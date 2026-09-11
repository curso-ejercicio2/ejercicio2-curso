# operaciones/suma.py
# Responsable: Ronald Escobar Vargas (eq02) y Diego (eq07)


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


def suma_lista(lista):
    """
    Suma todos los elementos de una lista de números.

    Args:
        lista (list): Lista de números

    Returns:
        float: Suma total de los elementos
    """
    return sum(lista)

def suma_pares(lista):
    """
    Filtra y suma únicamente los números pares de una lista.

    Args:
        lista (list): Lista de números enteros o flotantes.

    Returns:
        float/int: Suma total de los números pares.
    """
    return sum(x for x in lista if x % 2 == 0)