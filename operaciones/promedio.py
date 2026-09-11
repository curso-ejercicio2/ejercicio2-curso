#Responsable: Ticona Chura Stefani Mishel (eq04)
def promedio(numeros):
    suma = sum(numeros)          
    cantidad = len(numeros)
    
    cociente = 0
    while suma >= cantidad:
        suma -= cantidad
        cociente += 1
    
    return cociente

print(promedio([4, 8, 12, 16]))  