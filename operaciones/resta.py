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

# Responsable: Miguel (eq07)

def restar_lista(valores):
    """
    Resta una lista de números de forma acumulativa.

    Args:
        valores (list): Lista de números.

    Returns:
        float: Resultado de la resta acumulada.
    """

    if not valores:
        raise ValueError("La lista no puede estar vacía")

    for valor in valores:
        es_numero(valor, f"El valor '{valor}'")

    resultado = valores[0]

    for valor in valores[1:]:
        resultado -= valor

    return resultado
