# operaciones/permutacion.py - Cálculo de permutacion
# Responsables: Vanessa Flores (eq01), Luis Maturano (eq01)
from .factorial import calcular_factorial
def calcular_permutaciones(n, r):
    """
    Calcula el número de permutaciones de n elementos tomados de r en r (nPr).
    Fórmula: n! / (n - r)!
    """
    if r < 0 or n < 0:
        raise ValueError("n y r deben ser no negativos")
    if r > n:
        raise ValueError("r no puede ser mayor que n")

    return calcular_factorial(n) // calcular_factorial(n - r)