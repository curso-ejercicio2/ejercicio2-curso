import math

def calcular_hipotenusa(cateto_a: float, cateto_b: float) -> float:
    """Calcula la hipotenusa dados los catetos a y b."""
    if cateto_a <= 0 or cateto_b <= 0:
        raise ValueError("Los catetos deben ser mayores que cero.")
    return math.hypot(cateto_a, cateto_b)

def calcular_cateto(hipotenusa: float, cateto_conocido: float) -> float:
    """Calcula un cateto dada la hipotenusa y el otro cateto."""
    if hipotenusa <= 0 or cateto_conocido <= 0:
        raise ValueError("Las longitudes deben ser mayores que cero.")
    if hipotenusa <= cateto_conocido:
        raise ValueError("La hipotenusa debe ser estrictamente mayor que el cateto conocido.")
    return math.sqrt(hipotenusa**2 - cateto_conocido**2)