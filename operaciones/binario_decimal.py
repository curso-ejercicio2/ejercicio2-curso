# operaciones/binario_decimal.py - Cálculo de binario a decimal
# Responsable: Jose Armando Quisbert Medrano (eq07)
def binario_a_decimal(binario):
    decimal = 0
    potencia = 0

    for digito in reversed(binario):
        if digito == "1":
            decimal += 2 ** potencia
        elif digito != "0":
            raise ValueError("El número ingresado no es binario.")

        potencia += 1

    return decimal