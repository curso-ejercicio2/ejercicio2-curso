# operaciones/porcentaje.py
# Responsables: Alex Cristian Saavedra Veliz (eq07), Carlos Gabriel Calderon Javier (eq05)

from .validaciones import es_numero


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
    es_numero(total, "El total")
    es_numero(porcentaje, "El porcentaje")

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



# Responsable: Franz Orellana (eq04)
# mejora: Se agrega la función `variacion_porcentual`, que calcula el cambio
# porcentual entre un valor inicial y uno final (ej. cuánto subió o bajó un
# precio). Reutiliza `es_numero` para mantener la misma validación de tipos
# que usa el resto del archivo.
def variacion_porcentual(valor_inicial: float, valor_final: float) -> float:
    """
    Calcula el porcentaje de variación entre un valor inicial y uno final.

    Args:
        valor_inicial (float): Valor de referencia (antes del cambio).
        valor_final (float): Valor nuevo (después del cambio).

    Returns:
        float: Porcentaje de variación. Positivo si aumentó, negativo si disminuyó.

    Raises:
        TypeError: Si los valores ingresados no son numéricos.
        ValueError: Si el valor inicial es 0 (no se puede calcular variación desde 0).
    """
    es_numero(valor_inicial, "El valor inicial")
    es_numero(valor_final, "El valor final")

    if valor_inicial == 0:
        raise ValueError("No se puede calcular la variación porcentual desde un valor inicial de 0")

    diferencia = valor_final - valor_inicial
    return (diferencia / valor_inicial) * 100