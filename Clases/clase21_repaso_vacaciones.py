#VARIABLE (en mayuscula para python es una constante y no una variable que no puede mutar (inmutable).

VARIABLE = "Hola"

constante = "Chau"

#Lista se declara con corchete [] y las variables pueden mutar.

Lista = ["Hola", "chau", constante]
Lista.remove("Hola")
#print(Lista)

lista = ["Hola", "chau", constante]
elemento_eliminado = Lista.pop(0) #elimina el ultimo si no le pasamos un indice.
#print(f"Este es el elemento eliminado {elemento_eliminado}")
#print(Lista.pop())

print(lista.remove("Hola"))

tuplas = ("Hola", "chau", constante)
conjuntos = {"Hola", "chau", constante}
diccionario = {"Gaspar":23, "Diego":27, "Guillermo":29 , "Paula":17} #diccionario por la estructura de sus elementos. 
lista_nombre_edad = [["Gaspar",23], ["Diego",27]] 

#print(lista_nombre_edad[1][0])
#print(diccionario["Gaspar"])

#Tupla se declara con parentesis () tiene valores inmutables.

#Diccionario no acepta indices,(poder obtener un valor por una clave). Los recorremos  con for i y agregamos con imput.

#For recorre iterables o nros especificos, while en base a una condicion.
#Para recorrer listas usamos for.
#Condicional en base a una condicion que se cumpla o no.

'''
for i in range(10):
    print(i)
    if i == 5:
        break
    
while i in range(10):
    print(i)
    if i == 5:
        break
'''

print("Esto impriime el for")
for i in range(10):
    print(i)
    if i == 5:
        break
print("Esto imprime el while:")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 6:
        break

#el precio del mañana (pelicula), update (serie)

#Realizar un login que permita ingresar con varios usuarios y  contraseñas.

USUARIO = "Diego"
PASSWORD = "Diego*123"

ingrese_usuario = input("Ingrese el usuario a continuacion:... ")
ingrese_pass = input("Ingrese la contraseña a continuacion:... ")

if USUARIO == ingrese_usuario and PASSWORD == ingrese_pass:
    print("Bienvenido usuario")