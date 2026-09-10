#Alejandro Soliz Gonzales(eq05)
def multiplicar2(a, b):
    resultado = 0
    for _ in range(abs(int(b))):
        resultado += a
    return resultado if b >= 0 else -resultado