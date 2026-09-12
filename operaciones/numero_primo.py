def es_primo(n):
    """
    Retorna True si n es un número primo, False en caso contrario.
    """
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero.")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True