# operaciones/raiz.py

def calcular(base, indice):
    """Calcula la raíz n‑ésima de un número (base ** (1/indice))."""
    if indice == 0:
        return "Error: El índice de la raíz no puede ser cero"
    if base < 0 and indice % 2 == 0:
        return "Error: No existe raíz par de un número negativo en números reales"
    return base ** (1 / indice)
