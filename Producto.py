class Producto():
    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)
        self.ubicacion = ubicacion