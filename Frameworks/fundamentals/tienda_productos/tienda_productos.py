
class Producto: 
    contador_id = 0
    def __init__(self, nombre, precio, categoria, ):
        Producto.contador_id += 1
        self.id = Producto.contador_id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria


        
    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * (cambio_porcentaje / 100)
        else:
            self.precio -= self.precio * (cambio_porcentaje / 100)
            return self
        
    def Print_info(self):
        print(f"Producto:{self.nombre} - Categoria:{self.categoria} - Precio:{self.precio}")
        return self
    
    def vender_producto(self, id_producto):
        if self.id == id_producto:
            print("Producto vendido:", self.nombre)
        else:
            print("No se encontró un producto con el ID especificado.")
            return self


        

        
    