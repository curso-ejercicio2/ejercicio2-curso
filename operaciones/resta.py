# operaciones/resta.py

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
    # Responsable: Beckerman Aguero Mallqui (eq01)
def restar_varios(valor_inicial, *valores_a_restar):
    resultado = valor_inicial
    for valor in valores_a_restar:
        resultado -= valor
    return resultado

# Responsable: Torrico Copali Jorge David (eq04)

def restar_varios_mejorado(valor_inicial, *valores_a_restar):
    """
    Resta múltiples valores a un valor inicial de forma acumulativa.
    ...
    """
    if not isinstance(valor_inicial, (int, float)):
        raise TypeError(
            f"El valor inicial debe ser un número, se recibió: {type(valor_inicial).__name__}"
        )
    resultado = valor_inicial
    for i, valor in enumerate(valores_a_restar, start=1):
        if not isinstance(valor, (int, float)):
            raise TypeError(
                f"El valor #{i} a restar debe ser un número, se recibió: {type(valor).__name__}"
            )
        resultado -= valor
    return resultado
