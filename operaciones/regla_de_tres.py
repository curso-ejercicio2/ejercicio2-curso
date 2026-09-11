
# operaciones/regla_de_tres.py
# responsable: Victor David Flores Colque

def aplicar_regla_de_tres(a, b, c):
    """
    Calcula una regla de tres simple directa.
    Si a corresponde a b, calcula cuánto corresponde a c.
    """
    if a == 0:
        raise ValueError("El primer valor no puede ser cero")

    return (b * c) / a