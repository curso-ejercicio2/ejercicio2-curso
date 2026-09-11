# operaciones/logaritmo.py
#Responsable : Cristhian Chamaca Jimenez (eq06)
import math

def calcular_logaritmo(numero, base=None):
    if numero <= 0:
        raise ValueError("El número debe ser mayor a 0.")
    if base is not None and (base <= 0 or base == 1):
        raise ValueError("La base debe ser mayor a 0 y diferente de 1.")
    
    if base is None:
        return math.log(numero)
    return math.log(numero, base)