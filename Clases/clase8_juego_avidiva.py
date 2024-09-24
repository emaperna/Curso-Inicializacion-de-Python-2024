#3- Realizar un juego donde la computadora seleccione un numero aleatorio del 1 al 10 y nosotros 
#como jugadores tengamos hasta tres oportunidades de adivinar el numero, si ganamos que nos 
#muestre un mensaje felicitándonos y mostrando el numero aleatorio seleccionado. 
#Tener en cuenta que el numero seleccionado por la computadora al inicio es el mismo 
#que deben evaluar en los tres intentos!

#tambien quiero ver en que numero de intento lo acerte

import random 

entrada = input("Ingrese un Nro comprendido entre 1 a 10 y que pienses que yo haya elegido... : ")

if  entrada.isdigit(): 
    print(f"El numero ingresado es {entrada}.")

if not entrada.isdigit(): 
    print(f"El Valor ingresado {entrada} no es un numero, debes comenzar otra vez!!")
    exit()
    
numero_aleatorio = random.randint(1, 10) 
print(f"El Número seleccionado al azar fue: {numero_aleatorio}")
    
if entrada ==  numero_aleatorio:
    print("Felicitaciones !! Ganaste !!🚀🐍")
else:
    print("El numero al azar y el ingresado no coinciden , este fue tu primer intento... 🫨")

exit()