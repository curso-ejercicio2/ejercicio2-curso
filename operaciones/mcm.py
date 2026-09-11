# operaciones/mcm.py
# Responsable: Dennis Daniel Condori Mollo (eq06)
def mcm(a, b):
    if a == 0 or b == 0:
        return 0

    a = abs(a)
    b = abs(b)

    mayor = max(a, b)

    while mayor % a != 0 or mayor % b != 0:
        mayor += 1

    return mayor