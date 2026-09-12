# operaciones/raiz.py
# Responsable: (eq01)
# Responsable: Santiago Piscoya (eq02)
# Responsable: Daniel Flores (eq08)

from .validaciones import es_numero, no_cero


def calcular(base, indice):
    """Calcula la raíz n-ésima de un número (base ** (1/indice))."""
    if indice == 0:
        return "Error: El índice de la raíz no puede ser cero"
    if base < 0 and indice % 2 == 0:
        return "Error: No existe raíz par de un número negativo en números reales"
    if base < 0:
        # Fix: evita que Python devuelva un número complejo con base negativa
        # e índice impar; ahora retorna el real negativo esperado.
        return -((-base) ** (1 / indice))
    return base ** (1 / indice)


def calcular_raiz(numero, indice=2):
    es_numero(numero, "El número")
    es_numero(indice, "El índice de la raíz")
    no_cero(indice, "El índice de la raíz")

    if numero < 0:
        if indice % 2 == 0:
            raise ValueError(
                "No existe raíz real de índice par para un número negativo."
            )
        return -((-numero) ** (1 / indice))

    return numero ** (1 / indice)


def raiz_cuadrada(numero):
    """Atajo legible para el caso más común: raíz cuadrada.
    Reutiliza calcular_raiz() para no duplicar lógica."""
    return calcular_raiz(numero, indice=2)