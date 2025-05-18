#Ejercicios : 1

contador = 0
variable1 = input("ingrese un numero:")
variable2 = int(variable1)

variable2 = input("ingrese un numero:")
variable2 = int(variable2)

suma = int(variable1) + int(variable2)

contador = contador + 1 
print (f"El resultado de la suma es: {suma}")
print (f"El contador esta en : {contador}")

#Ejercicios : 2

variable = input("Ingrese un numero para la variable 1 ")
#variable = int(variable)
print(type(variable))

variable_2 = input("Ingrese un numero para la variable 2 ")
print(type(variable_2))
#variable_2 = int(variable_2)
print("El nuevo tipo de variable_2 es:")

suma = int(variable) + int(variable_2)
print(type(suma))
print(f"La suma de las dos variables es: {suma}")

#Ejercicios : 3

entrada = input("ingrese un numero:")
print (type(entrada))
print (entrada.isdigit())

if entrada.isdigit():
    print(f"el numero ingresado es {entrada}")
else:
    print(f"el numero ingresado es {entrada}")


#Trivias : 1

a = 20 
b = 19
c = 22
mensaje_true = "a es mayor a b y b es  menor a c"

mensaje_false = "esto no se cumple"

if a >b and b<c :
    print(mensaje_true)
else:
    print (mensaje_false)

#Trivias : 2

ingreso1 = 0 
nombre_apellido1 = input("Ingrese su Nombre y Apellido:")
direccion1 = input("Ingrese su Direccion:")
edad1 = int(input("Ingrese su Edad:"))

ingreso1 += 1

ingreso2 = 1
nombre_apellido2 = input("Ingrese su Nombre y Apellido:")
direccion2 = input("Ingrese su Direccion:")
edad2 = int(input("Ingrese su Edad:"))

ingreso2 += 1

ingreso3 = 2
nombre_apellido3 = input("Ingrese su Nombre y Apellido:")
direccion3 = input("Ingrese su Direccion:")
edad3 = int(input("Ingrese su Edad:"))

ingreso3 += 1

ingreso4 = 3
nombre_apellido4 = input("Ingrese su Nombre y Apellido:")
direccion4 = input("Ingrese su Direccion:")
edad4 = int(input("Ingrese su Edad:"))

ingreso4 += 1

edad_mayor = max(edad1, edad2, edad3, edad4)
edad_menor = min(edad1, edad2, edad3, edad4)

print(f"La persona más joven tiene {edad_menor} años.")
print(f"La persona más mayor tiene {edad_mayor} años.")

#Trivias : 3

valor1 = int(input("ingrese un numero:"))
valor2 = int(input("ingrese un numero:"))
valor3 = int(input("ingrese La operacion a realizar S,R,M o D:"))

S = valor1 + valor2
print(f"el resultado de sumar es: {S}")

R = valor1 - valor2
print(f"El resultado de restar es: {R}")

M = valor1 * valor2
print(f"El resultado de multiplicar es: {M}")

D = valor1 / valor2
print(f"El resultado de dividir es: {D}")


#print (f"Operación realizada con éxito, el resultado de {} es {}")
