from fractions import Fraction

from .validaciones import no_cero


def restar_fracciones(num1: int, den1: int, num2: int, den2: int) -> Fraction:
    no_cero(den1, "El denominador de la primera fracción")
    no_cero(den2, "El denominador de la segunda fracción")

    fraccion1 = Fraction(num1, den1)
    fraccion2 = Fraction(num2, den2)
    
    return fraccion1 - fraccion2

if __name__ == "__main__":
    # Ejemplo 1: Resta entre negativos -> (-1/2) - (-3/4) = 1/4
    resultado = restar_fracciones(-1, 2, -3, 4)
    print(f"Resultado 1: {resultado}")  # Imprime: 1/4

    res = restar_fracciones(1, -3, 2, 5)
    print(f"Resultado en numérico float: {float(res)}") # Se puede convertir según se necesite
    