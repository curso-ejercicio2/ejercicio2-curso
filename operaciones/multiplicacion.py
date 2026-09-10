# operaciones/multiplicacion.py
# Responsable: Jhosias Daza Albornoz
# Responsable: Juan Carlos Anagua Kahuana

def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de a * b

    Raises:
        TypeError: Si alguno de los argumentos no es numérico
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser numéricos")
    return a * b


def multiplicar_lista(valores):
    """
    Multiplica todos los elementos de una lista (producto acumulado).

    Args:
        valores (list): Lista de números

    Returns:
        float: Producto de todos los elementos

    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si algún elemento no es numérico
    """
    if not valores:
        raise ValueError("La lista no puede estar vacía")
    resultado = 1
    for valor in valores:
        if not isinstance(valor, (int, float)):
            raise TypeError(f"El valor '{valor}' no es numérico")
        resultado *= valor
    return resultado