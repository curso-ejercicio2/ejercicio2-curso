# operaciones/factorial.py - Cálculo de factorial
# Responsables: Vanessa Flores (eq01), Luis Maturano (eq01)
def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo n.
    Lanza ValueError si n es negativo o no es entero.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n != int(n):
        raise ValueError("El factorial solo está definido para números enteros")

    n = int(n)
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
