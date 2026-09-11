# operaciones/combinacion.py - Cálculo de combinacion
# Responsable: Gabriel Bazualdo (eq05)

from .factorial import calcular_factorial
from .permutacion import calcular_permutaciones

def calcular_combinaciones(n, r):
    """
    Calcula el número de combinaciones de n elementos tomados de r en r (nCr).
    Fórmula: n! / (r! * (n - r)!)
    """
    if r < 0 or n < 0:
        raise ValueError("n y r deben ser no negativos")
    if r > n:
        raise ValueError("r no puede ser mayor que n")
    if n != int(n) or r != int(r):
        raise ValueError("n y r deben ser enteros")

    n = int(n)
    r = int(r)

    if r == 0 or r == n:
        return 1

    return calcular_permutaciones(n, r) // calcular_factorial(r)
