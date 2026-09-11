# operaciones/conversion_decimal_binario.py - Conversión de decimal a binario

def decimal_a_binario(numero):
    if isinstance(numero, bool) or not isinstance(numero, (int, float)):
        raise TypeError("El valor debe ser un número entero o decimal válido")

    if numero != int(numero):
        raise ValueError("Solo se pueden convertir números enteros a binario")

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

