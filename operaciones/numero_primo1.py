def es_primo(n):
    """
    Verifica si un numero entero es primo.

    Parametros:
        n (int): numero entero a verificar

    Retorna:
        bool: True si n es primo, False si no lo es

    Lanza:
        ValueError: si n no es un entero
    """
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un numero entero")

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    numero = int(input("Ingrese un numero entero: "))
    if es_primo(numero):
        print(f"{numero} es un numero primo")
    else:
        print(f"{numero} no es un numero primo")
