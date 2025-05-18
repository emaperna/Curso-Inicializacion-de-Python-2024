#Comparadores : Ejemplo 1

a = int(input("ingrese un numero:"))
b = int(input("ingrese otro numero:"))

resultado = (a == b)
print(f"el resultado es:{resultado}")

resultado = (a != b)
print(f"el resultado es:{resultado}")

resultado = (a > b)
print(f"el resultado es:{resultado}")

resultado = (a < b)
print(f"el resultado es:{resultado}")

resultado = (a >= b)
print(f"el resultado es:{resultado}")

resultado = (a <= b)
print(f"el resultado es:{resultado}")

#Comparadores : Ejemplo 2

edad = int(input("¿Cuantos años tienes?:"))
if edad >= 18 and edad <=20:
    print("Puedes entrar al boliche")
elif edad >=21 and edad <=49:
    print("Puedes entrar al boliche y tomar alcohol")
elif edad >=50:
    print("Andate a dormir")
else:
    print("No puedes entrar al boliche")      


#Ejercicios : 1

numero1 = input ("ingrese un numero a sumar:")
numero1 = int(numero1)

numero2 = int(input("ingrese un numero a sumar:"))

#print(id(numero1)) #arroja el numero de espacio que ocupa en la memoria
#print(id(numero2)) #arroja el numero de espacio que ocupa en la memoria

print(f"La suma de los numero es: {numero1 + numero2}")

#Ejercicios : 2

if 3 < 4:
    print("A")
else:
    print("B")
    print("C")

#Ejercicios : 3

temperatura = int(input("ingrese la temperatura"))
if temperatura > 0:
    print("Hace calor")
else:
    print("Hace frio")


temperatura = -1
if temperatura >= 0:
    print("Hace calor")
else:
    print("Hace frio")

#Ejercicios : 4

numero1 = input("ingrese un numero:")
numero1 = int(numero1)

numero2 = input("ingrese un numero:")
numero2 = int(numero2)

suma = numero1 + numero2
print (f"El resultado de la suma es {suma}")

