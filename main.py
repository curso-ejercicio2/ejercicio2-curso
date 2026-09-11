# main.py - Menú central de operaciones




def mostrar_menu():
    print("\n=== CALCULADORA - EJERCICIO 2 ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Módulo")
    print("5. División")
    print("6. Valor absoluto")
    print("9. Factorial")
    print("10. Permutacion")
    print("11. Porcentaje")
    print("0. Salir")
    print("===============================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una operación: ")
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
        
        try:
            if opcion == "1":
                from operaciones import suma
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {suma.sumar(a, b)}")
            
            elif opcion == "2":
                from operaciones import resta
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {resta.restar(a, b)}")
            
            elif opcion == "3":
                from operaciones import multiplicacion
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {multiplicacion.multiplicar(a, b)}")
            
            elif opcion == "4":
                from operaciones import modulo
                a = float(input("Ingrese el dividendo: "))
                b = float(input("Ingrese el divisor: "))
                print(f"Resultado: {modulo.calcular_modulo(a, b)}")
            
            elif opcion == "5":
                from operaciones import division
                a = float(input("Ingrese el dividendo: "))
                b = float(input("Ingrese el divisor: "))
                print(f"Resultado: {division.dividir(a, b)}")

            elif opcion == "6":
                from operaciones import valor_absoluto
                a = float(input("Ingrese el número: "))
                print(f"Resultado: {valor_absoluto.calcular_valor_absoluto(a)}")
            
            elif opcion == "9":
                from operaciones import factorial
                n = float(input("Ingrese el número: "))
                print(f"Resultado: {factorial.calcular_factorial(n)}")
                
            elif opcion == "10":
                from operaciones import permutacion
                n = int(input("Ingrese n: "))
                r = int(input("Ingrese r: "))
                print(f"Resultado: {permutacion.calcular_permutaciones(n, r)}")

            elif opcion == "11":
                from operaciones import porcentaje
                total = float(input("Ingrese el número total: "))
                p = float(input("Ingrese el porcentaje: "))
                print(f"Resultado: {porcentaje.calcular_porcentaje(total, p)}")

            else:
                print("Opción no válida")
        
        except ImportError as e:
            print(f"Error: No se pudo importar el módulo. {e}")
            print("La operación aún no está implementada por ningún equipo.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
