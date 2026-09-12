PI = 3.141592653589793

def reducir_angulo(x):
    dos_pi = 2 * PI
    x = x % dos_pi
    if x > PI:
        x -= dos_pi
    return x


def funcion_seno(x, terminos=15):
    x = reducir_angulo(x)
    resultado = 0
    for n in range(terminos):
        signo = (-1) ** n
        exponente = 2 * n + 1
        factorial = 1
        for i in range(1, exponente + 1):
            factorial *= i
        resultado += signo * (x ** exponente) / factorial
    return resultado


if __name__ == "__main__":
    valor = float(input("Ingresa un ángulo en radianes: "))
    resultado = funcion_seno(valor)
    print(f"El seno de {valor} es: {resultado}")