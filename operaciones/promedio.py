#Responsable: Ticona Chura Stefani Mishel (eq04)
def promedio(numeros):
    suma = sum(numeros)          
    cantidad = len(numeros)
    
    cociente = 0
    while suma >= cantidad:
        suma -= cantidad
        cociente += 1
    
    return cociente


# responsable: Nicole Flores Escalera (eq07)
# mejora: Se agrega la función 'promedio_exacto' para calcular la media aritmética
# con decimales y validación de listas vacías, sin modificar la función original.

from typing import List, Union


def promedio_exacto(valores: List[Union[int, float]]) -> float:
    """
    Calcula el promedio exacto (media aritmética) de una lista de números.
    """
    if not valores:
        raise ValueError("La lista de valores no puede estar vacía.")

    return sum(valores) / len(valores)
