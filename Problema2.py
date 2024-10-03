'''
Problema 02:
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)
'''
def ingresar():
    correctas = [] 
    errores = [] 

    calificaciones = input("Ingrese las calificaciones separadas por comas: ")

    lista = calificaciones.split(",")

    for calificacion in lista:
        calificacion = calificacion.strip()  
        try:          
            if "." in calificacion: 
                raise ValueError(f"'{calificacion}' es un número decimal, no entero.")
            
            calificacion_entero = int(calificacion)
            correctas.append(calificacion_entero)  

        except ValueError as e:
            errores.append(str(e))

    print("Calificaciones correctas:", correctas)

    if errores:
        print("\nErrores encontrados:")
        for error in errores:
            print(error)

if __name__ == "__main__":
    ingresar()


