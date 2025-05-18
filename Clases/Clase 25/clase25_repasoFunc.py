#funciones y procedimientos:

'''
Procedimiento:

Arranca con la palabra "def" y no devuelve ningun resultado y la funcion si
Contiene un return al final y una variable, con el nombre definido la llamariamos nuevamente dentro del codigo
podemos pasar argumentos y parametros ()


Funcion:

devuelve un resultado

'''

#ingresando 3 numeros indicar cual es el mayor.

def ingrese_un_numero():
    while True:
        numero = input("Ingrese un numero:")
        if numero.isdigit():
            numero = int (numero)
            if numero > 0:
                break
            else:
                print("ingrese un numero mayor a 0")
        else :
            print("Por favor ingrese un numero")
    return numero

mayor = 0
menor = 0
suma = 0
for contador in range(3):

    numero = ingrese_un_numero()   
    print(f"El {contador+1}° N° ingresado es: {numero}")
    if numero > mayor:
        mayor = numero
    if numero < menor or menor == 0:
        menor = numero
    suma = suma + numero
    
print(f"El numero mayor es: {mayor}")
print(f"El numero mayor es: {menor}")
print(f"El primedio es igual: {suma/3}")