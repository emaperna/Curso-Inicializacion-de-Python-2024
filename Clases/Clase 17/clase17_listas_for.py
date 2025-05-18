#recorrer la lista
#nombre = "pame"

#listas=["hola",1,True,"chau",nombre]
#for lista in listas:
#    print(lista)

import random

listas = ["Diego","Gaspar","Pame","Agustin","Brisa","Cristian","Camila","Franco","Emanuel"]

seleccionado = random.choice(listas)

listas_seleccionadas = ["Brisa","Diego","Pame","Agustin","Cristian","Camila","Franco","Gaspar"]

recorrido = listas

if (listas_seleccionadas == listas):
    print("No hay mas alumnos para seleccionar")
    exit()
        
if (listas == seleccionado):
    listas.remove(seleccionado)
    seleccionado=random.choice(listas)
else:
    print(f"El alumno seleccionado es: {seleccionado}")
    exit()

print(f"El alumno/a suertudo para salir a programar es {seleccionado}")
#for lista in listas:
#    print(lista)