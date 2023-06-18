
from tienda_productos import Producto 

from tienda import Tienda

tienda = Tienda ("Mi tienda")

producto1 = Producto("Producto 1", 10.99, "Electrónicos")
producto2 = Producto("Producto 2", 5.99, "Ropa")
producto3 = Producto("Producto 3", 10.99, "Electrónicos")
producto5 = Producto("Producto 5", 5.99, "Lentes")
producto6 = Producto("Producto 6", 7.99, "Zapatos")

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

tienda.inflación(10)
tienda.hacer_liquidacion("Ropa", 20)
tienda.productos[1].vender_producto(2)
tienda.productos[2].vender_producto(3)

tienda.imprimir_productos_en_tienda()