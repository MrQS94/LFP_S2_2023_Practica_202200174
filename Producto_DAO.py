from Producto import Producto
from io import open
import os

class Producto_DAO():
    def __init__(self):
        self.inventario = []

    def cargar_inventario_inicial(self):
        try:
            with open(os.getcwd() + "\\Lab LFP\\LFP_S2_2023_Practica_202200174\\data_inventario.inv", 'r', encoding='UTF-8') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    try:
                        instruccion, detalles = linea.strip().split(' ', 1)
                    except ValueError:
                        print('EL archivo .inv está mal escrito.')
                        print('Recordar usar el siguiente ejemplo:')
                        print(
                            'crear_producto <nombre>;<cantidad>;<precio_unitario>;<ubicacion>')
                    if instruccion == 'crear_producto':
                        nombre, cantidad, precio_unitario, ubicacion = detalles.split(
                            ';')
                        nuevo_producto = Producto(
                            nombre, cantidad, precio_unitario, ubicacion)
                        self.inventario.append(nuevo_producto)
                        print(
                            f'El producto {nombre} y ubicación {ubicacion}, ha sido agregado existosamente.')
                    else:
                        print(
                            f'Error, El producto {nombre} y ubicación {ubicacion}, no han sido agregados.')
            inventario_ordenado = sorted(self.inventario, key=lambda producto:(producto.ubicacion, producto.nombre))
            self.inventario = inventario_ordenado
        except FileNotFoundError:
            print('El archivo .inv no se encontró. Verifica la ubicación del archivo.')
    
    def cargar_instrucciones_de_movimiento(self):
        with open(os.getcwd() + "\\Lab LFP\\LFP_S2_2023_Practica_202200174\\data_movimiento.mov", 'r', encoding='UTF-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                try:
                    instruccion, detalles = linea.strip().split(' ', 1)
                except ValueError:
                    print('EL archivo .mov está mal escrito.')
                    print('Recordar usar el siguiente ejemplo:')
                    print('agregar_stock <nombre>;<cantidad>;<ubicacion>')
                    print('vender_producto <nombre>;<cantidad>;<ubicacion>')
                nombre, cantidad, ubicacion = detalles.strip().split(';')
                
                if instruccion == 'vender_producto':
                    for producto in self.inventario:
                        if producto.ubicacion == ubicacion:
                            if producto.nombre == nombre:
                                if producto.cantidad >= int(cantidad):
                                    cantidad_temp = producto.cantidad
                                    producto.cantidad -= int(cantidad)
                                    print(
                                        f'El producto {nombre} y ubicación {ubicacion}, ha actualizado su stock de {cantidad_temp} a {producto.cantidad}.')
                                else:
                                    print(
                                        f'Error, El producto {nombre} y ubicación {ubicacion}, tiene un stock menor al deseado.')
                            else:
                                print(
                                    f'Error, No existe un producto ({nombre}), en esta ubicación ({ubicacion})')
                elif instruccion == 'agregar_stock':
                    for producto in self.inventario:
                        if producto.ubicacion == ubicacion:
                            if producto.nombre == nombre:
                                cantidad_temp = producto.cantidad
                                producto.cantidad += int(cantidad)
                                print(
                                    f'El producto {nombre} y ubicación {ubicacion}, ha actualizado su stock de {cantidad_temp} a {producto.cantidad}.')
                            else:
                                print(
                                    f'Error, No existe un producto ({nombre}), en esta ubicación ({ubicacion})')
                else:
                    print('Verifique que su archivo tenga la siguiente estructura.')
                    print('agregar_stock <nombre>;<cantidad>;<ubicacion>')
                    print('ó')
                    print('vender_producto <nombre>;<cantidad>;<ubicacion>')
                    input('Presione una tecla para continuar...')

    def crear_informe_de_inventario(self):
        ruta = os.getcwd() + "\\Lab LFP\\LFP_S2_2023_Practica_202200174\\resultado_123123.txt"
        with open(ruta, 'a', encoding='UTF-8') as archivo:
            archivo.write("Informe de Inventario:\n")
            archivo.write(
                "Producto\t\t\tCantidad\t\t\tPrecio Unitario\t\t\tValor Total\t\t\tUbicación\n")
            for producto in self.inventario:
                archivo.write(
                    f'{producto.nombre}\t\t\t\t\t{producto.cantidad}\t\t\t\t\t${producto.precio_unitario}\t\t\t\t\t${int(producto.cantidad) * float(producto.precio_unitario)}\t\t\t\t\t{producto.ubicacion}\n')
            archivo.close()
            print(
                'El informe del inventario ha sido cread o actualizado en la siguiente ruta:')
            print(ruta)