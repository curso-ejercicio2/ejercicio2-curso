# operaciones/validaciones.py - Validaciones genéricas reutilizables
# Responsable: Ximena Condo Ramirez (eq01)


def es_numero(valor, nombre="El valor"):
    """
    Valida que un valor sea numérico (int o float, excluyendo bool).

    Args:
        valor: Valor a validar.
        nombre (str): Nombre descriptivo del valor para el mensaje de error.

    Returns:
        bool: True si el valor es numérico.

    Raises:
        TypeError: Si el valor no es int o float (o es bool).
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise TypeError(f"{nombre} debe ser un número")
    return True


def es_entero(valor, nombre="El valor"):
    """
    Valida que un valor sea un número entero.

    Args:
        valor: Valor a validar.
        nombre (str): Nombre descriptivo del valor para el mensaje de error.

    Returns:
        bool: True si el valor es un número entero.

    Raises:
        TypeError: Si el valor no es numérico.
        ValueError: Si el valor no es un número entero.
    """
    es_numero(valor, nombre)
    if valor != int(valor):
        raise ValueError(f"{nombre} debe ser un número entero")
    return True


def no_cero(valor, nombre="El divisor"):
    """
    Valida que un valor sea distinto de cero.

    Args:
        valor: Valor a validar.
        nombre (str): Nombre descriptivo del valor para el mensaje de error.

    Returns:
        bool: True si el valor no es cero.

    Raises:
        ValueError: Si el valor es cero.
    """
    if valor == 0:
        raise ValueError(f"{nombre} no puede ser cero")
    return True


def es_positivo(valor, nombre="El valor"):
    """
    Valida que un valor sea positivo (mayor que cero).

    Args:
        valor: Valor a validar.
        nombre (str): Nombre descriptivo del valor para el mensaje de error.

    Returns:
        bool: True si el valor es positivo.

    Raises:
        ValueError: Si el valor es cero o negativo.
    """
    if valor <= 0:
        raise ValueError(f"{nombre} debe ser positivo")
    return True


def no_negativo(valor, nombre="El valor"):
    """
    Valida que un valor sea no negativo (mayor o igual a cero).

    Args:
        valor: Valor a validar.
        nombre (str): Nombre descriptivo del valor para el mensaje de error.

    Returns:
        bool: True si el valor no es negativo.

    Raises:
        ValueError: Si el valor es negativo.
    """
    if valor < 0:
        raise ValueError(f"{nombre} no puede ser negativo")
    return True


def lista_no_vacia(lista, nombre="La lista"):
    """
    Valida que una lista no esté vacía.

    Args:
        lista (list): Lista a validar.
        nombre (str): Nombre descriptivo de la lista para el mensaje de error.

    Returns:
        bool: True si la lista tiene al menos un elemento.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not lista:
        raise ValueError(f"{nombre} no puede estar vacía")
    return True


def misma_longitud(lista_a, lista_b, nombre="Las listas"):
    """
    Valida que dos listas tengan la misma cantidad de elementos.

    Args:
        lista_a (list): Primera lista.
        lista_b (list): Segunda lista.
        nombre (str): Nombre descriptivo para el mensaje de error.

    Returns:
        bool: True si ambas listas tienen la misma longitud.

    Raises:
        ValueError: Si las listas tienen longitudes distintas.
    """
    if len(lista_a) != len(lista_b):
        raise ValueError(f"{nombre} deben tener la misma longitud")
    return True