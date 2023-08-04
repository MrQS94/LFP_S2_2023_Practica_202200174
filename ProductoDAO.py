from Product import Producto
from io import open
import os

class Producto_DAO():
    def __init__(self):
        self.inventario = []
    
    def cargar_inventario_inicial(self):
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
                    if producto.ubicacion == ubicacion:
                        if instruccion == 'agregar_stock':
                            producto.cantidad += int(cantidad)
                            print('El stock ha sido actualizado.')
                            return True
                        elif instruccion == 'vender_producto':
                            if producto.cantidad >= int(cantidad):
                                producto.cantidad -= int(cantidad)
                                print('El producto ha sido vendido.')
                                return True
                            else:
                                print('La cantidad del producto es mayor al stock existente.')
                                return False
                        else:
                            print('La instrucción no ha sido escrita de una forma correcta.')
                            print('Recuerde usar \"agregar_stock\" o \"vender_producto\".')
                            return False
                                
                print('El producto no existe en está ubicación o tiene un nombre diferente.')
                return False
            
    def crear_informe_de_inventario(self):
        with open(os.getcwd() + "\\Lab LFP\\Practica 1\\resultado_123123.txt" , 'a', encoding='UTF-8') as archivo:
            archivo.write("Informe de Inventario:\n")
            archivo.write("Producto\t\t\tCantidad\t\t\tPrecio Unitario\t\t\tValor Total\t\t\tUbicación\n")
            for producto in self.inventario:
                archivo.write(f'{producto.nombre}\t\t\t\t\t{producto.cantidad}\t\t\t\t\t{producto.precio_unitario}\t\t\t\t\t{int(producto.cantidad) * float(producto.precio_unitario)}\t\t\t\t\t{producto.ubicacion}\n')
            archivo.close()
    
    
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
            
    
