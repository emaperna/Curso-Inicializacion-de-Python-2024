#POO en 🐍🐍
#Definiendo objetos
#Creando una clase de vehiculo

class vehiculos:
    def __init__(self, color:str, puertas:int, modelo:str, marca:str)-> None: #()LO PASADO DENTRO SON VARIABLES
        self.color = color
        self.puertas = puertas
        self.modelo = modelo
        self.marca = marca
        self.encendido = False

    def encender(self):
        self.encendido = True
    def apagar(self):
        self.apagado = False

    def mostrar_caracteristicas(self):
        esta_encendido = "El auto esta encendido"
        if self.encendido == False : 
            esta_encendido == " El auto esta apagado"

        print(f"El auto es de color {self.color} tiene {self.puertas} puertas y el modelo es {self.modelo} de la marca {self.marca}. El auto esta {esta_encendido} ")

    def mostrar_color(self):
        return

auto_diego = vehiculos("rojo", 2, "Fiesta", "Ford") #CREAMOS UNA CLASE DEL OBJETO VEHICULOS
auto_diego.mostrar_caracteristicas()
auto_diego.encender()
auto_diego.apagar()
auto_diego.mostrar_caracteristicas()

# auto_gaspar = vehiculos("azul", 4, "Duster", "Renault")
# auto_leti = vehiculos("negro", 5, "208", "Peugeot")
# print(f"El color es {auto_gaspar.color}")
# auto_gaspar.color = "verde"
# print(f"El color es {auto_gaspar.color}")
# auto_gaspar.mostrar_caracteristicas()