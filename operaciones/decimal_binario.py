# operaciones/conversion_decimal_binario.py - Conversión de decimal a binario
# Responsable: Rodrigo Mamani Rocha
from .validaciones import es_entero


def decimal_a_binario(numero):
    es_entero(numero, "El número")
    n = int(numero)

    if n == 0:
        return "0"

    es_negativo = n < 0
    n = abs(n)

    digitos = []
    while n > 0:
        digitos.append(str(n % 2))
        n //= 2

    binario = "".join(reversed(digitos))
    return f"-{binario}" if es_negativo else binario

