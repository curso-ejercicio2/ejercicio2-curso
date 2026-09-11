def calcular_moda(datos):
    # Validación: lista vacía
    if not datos:
        return None, "No se ingresaron datos."

    # Contar frecuencia de cada valor
    frecuencias = {}
    for valor in datos:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1

    # Encontrar la frecuencia máxima
    max_frecuencia = max(frecuencias.values())

    # Validación: si todos los valores tienen la misma frecuencia, no hay moda
    if max_frecuencia == 1 or len(set(frecuencias.values())) == 1:
        return None, "Amodal (no hay valor que se repita más que otro)."

    # Obtener todos los valores con la frecuencia máxima
    moda = [valor for valor, freq in frecuencias.items() if freq == max_frecuencia]

    # Determinar el tipo de moda
    if len(moda) == 1:
        tipo = "Unimodal"
    elif len(moda) == 2:
        tipo = "Bimodal"
    else:
        tipo = "Multimodal"

    return moda, tipo