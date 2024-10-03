'''
Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase. Además cree una clase CUADRADO que heredé de rectangulo. Cree un
objeto de tipo rectangulo y 1 de tipo cuadrado.
'''
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)


def Calculo():
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        lado = float(input("Ingrese el lado del cuadrado: "))

        rectangulo = RECTANGULO(largo, ancho)
        cuadrado = CUADRADO(lado)

        print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        print(f"El área del cuadrado es: {cuadrado.calcular_area()}")

    except ValueError as Error:
        print("Error: =",Error)
        

if __name__ == "__main__":
    Calculo()


