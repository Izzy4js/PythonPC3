from libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def listar_libros(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        return "\n".join(str(libro) for libro in self.libros)

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        return resultados if resultados else "No se encontraron libros con ese título."

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        return resultados if resultados else "No se encontraron libros de ese autor."