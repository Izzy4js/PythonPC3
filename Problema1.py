'''
Problema 01:
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser menor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
'''

def combustible():
    while True:
        try:
            fraccion = input("Ingrese una fracción (X/Y): ")
            x, y = fraccion.split("/")
            x = int(x)
            y = int(y)
            
            if y == 0:
                raise ZeroDivisionError
            
            elif x > y:
                raise ValueError("X debe ser menor o igual a Y")
            
            else : 
                resultado = calcular_combustible(x, y)
                return resultado
        
        except ValueError:
            print("Error: Solo números enteros y X debe de ser menor o igual a Y.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
            
def calcular_combustible(x,y):
    porcentaje = (x / y) * 100
            
    if porcentaje <= 1:
        return "E"
    elif porcentaje >= 99:
        return "F"
    else:
        return f"{round(porcentaje)}%"
        
if __name__ == "__main__":
    print(combustible())

        