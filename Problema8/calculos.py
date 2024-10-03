
import operaciones

def main():
    while True:
        try:
            print("\nSeleccione la operación:")
            print("1. Suma")
            print("2. Resta")
            print("3. Producto")
            print("4. División")
            print("5. Salir")

            opcion = int(input("Ingrese una opción (1-5): "))

            if opcion == 5:
                print("Saliendo del programa...")
                break
            
            if opcion not in [1, 2, 3, 4]:
                print("Error: Opción no válida. Por favor, seleccione un número entre 1 y 5.")
                continue 

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = operaciones.suma(num1, num2)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == 2:
                resultado = operaciones.resta(num1, num2)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == 3:
                resultado = operaciones.producto(num1, num2)
                print(f"Resultado del producto: {resultado}")
            elif opcion == 4:
                resultado = operaciones.division(num1, num2)
                print(f"Resultado de la división: {resultado}")

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
