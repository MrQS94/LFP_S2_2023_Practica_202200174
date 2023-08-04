from Product import Producto
from io import open
import os

class Producto_DAO():
    def __init__(self):
        self.inventario = []
    
    def cargar_inventario_desde_archivo(self):
        try:
            texto = ''
            with open(os.getcwd() + "\\Lab LFP\\Practica 1\\data_inventario.inv" , 'r', encoding='UTF-8') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    try:
                        instruccion, detalles = linea.strip().split(' ', 1)
                    except ValueError:
                        print('EL archivo .inv está mal escrito.')
                        print('Recordar usar el siguiente ejemplo:')
                        print('crear_producto <nombre>;<cantidad>;<precio_unitario>;<ubicacion>')
                    if instruccion == 'crear_producto':
                        nombre, cantidad, precio_unitario, ubicacion = detalles.split(';')
                        nuevo_producto = Producto(nombre, cantidad, precio_unitario, ubicacion)
                        self.inventario.append(nuevo_producto)
                        texto = 'Inventario actualizado exitosamente.'
            
            return texto
        except FileNotFoundError:
            print('El archivo .inv no se encontró. Verifica la ubicación del archivo.')    
    
    def cargar_instrucciones_de_movimiento(self):
        with open(os.getcwd() + "\\Lab LFP\\Practica 1\\data_movimiento.mov" , 'r', encoding='UTF-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                try:
                    instruccion, detalles = linea.strip().split(' ', 1)
                except ValueError:
                    print('EL archivo .mov está mal escrito.')
                    print('Recordar usar el siguiente ejemplo:')
                    print('crear_producto <nombre>;<cantidad>;<precio_unitario>;<ubicacion>')
                nombre, cantidad, ubicacion = detalles.split(';')
                
                for producto in self.inventario:
                    if producto.nombre == nombre:
                        print('Hola') # Solo queda comparar los demas nombre y ubicaciones
                        # Seguir probando
                
                
                
                if instruccion == 'agregar_stock':
                    print()
                if instruccion == 'vender_producto':
                    print()
    
    
    
    
    def imprimir_inventario(self):
        i = 0
        for producto in self.inventario:
            i += 1
            print('---------------- ', i, ' ----------------')
            print('Nombre: ', producto.nombre)
            print('Cantidad: ', producto.cantidad)
            print('Precio Unitario: ', producto.precio_unitario)
            print('Ubicacion: ', producto.ubicacion)
            print()
            
    
