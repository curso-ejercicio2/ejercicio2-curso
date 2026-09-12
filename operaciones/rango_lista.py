# Responsable: Mirko Coca (eq041)
def rango_lista(valores: list[float]) -> float:
    if not valores:
        raise ValueError("La lista no puede estar vacía")

    mayor = max(valores)
    menor = min(valores)

    return mayor - menor