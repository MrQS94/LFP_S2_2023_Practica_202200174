from ProductoDAO import Producto_DAO
import os

handler_producto = Producto_DAO()

def menu():
    with open(os.getcwd() + "\\Lab LFP\\Practica 1\\data.inv" , 'r', encoding='UTF-8') as archivo:
        lineas = archivo.readlines()
        contador = 0
        for linea in lineas:
            contador += 1
            print(contador)
            print(linea.strip())
        
    
    
    
    
    
    
    """print('-' * 45)
    print('Practica 1 - Lenguajes Formales y de Programación')
    print('-' * 45)
    print('# Sistema de inventario: ')
    print()
    while True:
        print('1. Cargar inventario inicial.')
        print('2. Cargar instrucciones de movimientos.')
        print('3. Crear informe de inventario.')
        print('4. Salir.')
        print('-' * 20)
        opcion = input('Ingrese una opción: ')
        print('-' * 20)
        if opcion == '1':
            handler_producto.crear_producto()
        elif opcion == '2':
            handler_producto.imprimir_inventario()
        elif opcion == '3':
            print('Hola')
        elif opcion == '4':
            print('Saliendo del programa')
            break
        else:
            print('#### Ingrese una opción correcta ####'.upper())
        print('-' * 20)"""


menu()
