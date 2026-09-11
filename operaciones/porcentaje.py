# operaciones/porcentaje.py
#responsable : Carlos Gabriel Calderon Javier (eq05)

def calcular_porcentaje(total, porcentaje):
    """Calcula el porcentaje de una cantidad dada."""
    if not isinstance(total, (int, float)) or not isinstance(porcentaje, (int, float)):
        raise TypeError("Los valores deben ser numéricos")
    return (total * porcentaje) / 100