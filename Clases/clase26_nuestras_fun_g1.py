#Nuestras funciones 

#para definir una variable , nombre de la variable = valor de la variable
"""
#Ejercicio 1 - Saludar

def saludar(nombre:str):
    print(f"Hola,{nombre}")
    return

#saludar("Matias")
#saludar("Fermin") #Parametros escrachados, o a mano con input
nombre = input("Ingrese un nombre:")
saludar(nombre)

"""

#Ejercicio 2 - Calcular el area de un cuadrado (cuadrado-area A = L x L)

def area_cuadrado(lado: int)-> int: #Calcula el area
    area = lado * lado
    return area

cuadrado = int(input("Ingrese el valor del lado:"))
area = area_cuadrado(cuadrado)

print(f"El Area del cuadrado es igual: {area}")

