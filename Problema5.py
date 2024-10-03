'''
Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante.
'''
class Alumno:
    def __init__(self, nombre, numero_registro, edad):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = edad 
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        print(f"Edad: {self.edad}")
        print(f"Notas: {self.notas}")

    def setNota(self, nota):
        self.notas.append(nota)


def asignar():
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        numero_registro = input("Ingrese el número de registro del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))

        alumno = Alumno(nombre, numero_registro, edad)

        notas_input = input("Ingrese las notas separadas por comas: ")
        notas_lista = notas_input.split(",")

        for nota in notas_lista:
            try:
                alumno.setNota(float(nota.strip())) 
            except ValueError:
                print(f"Error: '{nota}' no es una nota válida y será ignorada.")

        print("\nInformación del alumno:")
        alumno.display()

        continuar = input("\n¿Desea agregar otro alumno? (si/no): ").lower()
        if continuar != 'si':
            break 
        
if __name__ == "__main__":
    asignar()