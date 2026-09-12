# operaciones/division.py - División de Decimales (Refactorizado)
# Responsable: Heidy Jhael Flores Tiñini (eq05)

def dividir_decimales(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        raise ValueError("Error: No es posible dividir entre cero.")
    return dividendo / divisor


def solicitar_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número decimal válido.")


def main():
    print("=== Calculadora de División de Decimales ===")
    
    dividendo = solicitar_numero("Ingresa el dividendo (número a dividir): ")
    divisor = solicitar_numero("Ingresa el divisor (número divisor): ")

    try:
        resultado = dividir_decimales(dividendo, divisor)
        print(f"\nResultado: {dividendo} / {divisor} = {resultado:.4f}")
    except ValueError as e:
        print(f"\n[Error de cálculo]: {e}")


if __name__ == "__main__":
    main()