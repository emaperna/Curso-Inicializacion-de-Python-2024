'''
Ejercicio 3: Crear una Clase de Producto

Objetivo: Crear una clase llamada Producto que tenga tres atributos: nombre, precio y cantidad. 
Y tenga 3 metodos, Actualizar Precio, Actualizar Cantidad y Calcular valor total
el primero modificara el precio del producto, el segundo la cantidad y el ultimo debera multiplicar la
cantidad por el precio del producto seleccionado para saber el valor total del inventario
'''
import funciones as fp
class Producto:
    def __init__(self,cantidad : int | None = 0):
        self.nombre = fp.validar_texto("Ingrese el nombre del Producto : ")
        self.precio = fp.ingresar_numero("Ingrese el precio del Producto : $ ")
        self.cantidad = cantidad
        pass
    
    def actualizar_precio(self):
        actualiza = int(input("Ingrese el valor de actualizacion de precio : $ "))
        self.precio = (self.precio + actualiza)
        print(f"Se actualizó el precio del producto a : $ {self.precio} ")
        return actualiza
    
    def actualizar_cantidad(self):
        actualiza = int(input("Ingrese la cantidad del producto : "))
        self.cantidad = actualiza
        print(f"La cantidad del producto en stock es : {actualiza} ")
        return actualiza
    
    def calcular_cantidad(self):
        totales = (self.cantidad * self.precio)
        print(f"El valor total del inventario es : $ {totales} ")

negocio = Producto()
negocio.actualizar_precio()
negocio.actualizar_cantidad()
negocio.calcular_cantidad()
