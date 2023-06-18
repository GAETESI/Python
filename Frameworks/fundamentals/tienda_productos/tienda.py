from tienda_productos import Producto

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self. productos =  []
        
    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        return self
        
    def inflación(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)
            return self
            
    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
              producto.actualizar_precio(porcentaje_descuento, False)
              return self
          
    def imprimir_productos_en_tienda(tienda):
      print("Productos en la tienda:")
      for producto in tienda.productos:
        print("ID:", producto.id)
        print("Nombre:", producto.nombre)
        print("Precio:", producto.precio)
        print("Categoría:", producto.categoria)

        
        
tienda = Tienda("Mi Tienda")

producto1 = Producto("Producto 1", 10.99, "Electrónicos")
producto2 = Producto("Producto 2", 5.99, "Ropa")
producto3 = Producto("Producto 3", 7.99, "Ropa")

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

tienda.imprimir_productos_en_tienda()


