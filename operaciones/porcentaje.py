# operacion porcentaje
# Responsable : David Cabrera /eq09
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

if numero2 != 0:
    porcentaje = (numero1 / numero2) * 100
    print(f"{numero1} es el {porcentaje}% de {numero2}")
else:
    print("No se puede dividir entre cero.")
