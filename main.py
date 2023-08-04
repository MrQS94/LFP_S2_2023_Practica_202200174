from ProductoDAO import Producto_DAO

handler_producto = Producto_DAO()

def menu():
    print('-' * 45)
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
            print(handler_producto.cargar_inventario_inicial())
        elif opcion == '2':
            handler_producto.cargar_instrucciones_de_movimiento()
        elif opcion == '3':
            handler_producto.crear_informe_de_inventario()
        elif opcion == '4':
            print('Saliendo del programa')
            break
        else:
            print('#### Ingrese una opción correcta ####'.upper())
        print('-' * 20)

menu()
