from fractions import Fraction

from .validaciones import no_cero


# Responsable: Mayra Arias Grageda (eq02)
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

# responsable: Oliver Cristian Quispe Rocha (eq04)

def validar_fraccion(num: int, den: int) -> Fraction:
    if den == 0:
        raise ValueError("El denominador no puede ser cero.")
    return Fraction(num, den)

def mostrar_fraccion(num: int, den: int) -> str:
    fraccion = validar_fraccion(num, den)
    return str(fraccion)

def restar_y_mostrar(num1: int, den1: int, num2: int, den2: int) -> None:
    resultado = restar_fracciones(num1, den1, num2, den2)
    print(f"{num1}/{den1} - {num2}/{den2} = {resultado}")
    print(f"Resultado decimal: {float(resultado)}")

#responsable: Rogelio Cortez (eq08)
def multiplicar_fracciones(num1: int , den1: int, num2: int, den2: int) -> Fraction:
    if den1 == 0 or den2 == 0:
        raise ValueError("El denominador no puede ser cero.")
    
    fraccion1 = Fraction(num1, den1)
    fraccion2 = Fraction(num2, den2)
    
    return fraccion1 * fraccion2

# Pruebas adicionales
if __name__ == "__main__":
    print("\nPruebas adicionales:")

    restar_y_mostrar(3, 4, 1, 2)
    restar_y_mostrar(-5, 6, -1, 3)
    restar_y_mostrar(7, -8, 2, 5)

    # Comprobación de denominador cero
    try:
        restar_y_mostrar(1, 0, 2, 3)
    except ValueError as error:
        print(f"Error: {error}")


