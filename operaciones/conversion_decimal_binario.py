# operaciones/conversion_decimal_binario.py - Conversión de decimal a binario

def decimal_a_binario(numero):
    if numero == 0:
        return "0"

    n = numero
    digitos = []
    while n > 0:
        digitos.append(str(n % 2))
        n //= 2

    return "".join(reversed(digitos))