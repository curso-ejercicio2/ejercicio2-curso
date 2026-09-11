from fractions import Fraction

def restar_fracciones(num1: int, den1: int, num2: int, den2: int) -> Fraction:
    if den1 == 0 or den2 == 0:
        raise ValueError("El denominador no puede ser cero.")
    
    fraccion1 = Fraction(num1, den1)
    fraccion2 = Fraction(num2, den2)
    
    return fraccion1 - fraccion2

# Responsable: Alba Arrosquipa (eq08)
def sumar_fracciones(num1: int, den1: int, num2: int, den2: int) -> Fraction:
    if den1 == 0 or den2 == 0:
        raise ValueError("El denominador no puede ser cero.")
    
    fraccion1 = Fraction(num1, den1)
    fraccion2 = Fraction(num2, den2)
    
    return fraccion1 + fraccion2

if __name__ == "__main__":
    # Ejemplo 1: Resta entre negativos -> (-1/2) - (-3/4) = 1/4
    resultado = restar_fracciones(-1, 2, -3, 4)
    print(f"Resultado 1: {resultado}")  # Imprime: 1/4

    # Ejemplo 2: Suma de fracciones positivas -> 1/2 + 3/4 = 5/4
    resultado_suma = sumar_fracciones(1, 2, 3, 4)
    print(f"Resultado 2: {resultado_suma}")  # Imprime: 5/4

    res = restar_fracciones(1, -3, 2, 5)
    print(f"Resultado en numérico float: {float(res)}") # Se puede convertir según se necesite
    