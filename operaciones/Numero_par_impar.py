# operaciones/par_impar.py
# Responsable: Anahy Cayo (eq06)

from .validaciones import es_numero


def es_par(numero):
    es_numero(numero, "El número")
    return numero % 2 == 0


def es_impar(numero):
    es_numero(numero, "El número")
    return numero % 2 != 0


def verificar_numero(numero):
    if es_par(numero):
        return "El número es par"
    return "El número es impar"


def main():
    numero = int(input("Ingrese un número: "))
    print(verificar_numero(numero))


if __name__ == "__main__":
    main()
