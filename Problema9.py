'''
Problema 09:
Cree un menú que reutilice a manera de módulos las clases creadas en los ejercicios 3 y 4. El
menú para utilizar deberá tener las siguientes funcionalidades:
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir.
Deberá emplear un método que valide que los datos ingresados sean números validos y
positivos en caso corresponda.

'''
from Problema3 import CIRCULO
from Problema4 import RECTANGULO, CUADRADO

def validar(valor):
    try:
        numero = float(valor)
        if numero > 0:
            return numero
        else:
            print("El número debe ser positivo.")
            return None
    except ValueError:
        print("El valor ingresado no es un número válido.")
        return None


def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = validar(input("Ingrese el radio del círculo: "))
            if radio is not None:
                circulo = CIRCULO(radio)
                print(f"El área del círculo es: {circulo.calcular_area()}")
        elif opcion == "2":
            largo = validar(input("Ingrese el largo del rectángulo: "))
            ancho = validar(input("Ingrese el ancho del rectángulo: "))
            if largo is not None and ancho is not None:
                rectangulo = RECTANGULO(largo, ancho)
                print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        elif opcion == "3":
            lado = validar(input("Ingrese el lado del cuadrado: "))
            if lado is not None:
                cuadrado = CUADRADO(lado)
                print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()