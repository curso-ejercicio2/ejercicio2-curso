# operaciones/suma_cuadrados.py - Suma de Cuadrados
# Responsable: Daniel Sanchez (eq05)

from .validaciones import es_numero


def suma_cuadrados(a: float, b: float) -> float:
    """Calcula la suma de los cuadrados de dos números."""
    es_numero(a, "El primer número")
    es_numero(b, "El segundo número")
    return (a ** 2) + (b ** 2)

