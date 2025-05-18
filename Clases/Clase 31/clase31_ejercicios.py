#REPASO DE PROGRAMACION ORIENTADA A OBJETOS:
#return.. funcion devuelve algo ,return solo el procedimiento no

variable = "que tal"
class mi_objeto: #creamos el objeto mediante la clase (definida mediante class espacio y con mayuscula)
    def __init__(self): #self si o si se pasa y es referimo a si mismo, scoope. y luego pasamos parametros(...)
        self.variable = "Guille" #self. .. (atributo) global a toda la clase
        pass
    def mi_funcion(self):
        variable = "Hola" #variable local a esa funcion
        return variable  #sin return es un procedimiento
    def mi_procedimiento_hola_mundo(self):
        print("Hola mundo!")

obj = mi_objeto()
print(obj.mi_funcion().upper)
obj.mi_procedimiento_hola_mundo()
print(variable)



#Ejercicio 1: Crear una Clase de Rectángulo, Objetivo: Crear una clase llamada Rectangulo que tenga dos atributos: ancho y alto
#Que tenga dos metodos: area y perimetro.


import funciones as fp

class Rectangulo:
    '''
    Clase que crea un objeto Rectangulo, con metodos para mostrar todas sus caracteristicas, area y perimetro.
    \n
    En caso de que no se agreguen los argumentos al momento de declarar el objeto se tomaran los valores por defecto que es 0.
    
    '''
    def __init__(self)-> None:
        self.ancho = fp.ingresar_numero("Ingrese el ancho del rectangulo: ")
        self.alto =  fp.ingresar_numero("Ingrese el alto del rectangulo: ")
    
    def area(self):
        print(f"El area del rectangulo es {(self.ancho * self.alto)}")
        return
    def perimetro(self):
        print(f"El perimetro del rectangulo es {((self.ancho + self.alto) * 2)}")
        return
    def mostrar_caracteristicas(self):
        print(f"El ancho del rectangulo es {self.ancho} y el alto del rectangulo es {self.alto}")
        return


rectangulo_1 = Rectangulo()
rectangulo_1.mostrar_caracteristicas()
rectangulo_1.area()
rectangulo_1.perimetro()

#Trivia listas

lista_1 = [1,2,3]
lista_2 = lista_1
lista_1.append(4)
print(len(lista_2))

lista_2 = lista_1.copy()
print(len(lista_2))



lista_1 = ["Hola","Chau", "Nos vemos"]

lista_2 = lista_1

lista_1.append("Mundo")

print(len(lista_2))
print(lista_2)

lista_2.append("Los vemo")
print(len(lista_1))
print(id(lista_1))
print(id(lista_1))