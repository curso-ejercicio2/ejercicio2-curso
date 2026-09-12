# operaciones/combinacion.py - Cálculo de combinacion
# Responsable: Gabriel Bazualdo (eq05)

from .factorial import calcular_factorial
from .permutacion import calcular_permutaciones
from .validaciones import no_negativo, es_entero

def calcular_combinaciones(n, r):
    """
    Calcula el número de combinaciones de n elementos tomados de r en r (nCr).
    Fórmula: n! / (r! * (n - r)!)
    """
    no_negativo(n, "n")
    no_negativo(r, "r")
    es_entero(n, "n")
    es_entero(r, "r")
    if r > n:
        raise ValueError("r no puede ser mayor que n")

    n = int(n)
    r = int(r)

    if r == 0 or r == n:
        return 1

    return calcular_permutaciones(n, r) // calcular_factorial(r)
