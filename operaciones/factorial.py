# operaciones/factorial.py - Cálculo de factorial
# Responsables: Vanessa Flores (eq01), Luis Maturano (eq01), Tais Gemio (eq07)

from math import factorial
from .validaciones import es_entero, no_negativo


def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    """

    # Tais Gemio (eq07): Se mantienen las validaciones
    # para asegurar que el valor sea entero y no negativo
    no_negativo(n, "El número")
    es_entero(n, "El número")

    # Tais Gemio (eq07): Se refactorizó el cálculo manual
    # utilizando la función factorial de la biblioteca estándar
    n = int(n)
    return factorial(n)
