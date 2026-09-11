# operaciones/porcentaje.py

# Responsable: Alex Cristian Saavedra Veliz (eq07)

def porcentaje(total: float, porcentaje: float) -> float:
    """
    Calcula el porcentaje de una cantidad base.

    Args:
        total (float): Monto total
        porcentaje (float): Porcentaje del total que se quiere calcular

    Ejemplo: El 15% de 200
    
    porcentaje(200, 15) -> 30.0
    """
    return (total * porcentaje) / 100.0
