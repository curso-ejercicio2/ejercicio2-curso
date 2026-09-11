# Responsable: Mirko Coca (eq01)

def promedio(valores: list[float]) -> float:
    if not valores:
        return 0.0

    total = 0.0

    for valor in valores:
        total += valor

    return total / len(valores)