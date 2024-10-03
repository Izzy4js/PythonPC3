'''
Problema 07:
'''
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        elif self.x == 0:
            return "El punto está sobre el eje Y."
        elif self.y == 0:
            return "El punto está sobre el eje X."
        elif self.x > 0 and self.y > 0:
            return "El punto está en el cuadrante I."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el cuadrante II."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el cuadrante III."
        else:
            return "El punto está en el cuadrante IV."

    def vector(self, otro):
        return (otro.x - self.x, otro.y - self.y)

    def distancia(self, otro):
        return math.sqrt((otro.x - self.x) ** 2 + (otro.y - self.y) ** 2)


class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        self.punto_inicial = punto_inicial if punto_inicial else Punto(0, 0)
        self.punto_final = punto_final if punto_final else Punto(0, 0)

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()



if __name__ == "__main__":
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    print("Puntos:")
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print(f"D: {D}")

    print("\nCuadrantes:")
    print(f"A: {A.cuadrante()}")
    print(f"C: {C.cuadrante()}")
    print(f"D: {D.cuadrante()}")

    vector_AB = A.vector(B)
    vector_BA = B.vector(A)
    print("\nVectores:")
    print(f"Vector AB: {vector_AB}")
    print(f"Vector BA: {vector_BA}")

    distancia_AB = A.distancia(B)
    distancia_BA = B.distancia(A)
    print("\nDistancias:")
    print(f"Distancia A-B: {distancia_AB}")
    print(f"Distancia B-A: {distancia_BA}")

    puntos = [A, B, C]
    mas_lejos = max(puntos, key=lambda p: p.distancia(Punto(0, 0)))
    print(f"\nEl punto más lejano del origen es: {mas_lejos}")

    rectangulo = Rectangulo(A, B)
    print("\nRectángulo:")
    print(f"Base: {rectangulo.base()}")
    print(f"Altura: {rectangulo.altura()}")
    print(f"Área: {rectangulo.area()}")
