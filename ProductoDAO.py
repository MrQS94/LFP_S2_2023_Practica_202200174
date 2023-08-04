from Product import Producto
from io import open
import os

class Producto_DAO():
    def __init__(self):
        self.inventario = []
    
    def cargar_inventario_desde_archivo(self):
        try:
            texto = ''
            with open(os.getcwd() + "\\Lab LFP\\Practica 1\\data.inv" , 'r', encoding='UTF-8') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    instruccion, detalles = linea.strip().split(' ', 1)
                    if instruccion == 'crear_producto':
                        nombre, cantidad, precio_unitario, ubicacion = detalles.split(';')
                        nuevo_producto = {
                            "nombre": nombre,
                            "cantidad": cantidad,
                            "precio_unitario": precio_unitario,
                            "ubicacion": ubicacion
                        }
                        self.inventario.append(nuevo_producto)
                        texto = 'Inventario actualizado exitosamente.'
                    else:
                        texto = 'El archivo no ha sido escrito correctamente.'
            
            return texto
            
        except FileNotFoundError:
            print('El archivo .inv no se encontró. Verifica la ubicación del archivo.')    
    
    def imprimir_inventario(self):
        i = 0
        for producto in self.inventario:
            i += 1
            print('---------------- ', i, ' ----------------')
            print('Nombre: ', producto['nombre'])
            print('Cantidad: ', producto['cantidad'])
            print('Precio Unitario: ', producto['precio_unitario'])
            print('Ubicacion: ', producto['ubicacion'])
            print()
            
    
