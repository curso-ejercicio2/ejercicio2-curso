# main.py - Menú central de operaciones

def mostrar_menu():
    print("\n=== CALCULADORA - EJERCICIO 2 ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Módulo")
    print("5. División")
    print("6. Valor absoluto")
    print("7. Potencia")
    print("8. Raíz")
    print("9. Factorial")
    print("10. Permutación")
    print("11. Decimal a binario")
    print("12. Resta de fracciones")
    print("13. Suma de una lista")
    print("14. Resta de varios valores")
    print("15. Multiplicación de matrices")
    print("16. Módulo de una lista (con negativos)")
    print("17. División de positivos")
    print("18. Potencia vectorizada (listas)")
    print("19. Multiplicación de una lista")
    print("20. Porcentaje")
    print("21. Suma de Cuadrados")
    print("22. Máximo Común Divisor (MCD)")
    print("23 Division de una lista")
    print("24. Numero par o impar")
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
                usar_varios = input("¿Restar varios valores además de estos dos? (s/n): ").strip().lower()
                if usar_varios == "s":
                    extras = input("Ingrese valores adicionales separados por coma (o dejar vacío): ").strip()
                    valores_extra = [float(v) for v in extras.split(",") if v.strip()] if extras else []
                    print(f"Resultado: {resta.restar_varios(a - b, *valores_extra)}")
                else:
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
                validar = input("¿Validar que ambos sean positivos? (s/n): ").strip().lower()
                if validar == "s":
                    print(f"Resultado: {division.dividir_positivos(a, b)}")
                else:
                    print(f"Resultado: {division.dividir(a, b)}")

            elif opcion == "6":
                from operaciones import valor_absoluto
                a = float(input("Ingrese el número: "))
                print(f"Resultado: {valor_absoluto.calcular_valor_absoluto(a)}")

            elif opcion == "7":
                from operaciones import potencia
                a = float(input("Ingrese la base: "))
                b = float(input("Ingrese el exponente: "))
                print(f"Resultado: {potencia.calcular_potencia(a, b)}")

            elif opcion == "8":
                from operaciones import raiz
                num_base = float(input("Ingrese el número (base): "))
                num_indice = float(input("Ingrese el índice de la raíz: "))
                resultado = raiz.calcular_raiz(num_base, num_indice)
                print(f"Resultado: {resultado}")

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
                from operaciones import decimal_binario
                n = float(input("Ingrese el número decimal: "))
                print(f"Resultado: {decimal_binario.decimal_a_binario(n)}")

            elif opcion == "12":
                from operaciones import fracciones
                num1 = int(input("Ingrese el numerador de la primera fracción: "))
                den1 = int(input("Ingrese el denominador de la primera fracción: "))
                num2 = int(input("Ingrese el numerador de la segunda fracción: "))
                den2 = int(input("Ingrese el denominador de la segunda fracción: "))
                resultado = fracciones.restar_fracciones(num1, den1, num2, den2)
                print(f"Resultado: {resultado}")

            elif opcion == "13":
                from operaciones import suma
                datos = input("Ingrese los números separados por coma: ")
                lista = [float(x.strip()) for x in datos.split(",")]
                print(f"Resultado: {suma.suma_lista(lista)}")

            elif opcion == "14":
                from operaciones import resta
                inicial = float(input("Ingrese el valor inicial: "))
                datos = input("Ingrese los valores a restar separados por coma: ")
                valores = [float(x.strip()) for x in datos.split(",")]
                print(f"Resultado: {resta.restar_varios(inicial, *valores)}")

            elif opcion == "15":
                from operaciones import multiplicacion
                print("Ingrese la matriz A fila por fila (números separados por coma).")
                print("Escriba una línea vacía para terminar.")
                matriz_a = []
                while True:
                    fila = input("Fila A: ")
                    if fila == "":
                        break
                    matriz_a.append([float(x.strip()) for x in fila.split(",")])

                print("Ingrese la matriz B fila por fila (números separados por coma).")
                print("Escriba una línea vacía para terminar.")
                matriz_b = []
                while True:
                    fila = input("Fila B: ")
                    if fila == "":
                        break
                    matriz_b.append([float(x.strip()) for x in fila.split(",")])

                print(f"Resultado: {multiplicacion.multiplicar_matriz(matriz_a, matriz_b)}")

            elif opcion == "16":
                from operaciones import modulo
                datos = input("Ingrese los números separados por coma: ")
                lista = [float(x.strip()) for x in datos.split(",")]
                divisor = float(input("Ingrese el divisor: "))
                print(f"Resultado: {modulo.modulo_lista_negativos(lista, divisor)}")

            elif opcion == "17":
                from operaciones import division
                a = float(input("Ingrese el dividendo (positivo): "))
                b = float(input("Ingrese el divisor (positivo): "))
                print(f"Resultado: {division.dividir_positivos(a, b)}")

            elif opcion == "18":
                from operaciones import potencia
                datos_bases = input("Ingrese las bases separadas por coma: ")
                bases = [float(x.strip()) for x in datos_bases.split(",")]
                datos_exp = input("Ingrese los exponentes separados por coma: ")
                exponentes = [float(x.strip()) for x in datos_exp.split(",")]
                print(f"Resultado: {potencia.potencia_vectorizada(bases, exponentes)}")

            elif opcion == "19":
                from operaciones import multiplicacion
                datos = input("Ingrese los números separados por coma (ej. 2,3,4): ")
                valores = [float(x.strip()) for x in datos.split(",")]
                print(f"Resultado: {multiplicacion.multiplicar_lista(valores)}")
                
            elif opcion == "20":
                from operaciones import porcentaje
                try:
                    total = float(input("Ingrese la cantidad base (total): "))
                    pct = float(input("Ingrese el porcentaje a calcular (%): "))
                    print(f"Resultado: {porcentaje.porcentaje(total, pct)}")
                except ValueError:
                    print("Error: Debe ingresar números válidos, no texto.")
                except TypeError as e:
                    print(f"Error: {e}")    
                
            elif opcion == "21":  
                from operaciones import suma_cuadrados
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                print(f"Resultado: {suma_cuadrados.suma_cuadrados(a, b)}")
            
                
            elif opcion == "22":
               from operaciones import mcd
               a = int(input("Ingrese el primer número: "))
               b = int(input("Ingrese el segundo número: "))
               print(f"Resultado: {mcd.calcular_mcd(a, b)}")

            
            elif opcion == "23":
                from operaciones import division

                datos = input("Ingrese los números separados por coma: ")
                lista = [float(x.strip()) for x in datos.split(",")]
                divisor = float(input("Ingrese el divisor: "))
                print(f"Resultado: {division.dividir_lista(lista, divisor)}")

            elif opcion == "24":
                from operaciones import Numero_par_impar
                n = int(input("Ingrese el número: "))
                print(Numero_par_impar.verificar_numero(n))
                
            else:
                print("Opción no válida")

        except ImportError as e:
            print(f"Error: No se pudo importar el módulo. {e}")
            print("La operación aún no está implementada por ningún equipo.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
