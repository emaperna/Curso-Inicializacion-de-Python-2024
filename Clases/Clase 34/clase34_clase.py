#Objetivo: Crear una clase llamada Producto 
# que tenga tres atributos: nombre, precio y cantidad. 
# Y tenga 3 metodos, Actualizar Precio, Actualizar Cantidad y Calcular valor total, 
#el primero modificara el precio del producto,
# el segundo la cantidad 
# y el ultimo debera multiplicar la cantidad por el precio del producto seleccionado para saber el valor total del inventario. 
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

# Ejemplo de uso
producto = Producto("Manzanas", 2.5, 100)
print(f"Valor total del inventario: ${producto.calcular_valor_total()}")

# Actualizar precio y cantidad
producto.actualizar_precio(3.0)
producto.actualizar_cantidad(120)
print(f"Nuevo valor total del inventario: ${producto.calcular_valor_total()}")