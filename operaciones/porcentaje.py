# operaciones/porcentaje.py

# Responsable: Alex Cristian Saavedra Veliz (eq07)

def porcentaje(total: float, porcentaje: float) -> float:
    """Calcula el porcentaje de una cantidad base.

    Ejemplo: porcentaje(200, 15) -> 30.0
    """
    return (total * porcentaje) / 100.0

if __name__ == "__main__":
    print("--- Pruebas Locales: Porcentaje ---")
    base = 200.0
    tasa = 15.0
    print(f"{tasa}% de {base} = {porcentaje(base, tasa)}")