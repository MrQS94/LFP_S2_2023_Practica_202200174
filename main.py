from Producto_DAO import Producto_DAO

handler_producto = Producto_DAO()

def menu():
    print('-' * 45)
    print('Practica 1 - Lenguajes Formales y de Programación')
    print('-' * 45)
    while True:
        print('# Sistema de inventario: ')
        print()
        print('1. Cargar inventario inicial.')
        print('2. Cargar instrucciones de movimientos.')
        print('3. Crear informe de inventario.')
        print('4. Salir.')
        print('-' * 30)
        opcion = input('Ingrese una opción: ')
        print('-' * 30)
        print()
        if opcion == '1':
            ruta_inv = input('Ingrese la ruta del archivo .inv: ')
            handler_producto.cargar_inventario_inicial(ruta_inv)
        elif opcion == '2':
            ruta_mov = input('Ingrese la ruta del archivo .mov: ')
            handler_producto.cargar_instrucciones_de_movimiento(ruta_mov)
        elif opcion == '3':
            handler_producto.crear_informe_de_inventario()
        elif opcion == '4':
            print('Saliendo del programa...')
            break
        else:
            print('#### Ingrese una opción correcta ####'.upper())
        print()
        print('-' * 30)
menu()
