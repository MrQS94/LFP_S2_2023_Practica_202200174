from Product import Producto

class Producto_DAO():
    def __init__(self):
        self.inventario = []
    
    def crear_producto(self):
        with open('data.inv', 'r') as archivo:
            lineas = archivo.readlines()
        
        for linea in lineas:
            datos = linea.strip().split(';')
            # Función tiene index 0 y nombre index 1
            funcion_y_nombre = datos[0].split(' ')

            if funcion_y_nombre[0] == 'crear_producto':
                nombre = funcion_y_nombre[1]
                cantidad = datos[1]
                precio_unitario = datos[2]
                ubicacion = datos[3]
                crear_producto = Producto(nombre, cantidad, precio_unitario, ubicacion)
                self.inventario.append(crear_producto)
    
    def imprimir_inventario(self):
        for detalles in self.inventario:
            print(f'Nombre: {detalles.nombre}')
            print(f'Cantidad: {detalles.cantidad}')
            print(f'Precio Unitario: {detalles.precio_unitario}')
            print(f'Ubicacion: {detalles.Ubicacion}')
            input()
    
