# operaciones/permutacion.py - Cálculo de permutacion
# Responsables: Vanessa Flores (eq01), Luis Maturano (eq01)
from .factorial import calcular_factorial
from .validaciones import es_entero, no_negativo


def calcular_permutaciones(n, r):
    """
    Calcula el número de permutaciones de n elementos tomados de r en r (nPr).
    Fórmula: n! / (n - r)!
    """
    no_negativo(n, "n")
    no_negativo(r, "r")
    es_entero(n, "n")
    es_entero(r, "r")
    if r > n:
        raise ValueError("r no puede ser mayor que n")

    return calcular_factorial(n) // calcular_factorial(n - r)