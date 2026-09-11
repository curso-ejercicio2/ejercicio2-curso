# operaciones/suma.py
# Responsable: Ronald Escobar Vargas (eq02), Josue Lara Paqui (eq06) , Diego Alejandro Montaño quispe  (eq07)


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
def sumar_multiples(*args):
    """
    Suma una cantidad arbitraria de números.

    Args:
        *args: Múltiples números a sumar separados por comas.

    Returns:
        float: Suma total de todos los argumentos proporcionados.
    """
    return sum(args)
