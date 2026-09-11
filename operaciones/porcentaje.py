# operaciones/porcentaje.py
# Responsables: Alex Cristian Saavedra Veliz (eq07), Carlos Gabriel Calderon Javier (eq05)

def porcentaje(total: float, porcentaje: float) -> float:
    """
    Calcula el porcentaje de una cantidad base con validación de tipos de datos.

    Args:
        total (float): Monto total.
        porcentaje (float): Porcentaje del total que se quiere calcular.

    Returns:
        float: El resultado del porcentaje calculado.

    Raises:
        TypeError: Si los valores ingresados no son numéricos.
    """
    if not isinstance(total, (int, float)) or not isinstance(porcentaje, (int, float)):
        raise TypeError("Los valores deben ser numéricos")

    return (total * porcentaje) / 100.0
