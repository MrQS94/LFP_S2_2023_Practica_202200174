from Producto import Producto
from io import open
import os

class Producto_DAO():
    def __init__(self):
        self.inventario = []
        self.inventario_inicial = []
        self.ruta = os.getcwd()
        self.contador = 0

    def cargar_inventario_inicial(self, ruta):
        try:
            _, extension = os.path.splitext(ruta)
            if extension.lower() != '.inv':
                print("El archivo no es de tipo .inv")
                return
            with open(ruta, 'r', encoding='UTF-8') as archivo:
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
                        nuevo_producto_inicial = Producto(nombre, cantidad, precio_unitario, ubicacion)
                        self.inventario_inicial.append(nuevo_producto_inicial)
                        self.inventario.append(nuevo_producto)
                        print(f'El producto {nombre} y ubicación {ubicacion}, ha sido agregado existosamente.')
                    else:
                        print('Error, el producto no han sido agregados.')
            inventario_ordenado = sorted(self.inventario, key=lambda producto:(producto.ubicacion, producto.nombre))
            inventario_inicial_ordenado = sorted(self.inventario_inicial, key=lambda producto:(producto.ubicacion, producto.nombre))
            self.inventario = inventario_ordenado
            self.inventario_inicial = inventario_inicial_ordenado
        except FileNotFoundError:
            print('El archivo .inv no se encontró. Verifica la ubicación del archivo.')
    
    def cargar_instrucciones_de_movimiento(self, ruta):
        _, extension = os.path.splitext(ruta)
        if extension.lower() != '.mov':
            print("El archivo no es de tipo .mov")
            return
        with open(ruta, 'r', encoding='UTF-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                try:
                    instruccion, detalles = linea.strip().split(' ', 1)
                except ValueError:
                    print('EL archivo .mov está mal escrito.')
                    print('Recordar usar el siguiente ejemplo:')
                    print('agregar_stock <nombre>;<cantidad>;<ubicacion>')
                    print('vender_producto <nombre>;<cantidad>;<ubicacion>')
                partes = detalles.strip().split(';')
                
                if instruccion == 'agregar_stock':
                    self.agregar_stock(*partes)
                elif instruccion == 'vender_producto':
                    self.vender_producto(*partes)
                else:
                    print(f'La instrucción {instruccion}, no existe en el programa')
                
    def agregar_stock(self, nombre, cantidad, ubicacion):
        for producto in self.inventario:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                producto.cantidad += int(cantidad)
                print(f"Se agregaron {cantidad} unidades de {nombre} en {ubicacion}.")
                return
        print(f"Error: No se encontró el producto {nombre} en {ubicacion}.")
        
    def vender_producto(self, nombre, cantidad, ubicacion):
        for producto in self.inventario:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                if producto.cantidad >= int(cantidad):
                    producto.cantidad -= int(cantidad)
                    print(f"Se vendieron {cantidad} unidades de {nombre} en {ubicacion}.")
                    return
                else:
                    print(f"El producto {nombre} en {ubicacion}, no tiene el stock deseado ({cantidad}).")
                    return
        print(f"Error: No se encontró el producto {nombre} en {ubicacion}.")
            
    
    def crear_informe_de_inventario(self):
        ruta_inicial = f"{self.ruta}\\resultado_inicial_{self.contador}.txt"
        ruta_ = f"{self.ruta}\\resultado_{self.contador}.txt"
        self.contador += 1
        with open(ruta_, 'a', encoding='UTF-8') as archivo:
            archivo.write("Informe de Inventario:\n")
            archivo.write("Producto\t\t\tCantidad\t\t\tPrecio Unitario\t\t\tValor Total\t\t\tUbicación\n")
            archivo.write('-'*105)
            archivo.write('\n')
            for producto in self.inventario:
                archivo.write(f'{producto.nombre}\t\t\t\t\t{producto.cantidad}\t\t\t\t\t${producto.precio_unitario}\t\t\t\t\t${int(producto.cantidad) * float(producto.precio_unitario)}\t\t\t\t\t{producto.ubicacion}\n')
            archivo.close()
        
        with open(ruta_inicial, 'a', encoding='UTF-8') as archivo:
            archivo.write("Informe de Inventario Inicial:\n")
            archivo.write("Producto\t\t\tCantidad\t\t\tPrecio Unitario\t\t\tValor Total\t\t\tUbicación\n")
            archivo.write('-'*105)
            archivo.write('\n')
            for producto_inicial in self.inventario_inicial:
                archivo.write(f'{producto_inicial.nombre}\t\t\t\t\t{producto_inicial.cantidad}\t\t\t\t\t${producto_inicial.precio_unitario}\t\t\t\t\t${int(producto_inicial.cantidad) * float(producto_inicial.precio_unitario)}\t\t\t\t\t{producto_inicial.ubicacion}\n')
            archivo.close()
        
        print('El informe del inventario ha sido cread o actualizado en la siguiente ruta:')
        print(self.ruta)