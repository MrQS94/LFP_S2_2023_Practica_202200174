from Product import Producto
from io import open
import os

class Producto_DAO():
    def __init__(self):
        self.inventario = []
    
    def crear_producto(self):
        try:
            with open(os.getcwd() + "\\Lab LFP\\Practica 1\\data.inv" , 'r', encoding='UTF-8') as archivo:
                lineas = archivo.readlines()
                print(lineas)
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
                    print(f'El producto \"{nombre}\", ha sido agregado exitosamente.')
                    
        except FileNotFoundError:
            print('El archivo .inv no se encontró. Verifica la ubicación del archivo.')    
    
    def imprimir_inventario(self):
        i = 0
        for detalles in self.inventario:
            i += 1
            print('---------------- ', i, ' ----------------')
            print(f'Nombre: {detalles.nombre}')
            print(f'Cantidad: {detalles.cantidad}')
            print(f'Precio Unitario: {detalles.precio_unitario}')
            print(f'Ubicacion: {detalles.ubicacion}')
            
    
