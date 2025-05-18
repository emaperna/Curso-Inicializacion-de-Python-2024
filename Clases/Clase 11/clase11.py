#Ejercicios: 1

#Contador a la luna.

contador = 10
while contador >= 0:
    print(contador)
    contador -= 1
    
print("Despeguen")


#Ejercicios: 2

#Sumadora

suma = 0
numero = 1
while numero != 0:
    numero = input("ingrese un numero:")
    if numero.isdigit():
        numero = int(numero)
        suma += numero
        print(f"El numero ingresado es: {numero} y la suma acumulada es : {suma}")
    else:
        print("No ingresaste un numero.")


#Ejercicios: 3

#Multiplicadora

continuar = "1"
while continuar =="1":
    numero_usuario = input("Ingrese un numero de la tabla de multiplicar:")
    if not numero_usuario.isdigit():    #si  no es un numero termina el programa.
        exit("Chau por burro")
        
    numero_usuario = int(numero_usuario)
    contador = 0
    while contador < 10:
        contador += 1
        print(f"{contador} x {numero_usuario} = {numero_usuario*contador}")
    continuar = input("Si desea multiplicar otro numero coloque 1 sino no, 0:")


