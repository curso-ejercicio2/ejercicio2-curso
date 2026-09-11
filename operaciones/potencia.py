# operaciones/potencia.py
# Responsable: Gabriel Torrico Nina (eq02)
# Responsables: Guimela, Luis Santiago (eq03)

from .validaciones import es_numero, misma_longitud


def potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de una base elevada a un exponente.

    Args:
        base (float): Numero base
        exponente (float): Exponente al que se eleva la base

    Returns:
        float: Resultado de base ** exponente
    """
    es_numero(base, "La base")
    es_numero(exponente, "El exponente")

    # Caso principal: eleva base a exponente.
    if base == 0 and exponente == 0:
        raise ValueError("Indefinicion matematica: 0 elevado a la 0 no esta determinado")

    # Subcaso: maneja explicitamente exponentes negativos.
    if base == 0 and exponente < 0:
        raise ZeroDivisionError("No se puede elevar 0 a un exponente negativo")
    return base ** exponente


def calcular_potencia(a, b):
    """Calcula a elevado a b."""
    es_numero(a, "La base")
    es_numero(b, "El exponente")
    return a ** b


def potencia_vectorizada(bases, exponentes):
    """
    Calcula la potencia elemento por elemento entre dos listas.

    Args:
        bases (list): Lista de numeros base.
        exponentes (list): Lista de exponentes.

    Returns:
        list: Lista con los resultados de elevar cada base a su exponente.
    """
    misma_longitud(bases, exponentes, "Las listas")
    for base in bases:
        es_numero(base, f"La base '{base}'")
    for exponente in exponentes:
        es_numero(exponente, f"El exponente '{exponente}'")
    return [b ** e for b, e in zip(bases, exponentes)]
