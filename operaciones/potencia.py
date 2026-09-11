# operaciones/potencia.py
# REspponsable: Gabriel Torrico (eq02)
def potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de una base elevada a un exponente.
    
    Args:
        base (float): Número base
        exponente (float): Exponente al que se eleva la base
    
    Returns:
        float: Resultado de base ** exponente
    """
    """Caso principal: eleva base a exponente."""
    if base == 0 and exponente == 0:
        raise ValueError("Indefinicion matematica: 0 elevado a la 0 no esta determinado")
    
    """Subcaso: maneja explicitamente exponentes negativos."""

    if base == 0 and exponente < 0:
        raise ZeroDivisionError("No se puede elevar 0 a un exponente negativo")
    return base ** exponente
