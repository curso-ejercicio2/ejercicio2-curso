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


# responsable: Santos Marca Maria Clara (eq04)
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


if __name__ == "__main__":
    print("Prueba de la función original:")
    print("porcentaje(1500, 18) =", porcentaje(1500, 18))

    print("\nPrueba de la mejora:")
    print("porcentaje_redondeado(1234.5, 7.3) =", porcentaje_redondeado(1234.5, 7.3))