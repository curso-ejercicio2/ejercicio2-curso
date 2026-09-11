import math

angulo = float(input("Ingrese el ángulo en grados: "))

resultado = math.tan(math.radians(angulo))

print(f"La tangente de {angulo}° es: {resultado:.2f}")