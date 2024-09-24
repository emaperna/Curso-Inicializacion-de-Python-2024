#listas es tipo de datos(variable)

#print (es función)

#input, exit,str, list.

#funciones (para reutilizar lineas de codigo) escritas en snake_case. (devuelve un resultado)

#ejemplo de funcion

'''
def sumar():
    a = 1
    b = 2
    return a + b
print (sumar())
'''
def sumar( numero_1:int , numero_2:int ):
    resultado = numero_1 + numero_2
    #print (resultado)
    return resultado

numero_1 = int(input("Ingrese un numero para sumar:"))
numero_2 = int(input("Ingrese un numero para sumar:"))

resultado_suma = sumar(numero_1,numero_2) * 10 # a esta variable le asigno un funcion

print(resultado_suma)
