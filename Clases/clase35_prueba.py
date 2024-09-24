

# 1. Variables y tipos de datos:

# Variables: Espacios en memoria donde se almacenan datos. 
# En Python, no es necesario declarar el tipo de una variable al momento de su creación.

'''
x = 5
nombre = "Ana"

'''

#Tipos de datos: Los más comunes en Python incluyen:

#Números enteros (int): 5
#Números de punto flotante (float): 3.14
#Cadenas de texto (str): "Hola"
#Booleanos (bool): True, False
#Listas (list): [1, 2, 3]
#Diccionarios (dict): {"clave": "valor"}
#Tuplas (tuple): (1, 2, 3)
#Conjuntos (set): {1, 2, 3}

#--------------------------------------------

#2. Operadores aritméticos y de comparación:

#Aritméticos:

#Suma (+): 5 + 3
#Resta (-): 5 - 3
#Multiplicación (*): 5 * 3
#División (/): 5 / 3 (retorna un float)
#División entera (//): 5 // 3 (retorna un int)
#Módulo (%): 5 % 3 (retorna el resto de la división)
#Exponenciación (**): 5 ** 3


#Comparación:

#Igual a (==): 5 == 3 (retorna False)
#Diferente de (!=): 5 != 3 (retorna True)
#Mayor que (>): 5 > 3 (retorna True)
#Menor que (<): 5 < 3 (retorna False)
#Mayor o igual que (>=): 5 >= 3 (retorna True)
#Menor o igual que (<=): 5 <= 3 (retorna False)

#--------------------------------------------

#3. Estructuras de control: If, For y While:

#If:

'''
if x > 10:
    print("Mayor que 10")
elif x == 10:
    print("Igual a 10")
else:
    print("Menor que 10")

'''

#For:

'''
for i in range(5):  # Del 0 al 4
    print(i)

'''

#Listas:

'''

lista = [1, 2, 3]
for item in lista:
    print(item)

'''

#While:

'''
count = 0
while count < 5:
    print(count)
    count += 1

'''

#--------------------------------------------

#4. Listas:

#Definición:

'''

lista = [1, 2, 3, 4]

'''

#Acceso a elementos:

'''
print(lista[0])  # Imprime 1

'''

#Operaciones comunes:

#Agregar elementos: lista.append(5)
#Eliminar elementos: lista.remove(2)
#Slicing: lista[1:3] (retorna [2, 3])

#--------------------------------------------

#Funciones:

#Definición y llamada:

'''
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Ana"))  # Imprime "Hola, Ana"

'''
#Parámetros por defecto:

'''
def saludar(nombre="Mundo"):
    return f"Hola, {nombre}"

'''
#--------------------------------------------

#6. Programación orientada a objetos:

#Clases y objetos:

'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

persona = Persona("Ana", 30)
print(persona.presentarse())  # Imprime "Hola, soy Ana y tengo 30 años."

'''

#Herencia:

'''
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

'''
#--------------------------------------------

#7. Imports básicos de Python:

#Importar módulos:

'''
import math
print(math.sqrt(16))  # Imprime 4.0

'''

#Importar funciones específicas:

'''
from math import sqrt
print(sqrt(16))  # Imprime 4.0

'''

#Alias para módulos:

'''
import numpy as np
array = np.array([1, 2, 3])

'''

# Definimos una clase llamada 'Coche'
class Coche:
    # El método '__init__' es el constructor de la clase
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # Método para describir el coche
    def describir(self):
        return f"{self.marca} {self.modelo} ({self.año})"

    # Método para simular encender el coche
    def encender(self):
        return f"El {self.marca} {self.modelo} está encendido."

# Creamos un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2022)

# Llamamos a los métodos del objeto
print(mi_coche.describir())  # Salida: Toyota Corolla (2022)
print(mi_coche.encender())   # Salida: El Toyota Corolla está encendido.
