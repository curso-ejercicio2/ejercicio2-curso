# operaciones/raiz.py
# Responsable: (eq01)
# Responsable: Santiago Piscoya (eq02)

def calcular(base, indice):
    """Calcula la raíz n-ésima de un número (base ** (1/indice))."""
    if indice == 0:
        return "Error: El índice de la raíz no puede ser cero"
    if base < 0 and indice % 2 == 0:
        return "Error: No existe raíz par de un número negativo en números reales"
    return base ** (1 / indice)


def calcular_raiz(numero, indice=2):
    if indice == 0:
        raise ValueError("El índice de la raíz no puede ser 0.")

    if numero < 0:
        if indice % 2 == 0:
            raise ValueError(
                "No existe raíz real de índice par para un número negativo."
            )
        return -((-numero) ** (1 / indice))

    return numero ** (1 / indice)