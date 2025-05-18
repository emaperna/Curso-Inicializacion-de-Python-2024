#Ejercicio 1:

'''
Crear una lista de nombres y luego:
Imprimir la longitud de la lista.
Agregar un nuevo nombre al final de la lista.
Eliminar el primer nombre de la lista.
Buscar un nombre en la lista e imprimir si está o no presente.
Ordenar la lista alfabéticamente

'''

nombres = ["Emanuel", "Diego","Gaspar","Franco"]
nombre_buscado = "Diego"
print(f"La lista de integrantes esta formada por: {len(nombres)} integrantes {nombres}")

nombres.append("Juan")
print("Se ha añadido un integrante")

print(f"La lista ahora contiene {len(nombres)} integrantes {nombres}")

nombres.pop(0)
print("El primer integrante de la lista ha sido retirado")
print(nombres)

if nombre_buscado in nombres:
    print(f"El nombre {nombre_buscado} se encuentra en la lista")
else:
    print(f"El nombre {nombre_buscado} no se encuentra en la lista")

nombres.sort()
print(f" Lista ordenada Alfabeticamente: {nombres}")


#Ejercicio 2:


'''
Crear una lista de números y luego:
Calcular la suma de todos los números de la lista.
Encontrar el número máximo y mínimo de la lista.
Multiplicar cada número de la lista por 2.
Imprimir los números pares de la lista.

'''


numeros = [ 1, 2, 3, 4, 5]
print (f"La lista de numeros es: {numeros}")

suma = sum(numeros)
print(f"La suma Total de los numeros es: {suma}")

maximo = max(numeros)
minimo = min(numeros)
print(f"El numero maximo de la lista es el: {maximo}")
print(f"El numero minimo de la lista es el: {minimo}")

numeros = [numero * 2 for numero in numeros]
print(f"El Resultado de multiplicar x 2 los numeros de la lista es: {numeros}") 

for numero in numeros:
    if numero % 2 == 0:
        print(f"Los numeros pares de la lista son: {numero}")


#Ejercicio 3:


'''
Crear una lista de palabras y luego.
Contar cuántas veces aparece una palabra específica en la lista.
Invertir el orden de la lista.
Unir dos listas en una sola.
Dividir una lista en dos sublistas.

'''

palabras = ["Mate","Mate","Pc","Escritorio"]
print(f"la lista es {palabras}")

busca_palabras = palabras.count("Mate")
print(f"La palabra Mate aparece {busca_palabras} veces en la lista")

palabras.reverse()
print(f"La lista invertida es {palabras}")

palabras2 = ["Taza","Termo","Papeles","Impresora"]

lista_concatenada = palabras + palabras2
print(f"la lista unida es: {lista_concatenada}")

sublista = lista_concatenada[:2]
print (sublista)


#Ejercicio 4:

'''

Simular una cesta de la compra:
Crear una lista con los productos que se van a comprar.
Agregar un nuevo producto a la lista.
Eliminar un producto de la lista.
Imprimir la lista.

'''
lista_productos = ["Pan","Carne","Agua","Yerba","Azucar"]
print(f"Nuestra lista de compra es: {lista_productos}")


lista_productos.append("Manteca")
print(f"Se ha Anexado un producto: {lista_productos}")

lista_productos.remove("Pan")
print(f"Se ha Removido un producto: {lista_productos}")