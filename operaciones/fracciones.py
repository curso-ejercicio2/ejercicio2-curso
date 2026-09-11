from fractions import Fraction

def restar_fracciones(num1: int, den1: int, num2: int, den2: int) -> Fraction:
    if den1 == 0 or den2 == 0:
        raise ValueError("El denominador no puede ser cero.")
    
    fraccion1 = Fraction(num1, den1)
    fraccion2 = Fraction(num2, den2)
    
    return fraccion1 - fraccion2

if __name__ == "__main__":
    # Ejemplo 1: Resta entre negativos -> (-1/2) - (-3/4) = 1/4
    resultado = restar_fracciones(-1, 2, -3, 4)
    print(f"Resultado 1: {resultado}")  # Imprime: 1/4

    res = restar_fracciones(1, -3, 2, 5)
    print(f"Resultado en numérico float: {float(res)}") # Se puede convertir según se necesite
    