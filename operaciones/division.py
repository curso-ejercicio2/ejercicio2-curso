# operaciones/division.py
# Mejora realizada por: Diego Rafael Mancilla Flores (eq05)
# Código original: Alexander J. Padilla (eq02)

from .validaciones import es_numero, es_positivo, lista_no_vacia, no_cero, no_negativo


def dividir(a: float, b: float) -> float:
    """
    Divide dos números.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: Resultado de a / b.

    Raises:
        TypeError: Si alguno de los valores no es numérico.
        ValueError: Si b es cero.
    """
    es_numero(a, "El dividendo")
    es_numero(b, "El divisor")
    no_cero(b, "El divisor")
    return a / b

# Responsable: Santiago Huapalla (eq03)
def dividir_lista(lista, divisor):
    """Divide cada elemento de una lista entre un número divisor.

    Args:
        lista (list): Lista de números a dividir.
        divisor (int/float): Número por el cual se divide cada elemento.

    Returns:
        list of float: Nueva lista con los resultados de cada división.
    """
    lista_no_vacia(lista)
    es_numero(divisor, "El divisor")
    no_cero(divisor, "El divisor")
    for elemento in lista:
        es_numero(elemento, f"El elemento '{elemento}'")
    return [elemento / divisor for elemento in lista]



def dividir_positivos(a: float, b: float) -> float:
    """
    Divide dos números positivos.

    Args:
        a (float): Dividendo positivo.
        b (float): Divisor positivo.

    Returns:
        float: Resultado de la división.

    Raises:
        ValueError: Si a no es positivo o b no es mayor que cero.
    """
    es_numero(a, "El dividendo")
    es_numero(b, "El divisor")
    no_negativo(a, "El dividendo")
    es_positivo(b, "El divisor")

    return a / b

# operaciones.divisionBusquedaBinaria.py
# Responsable: Natalie Saravia Camacho (eq07)

def divisionBusquedaBinaria(dividendo: float, divisor: float):
    """
    Divide 'dividendo' entre 'divisor' usando búsqueda binaria
    sobre el posible cociente.

    Retorna una tupla (cociente, residuo).
    """
    if divisor == 0:
        raise ValueError("No se puede dividir entre cero")

    # Determinar el signo del resultado
    signo = 1
    if (dividendo < 0) != (divisor < 0):
        signo = -1

    dividendo = abs(dividendo)
    divisor = abs(divisor)

    izquierda, derecha = 0, int(dividendo)
    cociente = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if divisor * medio <= dividendo:
            cociente = medio
            izquierda = medio + 1
        else:
            derecha = medio - 1

    residuo = dividendo - (divisor * cociente)

    return cociente * signo, residuo