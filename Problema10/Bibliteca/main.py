from gestion import GestionBiblioteca
from libro import Libro

def main():
    gestion_biblioteca = GestionBiblioteca()

    while True:
        print("\n--- Menú ---")
        print("1. Agrega un libro a nuestra biblioteca")
        print("2. Listar los libros en nuestra biblioteca")
        print("3. Buscar libro segun su título")
        print("4. Buscar libro segun su autor")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                isbn = input("Ingrese el ISBN del libro: ")
                libro = Libro(titulo, autor, isbn)
                gestion_biblioteca.agregar_libro(libro)

            elif opcion == 2:
                print("\nLibros en la biblioteca:")
                print(gestion_biblioteca.listar_libros())

            elif opcion == 3:
                titulo = input("Ingrese el título del libro a buscar: ")
                resultados = gestion_biblioteca.buscar_por_titulo(titulo)
                if isinstance(resultados, str):
                    print(resultados)
                else:
                    for libro in resultados:
                        print(libro)

            elif opcion == 4:
                autor = input("Ingrese el autor del libro a buscar: ")
                resultados = gestion_biblioteca.buscar_por_autor(autor)
                if isinstance(resultados, str):
                    print(resultados)
                else:
                    for libro in resultados:
                        print(libro)

            elif opcion == 5:
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()