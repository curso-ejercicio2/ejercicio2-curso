# Autor: Nicole Flores escalera - eq05

def promedio(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)
