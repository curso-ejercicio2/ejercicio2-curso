# operaciones/es_perfecto.py
# Responsable: Ordoñez Luna Jhoan Jhostyn(eq08)
from .validaciones import es_numero

def es_perfecto(n):
    if not es_numero(n):
        raise TypeError("El argumento debe ser un número")

    if n <= 1:
        return False

    suma = 0

    for i in range(1, n):
        if n % i == 0:
            suma += i

    return suma == n