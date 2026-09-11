# operacion/promedio.py
# Responsable: Dajhana Arce Rocha (eq01)
def promedio(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)
