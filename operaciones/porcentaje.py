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


# responsable: Santos Marca Maria Clara
# mejora: Se agrega la función `porcentaje_redondeado`, que reutiliza la lógica de
# `porcentaje` y devuelve el resultado redondeado a 2 decimales (útil para montos
# de dinero). No modifica ni reemplaza a la función original.
# Nota: el segundo parámetro se llama `pct` para evitar conflicto con el nombre
# de la función `porcentaje`.

def porcentaje_redondeado(total: float, pct: float) -> float:
    """
    Calcula el porcentaje de una cantidad y redondea el resultado a 2 decimales.

    Args:
        total (float): Monto total.
        pct (float): Porcentaje del total que se quiere calcular.

    Returns:
        float: El resultado del porcentaje redondeado a 2 decimales.
    """
    return round(porcentaje(total, pct), 2)
