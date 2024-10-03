'''
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
Cree 2 objetos de tipo circulo y calcule su área.
'''
import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)


def Calculo():
    try:
        radio1 = float(input("Ingrese el radio del primer círculo: "))
        radio2 = float(input("Ingrese el radio del segundo círculo: "))

        circulo1 = CIRCULO(radio1)
        circulo2 = CIRCULO(radio2)

        print(f"El área del círculo 1 es: {circulo1.calcular_area():.2f}")
        print(f"El área del círculo 2 es: {circulo2.calcular_area():.2f}")
    except ValueError as Error:
        print("Error: El radio debe ser un número válido =",Error)


if __name__ == "__main__":
    Calculo()
