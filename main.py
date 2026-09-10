# main.py - Menú central de operaciones

def mostrar_menu():
    print("\n=== CALCULADORA - EJERCICIO 2 ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Módulo")
    print("5. División")
    print("6. Logaritmo")
    print("9. Factorial")
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

            elif opcion == "9":
                from operaciones import factorial
                n = float(input("Ingrese el número: "))
                print(f"Resultado: {factorial.calcular_factorial(n)}")

            elif opcion == "0":
                from operaciones import logaritmos
                numero = float(input("Ingrese el número: "))
                base_str = input("Ingrese la base (Enter para usar 2 por defecto): ")
                if base_str.strip() == "":
                    print(f"Resultado: {logaritmos.calcular_logaritmo(numero)}")
                else:
                    print(f"Resultado: {logaritmos.calcular_logaritmo(numero, float(base_str))}")
            
            else:
                print("Opción no válida")
        
        except ImportError as e:
            print(f"Error: No se pudo importar el módulo. {e}")
            print("La operación aún no está implementada por ningún equipo.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()