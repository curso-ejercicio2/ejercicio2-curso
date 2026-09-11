# operaciones/resta.py - Resta de varios números
# Responsable: Beckerman Aguero Mallqui (eq01)


def restar(a, b):
    """
    Resta dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
    
    Returns:
        float: Resultado de a - b
    """
    return a - b

def restar_varios(valor_inicial, *valores_a_restar):
    resultado = valor_inicial
    for valor in valores_a_restar:
        resultado -= valor
    return resultado