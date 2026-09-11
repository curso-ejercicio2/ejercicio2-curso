# operaciones/resta.py

from .validaciones import es_numero


def restar(a, b):
    """
    Resta dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
    
    Returns:
        float: Resultado de a - b
    """
    es_numero(a, "El primer número")
    es_numero(b, "El segundo número")
    return a - b
    # Responsable: Beckerman Aguero Mallqui (eq01)
def restar_varios(valor_inicial, *valores_a_restar):
    es_numero(valor_inicial, "El valor inicial")
    for valor in valores_a_restar:
        es_numero(valor, f"El valor '{valor}'")
    resultado = valor_inicial
    for valor in valores_a_restar:
        resultado -= valor
    return resultado