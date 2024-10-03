'''
Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
método para agregar productos y otra para mostrar toda la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
agregar más atributos a los productos para que se puedan hacer otras funcionalidades.
Cree 3 objetos de tipo producto y agregalos al catálogo. Colocar ejemplos empleandolos
métodos de catálogo.
'''
class Producto:
    def __init__(self, nombre, año, precio):
        self.nombre = nombre
        self.año = año
        self.precio = precio

    def mostrar(self):
        return f"Producto: {self.nombre}, Año: {self.año}, Precio: ${self.precio:.2f}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar(self, nombre, año, precio):
        nuevo_producto = Producto(nombre, año, precio)
        self.productos.append(nuevo_producto)
        print(f"El producto {nombre} se ha  agregado al catálogo.")

    def mostrar(self):
        return "\n".join(producto.mostrar() for producto in self.productos)

    def filter_per_year(self, año):
        return [producto.mostrar() for producto in self.productos if producto.año == año] or ["No hay productos en ese año."]

    def filter_per_price(self, min_price, max_price):
        return [producto.mostrar() for producto in self.productos if min_price <= producto.precio < max_price] or ["No hay productos en este rango de precios."]


def obtener_datos_producto():
    while True:
        try:
            nombre = input('Digite el nombre del producto -> ')
            año = int(input('Digite el año de producción -> '))
            precio = float(input('Digite el precio del producto -> '))
            return nombre, año, precio
        except ValueError:
            print('Error. Digite los valores correctamente (nombre=cadena, año=entero, precio=decimal)')


def main():
    catalogo = Catalogo()
    nombre, año, precio = obtener_datos_producto()
    catalogo.agregar(nombre, año, precio)
    print(catalogo.mostrar())

    while True:
        try:
            opcion = int(input('¿Qué desea hacer?\n1. Mostrar productos\n2. Agregar otro producto\n3. Filtrar productos\n4. Salir\n -> '))
            match opcion:
                case 1:
                    print(catalogo.mostrar())
                case 2:
                    nombre, año, precio = obtener_datos_producto()
                    catalogo.agregar(nombre, año, precio)
                    print(catalogo.mostrar())
                case 3:
                    filtro = int(input('¿Desea filtrar por:\n1. Año\n2. Precio\n-> '))
                    if filtro == 1:
                        año_filtro = int(input('Digite año para filtrar -> '))
                        resultados_filtrados = catalogo.filter_per_year(año_filtro)
                        print("\n".join(resultados_filtrados))
                    elif filtro == 2:
                        print("Intervalos de precios:\n1. 0 a 100\n2. 100 a 300\n3. 300 o más")
                        intervalo = int(input('Seleccione un intervalo de precios(1-3) -> '))
                        if intervalo == 1:
                            resultados_filtrados = catalogo.filter_per_price(0, 100)
                        elif intervalo == 2:
                            resultados_filtrados = catalogo.filter_per_price(100, 300)
                        elif intervalo == 3:
                            resultados_filtrados = catalogo.filter_per_price(300, float('inf'))
                        else:
                            print("Selección no válida.")
                            continue
                        print("\n".join(resultados_filtrados))
                    else:
                        print("Selección no válida.")
                case 4:
                    break
                case _:
                    print('Error, digite un número perteneciente al menú(1-4)')
        except ValueError:
            print('Error, digite un valor perteneciente al menú(1-4)')


if __name__ == '__main__':
    main()
