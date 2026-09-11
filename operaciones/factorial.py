# operaciones/factorial.py - Cálculo de factorial
# Responsables: Vanessa Flores (eq01), Luis Maturano (eq01)

from .validaciones import es_entero, no_negativo


def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo n.
    Lanza ValueError si n es negativo o no es entero.
    """
    no_negativo(n, "El número")
    es_entero(n, "El número")

    n = int(n)
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
