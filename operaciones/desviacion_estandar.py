#Autor: Yadira Peredo Equipo 9

import math

def calcular_desviacion_estandar(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    
    media = sum(lista) / len(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    return math.sqrt(varianza)