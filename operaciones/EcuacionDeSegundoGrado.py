import math


def resolver(a, b, c):
    discriminante = b**2 - 4 * a * c

    if discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"x1 = {x1}, x2 = {x2}"
    else:
        return "La ecuación no tiene soluciones reales."