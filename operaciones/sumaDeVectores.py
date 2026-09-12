##Responsable: Dayana Ibarra Zarate (eq05)


def sumar_vectores(v1, v2):
    """Suma dos vectores elemento a elemento."""
    if len(v1) != len(v2):
        raise ValueError("Los vectores deben tener la misma longitud.")
    return [a + b for a, b in zip(v1, v2)]


# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    vector_a = [3, 5, -2, 8]
    vector_b = [1, 2, 9, -4]

    resultado = sumar_vectores(vector_a, vector_b)

    print(f"Vector A:  {vector_a}")
    print(f"Vector B:  {vector_b}")
    print(f"Resultado: {resultado}")